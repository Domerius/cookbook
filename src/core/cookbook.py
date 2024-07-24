from typing import List, Union, Any, Container, TypeVar, get_origin
import numpy as np
from abc import ABC

from .difficulty import Difficulty
from .ingredient import Ingredient
from .recipe import Recipe
from ..helpers import checkType


# Generic types for type hints
T = TypeVar("T")
G = TypeVar("G")

class CookbookBase(ABC):
    def __init__(self, recipes: List[Recipe]) -> None:
        self._recipes = recipes

class RecipeOrganizer(CookbookBase):
    """
    An abstract class handling sorting and filtering of the recipes in the Cookbook class.
    """

    def _sortRecipes(self, attribute: str, reverse: bool = False) -> None:
        """
        Filters the filtering_base based on the presence of keys.

        Parameters:
        - attribute (str): A name of the Recipe's field serving as the base for sorting.
        - reverse (bool): List of keys to filter by.
        """

        if attribute not in Recipe.__dir__:
            raise TypeError(f"The Recipe class doesn't have a field of type {attribute}. " \
                            f"Should be one of the following: {Recipe.__dir__}")
        
        # Create a base for sorting - additional column allows pushing None values to the end
        moveToEnd = lambda x: x is not None if reverse else x is None
        sortingBase = np.array([(getattr(recipe, attribute), moveToEnd(getattr(recipe, attribute))) for recipe in self._recipes])
        # Get sorting order firstly sorting by target value and then push None values to the end of the order
        order = sortingBase[sortingBase[:, 0].argsort(kind='stable')[::-1]] if reverse else sortingBase[sortingBase[:, 0].argsort(kind='stable')]
        order = order[order[:,1].argsort(kind='stable')]
        # Apply the new order to the whole list of recipes
        self._recipes[:] = [self._recipes[i] for i in order]
    
    def __filterRecipesByMultipleKeys(self, attribute: str, keys: List[Any], mutualExclusion: bool) -> List[int]:
        """
        Filters the filtering_base based on the presence of keys.

        Parameters:
        - attribute (str): A name of the Recipe's field serving as the base for filtering.
        - keys (List[Any]): List of keys to filter by.
        - mutualExclusion (bool): If True, all keys must be present in an element. If False, any key can be present.

        Returns:
        - List[int]: Indices of elements that match the filter criteria for the chosen attribute.
        """

        # Check if the attribute of the Recipe class is chosen correctly
        if attribute not in Recipe.__dir__:
            raise TypeError(f"The Recipe class doesn't have a field of type {attribute}. " \
                            f"Should be one of the following: {Recipe.__dir__}")
        
        # Create a list for filtering to base on by extracting the value from beneath the chosen attribute
        # We don't need to worry about None values - they will be ignored automatically as they won't match any key
        filteringBase = [getattr(recipe, attribute) for recipe in self._recipes]

        # If the base for filtering doesn't contain of lists of items, there's no possibility for any item to match multiple keys
        baseTypes = set(type(item) for item in filteringBase)
        if mutualExclusion and not all(type == List for type in baseTypes):
            raise TypeError(f"The base for filtering of {'types' if len(baseTypes) > 1 else 'type'} {baseTypes} will never satisfy such filtering condition.")

        # Check whether there are multiple keys to filter by
        keyTypes = set(type(key) for key in keys)
        if len(keyTypes) > 1:
            raise TypeError(f"Input keys have different types: {keyTypes}. Multiple keys must be of the same type.")
        keysType = keyTypes.pop()
        
        # A function that the filtering bases on
        if all(checkType(item, str) for item in filteringBase) and keysType == str:
            filteringFunc = lambda x: all(key in x for key in keys) if mutualExclusion else any(key in x for key in keys)  # To be replaced by a separate function
        elif all(checkType(item, List[type(keysType)]) for item in filteringBase):
            filteringFunc = lambda x: all(key in x for key in keys) if mutualExclusion else any(key in x for key in keys)
        elif all(checkType(item, type(keysType)) for item in filteringBase):
            filteringFunc = lambda x: any(key == x for key in keys)
        else:
            raise TypeError(f"Items of the filtering base have the wrong type. " \
                            f"Should be {type(keysType)} or List{type(keysType)}.")
        
        # Apply the filtering function and return indices of matching elements
        return [idx for idx, item in enumerate(filteringBase) if filteringFunc(item)]

    def __filterRecipesBySingleKey(self, attribute: str, key: Any) -> List[int]:
        """
        Filters the filtering_base based on the presence of a single key.

        Parameters:
        - attribute (str): A name of the Recipe's field serving as the base for filtering.
        - key (Any): A key to filter by.

        Returns:
        - List[int]: Indices of elements that match the filter criteria for the chosen attribute.
        """

        # Check if the attribute of the Recipe class is chosen correctly
        if attribute not in Recipe.__dir__:
            raise TypeError(f"The Recipe class doesn't have a field of type {attribute}. " \
                            f"Should be one of the following: {Recipe.__dir__}")
        
        # Create a list for filtering to base on by extracting the value from beneath the chosen attribute
        # We don't need to worry about None values - they will be ignored automatically as they won't match any key
        filteringBase = [getattr(recipe, attribute) for recipe in self._recipes]

        # Check if the key is a single item
        if get_origin(key) is Container and len(key) > 1:
            raise TypeError(f"Input key has multiple values: {key}.")

        # A function that the filtering bases on
        keyType = type(key)
        if all(checkType(item, str) for item in filteringBase) and keyType == str:
            filteringFunc = lambda x: key in x  # To be replaced by a separate function
        elif all(checkType(item, List[type(keyType)]) for item in filteringBase):
            filteringFunc = lambda x: key in x
        elif all(checkType(item, type(keyType)) for item in filteringBase):
            filteringFunc = lambda x: key == x
        else:
            raise TypeError(f"Items of the filtering base have the wrong type. " \
                            f"Should be {type(keyType)} or List{type(keyType)}.")
    
        # Apply the filtering function and return indices of matching elements
        return [idx for idx, item in enumerate(filteringBase) if filteringFunc(item)]

    def _filterRecipes(self, attribute: str, keys: Union[G, List[G]], mutualExclusion: bool) -> List[int]:
        """
        Filters the filtering_base based on the presence of a single key.

        Parameters:
        - attribute (str): A name of the Recipe's field serving as the base for filtering.
        - keys (List[Any]): List of keys to filter by.
        - mutualExclusion (bool): If True, all keys must be present in an element. If False, any key can be present.

        Returns:
        - List[Recipe]: Recipes that match the filter criteria for the chosen attribute.
        """

        # Call the correct function depending on input keys and return indices of filtered recipes
        if get_origin(keys) == List:
            return self.__filterRecipesByMultipleKeys(attribute, keys, mutualExclusion)
        else:
            return self.__filterRecipesBySingleKey(attribute, keys)
    

