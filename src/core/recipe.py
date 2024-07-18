from __future__ import annotations
from string import punctuation, digits
from typing import Any, Type, Union, get_origin, get_args

from .difficulty import Difficulty
from .ingredient import Ingredient


def checkType(variable: Any, expected_type: Type):
    """
    Check whether a variable has a correct type.
    Created to handle both built-in types and more complex containers like lists or dictionaries having regard to its inner types.

    Parameters:
        variable: A variable that is being evaluated
        type: Expected type of the variable (eg. int, list[str], dict[str, int])
    """

    origin_type = get_origin(expected_type)
    
    # If origin_type is None, it's a basic type
    if origin_type is None:
        return isinstance(variable, expected_type)
    
    # If the expected_type is a Union
    if origin_type is Union:
        return any(checkType(variable, arg) for arg in get_args(expected_type))
    
    # If the expected_type is a generic type (e.g. list[str])
    if origin_type in (list, dict, tuple, set):
        if not isinstance(variable, origin_type):
            return False
        
        inner_types = get_args(expected_type)
        # If there's no inner types, assume that the correct origin type is a satisfying condition
        if inner_types == None:
            return True
        
        # Check inner types (e.g. list[str] should check str)
        if origin_type in (list, tuple, set):
            return all(checkType(item, inner_types[0]) for item in variable)
        # Check
        elif origin_type is dict:
            key_type, value_type = inner_types
            return all(checkType(k, key_type) and checkType(v, value_type) for k, v in variable.items())
        
        """
        elif origin_type is tuple:
            if len(variable) != len(inner_types):
                return False
            return all(checkType(item, inner_types[i]) for i, item in enumerate(variable))
        
        elif origin_type is set:
            return all(checkType(item, inner_types[0]) for item in variable)
        """
    
    # If none of the above, return False
    return False


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

        if not checkType(name, str):
            raise TypeError(f"Parameter 'name' has wrong type: {type(name)}. " \
                            "Should be str.")
        if not checkType(ingredients, list) or len(ingredients) < 2:
            raise TypeError(f"Parameter 'ingredients' has wrong type: {type(ingredients)} or contains too little entries: {len(ingredients)}. " \
                            "Type should be list[Ingredient] and the list is supposed to have at least 2 elements.")
        if not checkType(description, Union[str, list[str]]):
            raise TypeError(f"Parameter 'description' has wrong type: {type(name)}. " \
                            "Should be str or list[str].")
        
        # Assign mandatory arguments
        self.nameFull = name
        self.__nameCompressed = compressName(name)
        self.ingredients = ingredients
        self.description = description  if  isinstance(description, str)  else  f"\t{"\n\t".join(description)}\n"
        
        # Assign optional keyword arguments
        keywords = {"estimatedTime": int, "difficulty": Difficulty, "relatedLinks": Union[str, list[str]]}
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
        str_out = f"{self.nameFull}\n\n"    # Start string with the name of the recipe

        # Print out the difficulty (if such exists)
        if hasattr(self, "difficulty"):
            str_out += f"Difficulty: {self.difficulty}\n\n"

        # Print out the estimated time (if such exists)
        if hasattr(self, "estimatedTime"):
            str_out += f"Estimated time: {self.estimatedTime} min\n\n"
        
        # Print out the ingredients
        str_out += "Ingredients:"
        for ingredient in self.ingredients:
            str_out += f"\n\t- {str(ingredient)}"
        str_out += "\n\n"

        # Print out the description
        str_out += f"Description:\n{self.description}"

        # Print out related links (if such exist)
        if hasattr(self, "relatedLinks"):
            if checkType(self.relatedLinks, list[str]):
                str_out += "\nRelated links:"
                for link in self.relatedLinks:
                    str_out += f"\n\t{link}"
            elif checkType(self.relatedLinks, str):
                str_out += f"\n\nRelated links: {self.relatedLinks}"

        return str_out