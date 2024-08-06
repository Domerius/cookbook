from typing import List, Union

from ..recipe import Recipe

from .recipe_archivizer import RecipeArchivizer
from .recipe_organizer import RecipeOrganizer

class Cookbook(RecipeArchivizer, RecipeOrganizer):
    """
    Contains all recipes, manages them into files, allows sorting and filtering.

    Parameters:
        recipes (List[Recipe]): List of every registered recipe in the app.
    """

    def __init__(self):
        super(Cookbook, self).__init__()
        self.__loadAllRecipes()
    
    def __findRecipeByName(self, name: str) -> int:
        """ Find a recipe of given name and return its index. """
        # Iterate through the Cookbook for search
        for idx in range(len(self._recipes)):
            if self._recipes[idx].nameFull == name:
                return idx
        return None
    
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
    def filterRecipesByNamePhrases(self, keys: Union[str,List[str]], mutualExclusion: bool = False) ->  List[int]:
        return super()._filterRecipesByKeys("nameFull", keys, mutualExclusion)
    
    def filterRecipesByIngredients(self, keys: Union[str,List[str]], mutualExclusion: bool = False) ->  List[int]:
        return super()._filterRecipesByKeys("ingredients", keys, mutualExclusion)

    def filterRecipesByDifficulty(self, keys: Union[str,List[str]], mutualExclusion: bool = False) ->  List[int]:
        return super()._filterRecipesByKeys("difficulty", keys, mutualExclusion)

    def filterRecipesByEstimatedTime(self, threshold: int) ->  List[int]:
        return super()._filterRecipesByLimit(self, "estimatedTime", threshold)
    
    # File management methods
    def addRecipe(self, recipe: Recipe) -> bool:
        """ Add a new recipe to the Cookbook and create a file associated to it. """
        # The name of the recipe is unique - there can't be another one the same.
        if self.__findRecipeByName(recipe.nameFull):
            raise ValueError(f"A recipe of name {recipe.nameFull} is already present in the Cookbook.")
        # Create a file associated with the recipe then add the recipe to the Cookbook
        if super()._createFile(recipe):
            self._recipes.append(recipe)
            return True
        return False

    def removeRecipe(self, recipe: Recipe) -> bool:
        """ Remove the recipe from the Cookbook and its associated file from the file system. """
        # Remove a file associated with the recipe then remove the recipe from the Cookbook
        if super()._removeFile(recipe):
            self._recipes.remove(recipe)
            return True
        return False

    def updateRecipe(self, recipe: Recipe) -> bool:
        """ Update contents of the recipe when changed by the user during runtime so it will load properly later. """
        # Find an instance of the recipe with the same name in the Cookbook and get its index
        idx = self.__findRecipeByName(recipe.nameFull)
        if not idx:
            raise ValueError(f"There's no known recipe of name {recipe.nameFull}")
        # Replace contentes of the recipe both in the Cookbook and in its associated file
        if super()._updateFile(recipe):
            self._recipes[idx] = recipe
            return True
        return False

    def __loadAllRecipes(self) -> bool:
        """ Load each recipe from file. Called on initialization of the Cookbook. """
        # Iterate through every file associated with a recipe and append them to the Cook
        for file in super()._getFileNames():
            if file:
                self._recipes.append(super()._readFile(file))
        return True
    
    # Magic methods
    def __str__(self):
        pass 

    def __repr__(self):
        return f"{type(self).__name__}(recipes={[recipe.__repr__ for recipe in self._recipes]})"
    