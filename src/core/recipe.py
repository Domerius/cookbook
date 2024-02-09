from __future__ import annotations
from string import punctuation, digits
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
        if isinstance(ingredients, list) and len(ingredients) > 1:
            self.ingredients = ingredients
        else:
            raise TypeError(f"Parameter 'ingredients' has wrong type: {type(ingredients)} or contains too little entries: {len(ingredients)}. " \
                            "Type should be list[Ingredient] and the list is supposed to have at least 2 elements.")
            
        # Assign description
        if isinstance(description, str):
            self.description = description
        elif isinstance(description, list):
            self.description = ""
            for paragraph in description:
                self.description += f"\t{paragraph}\n"
        else:
            raise TypeError(f"Parameter 'description' has wrong type: {type(name)}. " \
                            "Should be str or list[str].")
        
        # Assign optional keyword arguments
        keywords = {"estimatedTime": int, "difficulty": Difficulty, "relatedLinks": Union[str, list[str]]}
        for key in keywords.keys():
            if key in kwargs.keys():
                
                if isinstance(kwargs[key], get_args(keywords[key])):
                    setattr(self, key, kwargs[key])
                elif type(keywords[key]) is Literal and isinstance(kwargs[key], keywords[key]):
                    pass
                else:
                    raise TypeError(f"Optional parameter {key} has wrong type: {type(kwargs[key])}. " \
                                    f"Should be {keywords[key]}.")
            else:
                setattr(self, key, None)
    
    def __str__(self):
        str_out = f"{self.nameFull}\n\n"    # Start string with the name of the recipe

        # Print out the difficulty (if such exists)
        if hasattr(self, "difficulty"):
            str_out += f"Difficulty: {self.difficulty}\n\n"

        # Print out the estimated time (if such exists)
        if hasattr(self, "estimatedTime"):
            str_out += f"Estimated time: {self.estimatedTime} min\n\n"
        
        # Print out the ingredients
        str_out += "Ingredients:\n"
        for ingredient in self.ingredients:
            str_out += f"\t- {str(ingredient)}"
        str_out += "\n\n"

        # Print out the description
        str_out += f"Description:\n{self.description}"

        # Print out related links (if such exist)
        if hasattr(self, "relatedLinks"):
            if isinstance(self.relatedLinks, list):
                str_out += "\n\nRelated links:\n"
                for link in self.relatedLinks:
                    str_out += f"\t: {self.link}"
            elif isinstance(self.relatedLinks, str):
                str_out += f"\n\nRelated links: {self.relatedLinks}"

        return str_out