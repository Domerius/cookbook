from typing import List, Union, Any, Callable, Iterable, TypeVar, Generic, get_origin, get_args

from .difficulty import Difficulty
from .ingredient import Ingredient
from .recipe import Recipe
from ..helpers import checkType


# Generic types for type hints
T = TypeVar("T")
G = TypeVar("G")


class Classifier:
    """
    An abstract class handling sorting and filtering of an object.
    """

    def _sortStructure(self, unsortedStruct: List[Any], sortingBase: List[Iterable], reverse: bool = False, method: Callable = None) -> None:
        # Get sorting order from the base and then apply it to the unsorted structure
        order = sorted(sortingBase, reverse=reverse, key=method)
        unsortedList = [unsortedList[i] for i in order]

    def __filterStructureByMultipleKeys(self, filteringBase: List[Union[G, List[G]]], keys: List[G], mutualExclusion: bool = False) -> List[int]:
        # A comment
        keysType = get_args(keys)
        if get_origin(keysType) == List:
            raise TypeError(f"Inputed keys have different types: {keysType}. Multiple keys are allowed only when are of the same type")
        
        # A function that the filtering bases on
        if all(checkType(item, List[type(keysType)]) for item in filteringBase):
            filteringFunc = lambda x: all(key in x for key in keys)  if  mutualExclusion  else  any(key in x for key in keys)
        elif all(checkType(item, type(keysType)) for item in filteringBase):
            filteringFunc = lambda x: any(key == x for key in keys)
        else:
            raise TypeError(f"Items of the filtering base has wrong type: {get_args(filteringBase)}. " \
                            f"Should be {type(keysType)} or List{type(keysType)}.")
        
        # Get filtering mask from the base
        return filter(filteringFunc, filteringBase)


    def __filterStructureBySingleKey(self, filteringBase: List[Union[G, List[G]]], key: G) -> List[int]:
        # A comment
        keyType = type(key)

        # A function that the filtering bases on
        if all(checkType(item, List[type(keyType)]) for item in filteringBase):
            filteringFunc = lambda x: key in x
        elif all(checkType(item, type(keyType)) for item in filteringBase):
            filteringFunc = lambda x: key == x
        else:
            raise TypeError(f"Items of the filtering base has wrong type: {get_args(filteringBase)}. " \
                            f"Should be {type(keyType)} or List{type(keyType)}.")
    
        # Get filtering mask from the base and then apply it to the unfiltered structure
        mask = filter(filteringFunc, filteringBase)


    # Jak dojdę do wniosku, że muszę zmienić filtrowanie w Cookbook, to to dalej będzie bazą pod tamto
    def _filterStructure(self, unfilteredStruct: List[T], filteringBase: List[Union[G, List[G]]], keys: Union[G, List[G]], mutualExclusion: bool = False) -> List[T]:
        if mutualExclusion and get_origin(keys) == List and get_origin(get_args(filteringBase)) != List:
            raise TypeError(f"The base to filter of type {type(filteringBase)} will never satisfy such filtering condition.")
        
        if get_origin(keys) == List:
            mask = self.__filterStructureByMultipleKeys(filteringBase, keys, mutualExclusion)
        else:
            mask = self.__filterStructureBySingleKey(filteringBase, keys)
        return [filteringBase[i] for i in mask]


class Cookbook:
    pass
    """
    Contains all recipes, manages them into files, allows sorting and filtering

    Parameters:
        cookbook (list[Recipe]): List of every registered recipe in the app
    """"""

    def __init__(self, recipes: List[Recipe]):
        self._cookbook = None

    def __str__(self):
        pass

    def __repr__(self):
        return self._cookbook
    
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
"""