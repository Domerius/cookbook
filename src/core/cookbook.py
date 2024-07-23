from typing import List, Union, Any, Callable, Iterable, TypeVar, Generic, get_origin, get_args
from abc import ABC

from .difficulty import Difficulty
from .ingredient import Ingredient
from .recipe import Recipe
from ..helpers import checkType


# Generic types for type hints
T = TypeVar("T")
G = TypeVar("G")


class Classifier(ABC):
    """
    An abstract class handling sorting and filtering of an object.
    """

    def _getSortingOrder(self, sortingBase: List[Union[G, List[G]]], reverse: bool = False) -> List[int]:
        return sorted(range(len(sortingBase)), key=lambda i: sortingBase[i], reverse=reverse)

    def __filterStructureByMultipleKeys(self, filteringBase: List[Union[G, List[G]]], keys: List[G], mutualExclusion: bool) -> List[int]:
        """
        Filters the filtering_base based on the presence of keys.

        Parameters:
        - filteringBase: List serving as the base for filtering. Can contain elements or lists of elements.
        - keys: List of keys to filter by.
        - mutualExclusion: If True, all keys must be present in an element. If False, any key can be present.

        Returns:
        - List[int]: Indices of elements in filtering_base that match the filter criteria.
        """

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
        return [i for i, item in enumerate(filteringBase) if filteringFunc(item)]

    def __filterStructureBySingleKey(self, filteringBase: List[Union[G, List[G]]], key: G) -> List[int]:
        """
        Filters the filtering_base based on the presence of a single key.

        Parameters:
        - filteringBase: List serving as the base for filtering. Can contain elements or lists of elements.
        - keys: List of keys to filter by.
        - mutualExclusion: If True, all keys must be present in an element. If False, any key can be present.

        Returns:
        - List[int]: Indices of elements in filtering_base that match the filter criteria.
        """

        # Check if the key is a single item
        if len(key) > 1:
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
        return [i for i, item in enumerate(filteringBase) if filteringFunc(item)]

    # Jak dojdę do wniosku, że muszę zmienić filtrowanie w Cookbook, to to dalej będzie bazą pod tamto
    def _filterStructure(self, unfilteredStruct: List[T], filteringBase: List[Union[G, List[G]]], keys: Union[G, List[G]], mutualExclusion: bool) -> List[T]:
        # Call the correct function depending on input keys
        if get_origin(keys) == List:
            mask = self.__filterStructureByMultipleKeys(filteringBase, keys, mutualExclusion)
        else:
            mask = self.__filterStructureBySingleKey(filteringBase, keys)
        return [unfilteredStruct[i] for i in mask]

class Cookbook(Classifier):
    """
    Contains all recipes, manages them into files, allows sorting and filtering.

    Parameters:
        recipes (np.array[Recipe]): List of every registered recipe in the app.
    """

    def __init__(self, recipes: List[Recipe]):
        self._recipes = recipes

    def __str__(self):
        pass

    def __repr__(self):
        return self._recipes
    
    def sortRecipesAlphabetically(self, reverse: bool = False) -> None:
        sortingBase = [recipe.nameFull for recipe in self._recipes]
        order = super()._getSortingOrder(sortingBase, reverse)
        self._recipes = [self._recipes[i] for i in order]

    def sortRecipesByIngredientCount(self, reverse: bool = False) -> None:
        sortingBase = [len(recipe.ingredients) for recipe in self._recipes]
        order = super()._getSortingOrder(sortingBase, reverse)
        self._recipes = [self._recipes[i] for i in order]

    def sortRecipesByDifficulty(self, reverse: bool = False) -> None:
        sortingBase = [(recipe.difficulty is not None, recipe.difficulty) for recipe in self._recipes] if reverse else [(recipe.difficulty is None, recipe.difficulty) for recipe in self._recipes]
        order = super()._getSortingOrder(sortingBase, reverse)
        self._recipes = [self._recipes[i] for i in order]

    def sortRecipesByEstimatedTime(self, reverse: bool = False) -> None:
        # Get sorting order from the base and then apply the sorting order to the cookbook
        sortingBase = [(recipe.estimatedTime is not None, recipe.estimatedTime) for recipe in self._recipes] if reverse else [(recipe.estimatedTime is None, recipe.estimatedTime) for recipe in self._recipes]
        order = super()._getSortingOrder(sortingBase, reverse)
        self._recipes = [self._recipes[i] for i in order]
        # https://stackoverflow.com/questions/18411560/sort-list-while-pushing-none-values-to-the-end
    
    def filterRecipesByNamePhrases(self, keys: List[str], mutualExclusion: bool = False) ->  list[Recipe]:
        filteringBase = [recipe.nameFull for recipe in self._recipes]
        mask = super()._filterStructure(filteringBase, keys, mutualExclusion)
        return [self._recipes[i] for i in mask]

    def filterRecipesByIngredients(self, keys: List[G], mutualExclusion: bool = False) -> list[Recipe]:
        filteringBase = [recipe.ingredients for recipe in self._recipes]
        mask = super()._filterStructure(filteringBase, keys, mutualExclusion)
        return [self._recipes[i] for i in mask]

    def filterRecipesByDifficulty(self, filteringBase: List[G | List[G]], keys: List[G], mutualExclusion: bool = False) -> list[Recipe]:
        filteringBase = [recipe.difficulty for recipe in self._recipes]
        mask = super()._filterStructure(filteringBase, keys, mutualExclusion)
        return [self._recipes[i] for i in mask]

    def filterRecipesByEstimatedTime(self, filteringBase: List[G | List[G]], keys: List[G], mutualExclusion: bool = False) -> list[Recipe]:
        filteringBase = [recipe.estimatedTime for recipe in self._recipes]
        mask = super()._filterStructure(filteringBase, keys, mutualExclusion)
        return [self._recipes[i] for i in mask]
    
    def __createFileFromRecipe(self):
        pass

    def __updateFileWithRecipe(self):
        pass

    def __RemoveFileWithRecipe(self):
        pass

    def __getRecipeFromFile(self):
        pass

    # Można zrobić operacje na plikach w osobnej klasie i potem np. __getRecipeFromFile = __getRecipeFromFile(self, self._cookbook) (dziedziczenie)
    # Można też to samo zrobić dla filtrowania. Nie wiem, klasa abstrakcyjna gdzie jest jedna funkcja, która filtruje (i może sortuje) ze względu na wskazaną kolumnę (pole klasy).