class Cookbook(RecipeOrganizer):
    """
    Contains all recipes, manages them into files, allows sorting and filtering.

    Parameters:
        recipes (np.array[Recipe]): List of every registered recipe in the app.
    """

    def __init__(self, recipe):
        super().__init__(recipe)

    def __str__(self):
        pass

    def __repr__(self):
        return self._recipes
    
    # Sorting methods - for sorting by more than 1 criterium call the methods one after another (last one will lead)
    def sortRecipesAlphabetically(self, reverse: bool = False) -> None:
        super()._sortRecipes("nameFull", reverse)

    def sortRecipesByIngredientCount(self, reverse: bool = False) -> None:
        super()._sortRecipes("ingredientsCount", reverse)

    def sortRecipesByDifficulty(self, reverse: bool = False) -> None:
        super()._sortRecipes("difficulty", reverse)

    def sortRecipesByEstimatedTime(self, reverse: bool = False) -> None:
        super()._sortRecipes("estimatedTime", reverse)
    
    # Filtering methods - for filtering by more than 1 criterium call each method and pick a common part from each mask
    # Keep products of each method separatelly so you can reverse filtering
    def filterRecipesByNamePhrases(self, keys: List[str], mutualExclusion: bool = False) ->  list[int]:
        return super()._filterRecipes("nameFull", keys, mutualExclusion)
    
    def filterRecipesByNamePhrases(self, keys: List[str], mutualExclusion: bool = False) ->  list[int]:
        return super()._filterRecipes("ingredients", keys, mutualExclusion)

    def filterRecipesByNamePhrases(self, keys: List[str], mutualExclusion: bool = False) ->  list[int]:
        return super()._filterRecipes("difficulty", keys, mutualExclusion)

    def filterRecipesByNamePhrases(self, keys: List[str], mutualExclusion: bool = False) ->  list[int]:
        return super()._filterRecipes("estimatedTime", keys, mutualExclusion)