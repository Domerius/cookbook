from typing import List

from .recipe_archivizer import RecipeArchivizer
from .recipe_organizer import RecipeOrganizer

class Cookbook(RecipeArchivizer, RecipeOrganizer):
    """
    Contains all recipes, manages them into files, allows sorting and filtering.

    Parameters:
        recipes (List[Recipe]): List of every registered recipe in the app.
    """

    def __init__(self, recipe):
        super(Cookbook, self).__init__(recipe)

    def __str__(self):
        return 

    def __repr__(self):
        return f"{type(self).__name__}(recipes={[recipe.__repr__ for recipe in self._recipes]})"
    
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
    
    # File management
    