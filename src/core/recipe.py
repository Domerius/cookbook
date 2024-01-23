from string import punctuation, digits

from difficulty import Difficulty
from ingredient import Ingredient

def compressTitle(title: str):
    # Erase all punctuation and digits and seperate remaining words 
    titleSplit = title.translate(str.maketrans('', '', punctuation + digits)).split()
    # Join words together into the compressed title
    if len(titleSplit) == 0:
        # Exception: Wrong input title
        raise()
    elif len(titleSplit) == 1:
        # Leave the word as it is
        return titleSplit[0].capitalize()
    else:
        titleCompressed = ''
        for word in titleSplit:
            titleCompressed += word[0:2].capitalize()
        return titleCompressed
    

class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient], description: Union(str, list[str]), **kwargs):
        # Assign title and its shorted version
        if type(title) == str:
            self.titleFull = title
            self.__titleCompressed = compressTitle(title)
        else:
            # Exception: Wrong type of entered title
            raise()
        
        # Assign ingredients
        if type(ingredients) == list[Ingredient] and len(ingredients) > 1:
            self.ingredients = ingredients
        else:
            # Exception: Inputed ingredients have wrong type or the list contains of very few items
            raise()
            
        # Assign description
        if type(description) == str:
            self.description = description
        elif type(description) == list[str]:
            self.description = ''.join('\n', description)
        else:
            # Exception: Given description has wrong type
            raise()
        
        # Assign optional keyword arguments
        keywords = ["estimatedTime", "difficulty", "relatedLinks"]
        for keyword in keywords:
            # TODO: Check if more optimal
            if keyword in kwargs.keys:
                pass
            else:
                pass
        
        if "estimatedTime" in kwargs.keys:
            self.estimatedTime = kwargs["estimatedTime"]
        else:
            self.estimatedTime = None
            
        if "difficulty" in kwargs.keys:
            self.difficulty = kwargs["difficulty"]
        else:
            self.difficulty = None
            
        if "relatedLinks" in kwargs.keys:
            self.relatedLinks = kwargs["relatedLinks"]
        else:
            self.relatedLinks = None
                