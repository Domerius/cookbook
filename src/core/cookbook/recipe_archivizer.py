from typing import List
import os
import json

from ..difficulty import Difficulty
from ..ingredient import Ingredient
from ..recipe import Recipe

from .cookbook_base import CookbookBase


DIR_PATH = "..../recipes"

class RecipeArchivizer(CookbookBase):
    """
    An abstract class managing files associated with recipes of the Cookbook class.
    Recipes are saved in files as JSONs.
    """

    def __init__(self) -> None:
        super(RecipeArchivizer, self).__init__()
        self.__path = DIR_PATH

    def _createFile(self, recipe: Recipe) -> bool:
        """ Try creating a file - write the recipe into the file if it hasn't existed before call. """

        fileName = recipe.nameCompressed
        filePath = self.__path + "/" + fileName + ".json"
        if not os.path.exists(filePath):
            with open(filePath, "w") as openfile:
                json.dump(recipe.getJSON(), openfile)
            return True
        else:
            return False
        
    def _updateFile(self, recipe: Recipe) -> bool:
        """ Try finding a file - overwrite it if found. """

        fileName = recipe.nameCompressed
        filePath = self.__path + "/" + fileName + ".json"
        if os.path.exists(filePath):
            with open(filePath, "w") as openfile:
                json.dump(recipe.getJSON(), openfile)
            return True
        else:
            return False
        
    def _removeFile(self, fileName: str) -> bool:
        """ Try to find the pointed file - remove it if found. """

        filePath = self.__path + "/" + fileName
        if os.path.exists(filePath):
            os.remove(filePath)
            return True
        else:
            return False

    def _getFileNames(self) -> List[str]:
        """ Return a list of all files in the 'recipes' directory. """

        # It may be usefull to check whether all files are .json just in case
        return os.listdir(self.__path)

    def _readFile(self, fileName: str) -> Recipe:
        """ Try to read a file - if not succesful raise an exception. """

        filePath = self.__path + "/" + fileName
        if os.path.exists(filePath):
            with open(fileName, 'r') as openfile:
                jsonData = json.load(openfile)
        else:
            raise FileNotFoundError(f"There's no file called {fileName} in 'recipes' directory. " \
                                    f"Should be one of the following: {self.getFileNames()}")
        
        # Interpret read data as an object of the Recipe class
        return Recipe.fromJSON(jsonData)