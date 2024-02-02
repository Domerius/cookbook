from __future__ import annotations
from string import punctuation, digits
from typeguard import check_type
from typing import Union

from .difficulty import Difficulty
from .ingredient import Ingredient

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

    def __init__(self, name: str, ingredients: list[Ingredient], description: Union[str, list[str]], **kwargs) -> None:
        """
        Initialises Recipe object:

        Parameters:
            name (str): Name of the recipe
            ingredients (list[Ingredient]): List of needed ingeredients
            description (str): Description mainly containing instructions for making the recipe
            **kwargs: Accepts all optional class parameters
        """

        # Assign name and its shorted version
        if isinstance(name, str):
            self.nameFull = name
            self.__nameCompressed = compressName(name)
        else:
            raise TypeError(f"Parameter 'name' has wrong type: {type(name)}. " \
                            "Should be str.")
        
        # Assign ingredients
        if check_type(ingredients, list[Ingredient]) and len(ingredients) > 1:
            self.ingredients = ingredients
        else:
            raise TypeError(f"Parameter 'ingredients' has wrong type: {type(ingredients)} or contains too little entries: {len(ingredients)}. " \
                            "Type should be list[Ingredient] and the list is supposed to have at least 2 elements.")
            
        # Assign description
        if isinstance(description, str):
            self.description = description
        elif check_type(description, list[str]):
            self.description = '\n'.join(description)
        else:
            raise TypeError(f"Parameter 'description' has wrong type: {type(name)}. " \
                            "Should be str or list[str].")
        
        # Assign optional keyword arguments
        keywords = {"estimatedTime": int, "difficulty": Difficulty, "relatedLinks": Union[str, list[str]]}
        for key in keywords.keys():
            if key in kwargs.keys():
                if check_type(kwargs[key], keywords[key]):
                    setattr(self, key, kwargs[key])
                else:
                    raise TypeError(f"Optional parameter {key} has wrong type: {type(kwargs[key])}. " \
                                    f"Should be {keywords[key]}.")
            else:
                setattr(self, key, None)
                