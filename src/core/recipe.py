from __future__ import annotations
from string import punctuation, digits
from typing import List, Union

from .difficulty import Difficulty
from .ingredient import Ingredient
from ..helpers import checkType


def compressName(name: str) -> str:
    """
    Transform name of the recipe into a shortened form. Punctuation and digits are being removed from input.
    """

    # Erase all punctuation and digits and seperate remaining words 
    nameSplit = name.translate(str.maketrans('', '', punctuation + digits)).split()

    # Join words together into the compressed name
    if len(nameSplit) == 0:
        raise TypeError(f"Wrong input name: {name}.")
    elif len(nameSplit) == 1:
        # Leave the word as it is
        return nameSplit[0].capitalize()
    else:
        nameCompressed = ''
        for word in nameSplit:
            nameCompressed += word[0:2].capitalize()
        return nameCompressed
    

class Recipe:
    """
    Contains informations about a single recipe from the cookbook.

    Parameters:
        name (str): Name of the recipe
        ingredients (list[Ingredient]): List of needed ingeredients
        description (str): Description mainly containing instructions for making the recipe
        estimatedTime (int): Estimated time which is supposed to take in order to prepare the meal
        difficulty (Difficulty): Subjective difficulty of the recipe
        relatedLinks (str): Hiperlinks directing to related web pages
    """

    def __init__(self, name: str, ingredients: List[Ingredient], description: Union[str, List[str]], **kwargs):
        """
        Initialises Recipe object:

        Parameters:
            name (str): Name of the recipe
            ingredients (list[Ingredient]): List of needed ingeredients
            description (str): Description mainly containing instructions for making the recipe
            **kwargs: Accepts all optional class parameters
        """

        # Check if argument types are correct and make sense
        if not checkType(name, str):
            raise TypeError(f"Parameter 'name' has wrong type: {type(name)}. " \
                            "Should be str.")
        if not checkType(ingredients, list) or len(ingredients) < 2:
            raise TypeError(f"Parameter 'ingredients' has wrong type: {type(ingredients)} or contains too little entries: {len(ingredients)}. " \
                            "Type should be list[Ingredient] and the list is supposed to have at least 2 elements.")
        if not checkType(description, Union[str, List[str]]):
            raise TypeError(f"Parameter 'description' has wrong type: {type(name)}. " \
                            "Should be str or list[str].")
        
        # Assign mandatory arguments
        self.nameFull = name
        self.__nameCompressed = compressName(name)
        self.ingredients = ingredients
        self.description = description  if  isinstance(description, str)  else  "\t{}\n".format('\n\t'.join(description))
        
        # Assign optional keyword arguments
        keywords = {"estimatedTime": int, "difficulty": Difficulty, "relatedLinks": Union[str, List[str]]}
        for key in keywords.keys():
            if key in kwargs.keys():
                if checkType(kwargs[key], keywords[key]):
                    setattr(self, key, kwargs[key])
                else:
                    raise TypeError(f"Optional parameter {key} has wrong type: {type(kwargs[key])}. " \
                                    f"Should be {keywords[key]}.")
            else:
                setattr(self, key, None)
    
    def __str__(self):
        # Start string with the name of the recipe
        str_out = "{}\n\n".format(self.nameFull)

        # Print out the difficulty (if such exists)
        if hasattr(self, "difficulty"):
            str_out += "Difficulty: {}\n\n".format(self.difficulty)

        # Print out the estimated time (if such exists)
        if hasattr(self, "estimatedTime"):
            str_out += "Estimated time: {} min\n\n".format(self.estimatedTime)
        
        # Print out the ingredients
        str_out += "Ingredients:"
        for ingredient in self.ingredients:
            str_out += "\n\t- {}".format(str(ingredient))
        str_out += "\n\n"

        # Print out the description
        str_out += "Description:\n{}".format(self.description)

        # Print out related links (if such exist)
        if hasattr(self, "relatedLinks"):
            if checkType(self.relatedLinks, List[str]):
                str_out += "\nRelated links:"
                for link in self.relatedLinks:
                    str_out += "\n\t{}".format(link)
            elif checkType(self.relatedLinks, str):
                str_out += "\n\nRelated links: {}".format(self.relatedLinks)

        return str_out