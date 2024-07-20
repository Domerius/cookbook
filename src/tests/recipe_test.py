from __future__ import annotations
import pytest
from ..core import Recipe, Ingredient, Difficulty

# Recipe's name fixtures
@pytest.fixture()
def name():
    return "Naleśniki z serem"

# Recipe's ingredients fixtures
@pytest.fixture()
def ingredients():
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    return [ingredient1, ingredient2, ingredient3]

# Recipe's description fixtures
@pytest.fixture()
def description():
    return ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
            "Podpiekaj na patelni aż się zetnie.", \
            "Całość podawać z ulubionymi dodatkami!"]

# Recipe's additional argument fixtures
@pytest.fixture()
def estimated_time():
    return 20

@pytest.fixture()
def difficulty():
    return Difficulty.EASY

@pytest.fixture()
def related_links():
    return ["https://pierwszastronainternetowa.com", "https://drugastronainternetowa.com"]

# Fixtures of expected values
@pytest.fixture()
def expected_description(description: list):
    
    """
    Wymieszaj mąkę z serem. Wlej mleko i z miksuj.
    Podpiekaj na patelni aż się zetnie.
    Całość podawać z ulubionymi dodatkami!
    """
    
    str_out = ''
    for paragraph in description:
        str_out += "\t{}\n".format(paragraph)
        
    return str_out

@pytest.fixture()
def expected_string(name: str,
                    ingredients: Ingredient,
                    description: list[str],
                    estimated_time: int,
                    difficulty: Difficulty,
                    related_links: list[str]):
    
    """
    Naleśniki z serem

    Difficulty: Easy

    Estimated time: 20 min

    Ingredients:
       - mąka: 500 g
       - ser biały: 20 dag
       - mleko: 0.2 l
       
    Description:
        Wymieszaj mąkę z serem. Wlej mleko i z miksuj.
        Podpiekaj na patelni aż się zetnie.
        Całość podawać z ulubionymi dodatkami!

    Related links:
        https://pierwszastronainternetowa.com
        https://drugastronainternetowa.com
    """
            
    str_out = "{}\n\n".format(name)
    str_out += "Difficulty: {}\n\n".format(difficulty)
    str_out += "Estimated time: {} min\n\n".format(estimated_time)
    str_out += "Ingredients:\n"
    for ingredient in ingredients:
        str_out += "\t- {}\n".format(str(ingredient))
    str_out += "\n"
    str_out += "Description:\n\t{}".format("\n\t".join(description))
    str_out += "\n\nRelated links:"
    for link in related_links:
        str_out += "\n\t{}".format(link)

    return str_out


# Tests of __init__
def test_init(name: str,
              ingredients: Ingredient,
              description: list[str],
              expected_description: str):
    """
    TEST 1: Check if the Recipe class initialises correctly.
    """

    recipe = Recipe(name, ingredients, description)
    
    assert recipe.nameFull == name
    assert recipe.ingredients == ingredients
    assert recipe.description == expected_description
    
def test_init_with_kwargs(name: str,
                          ingredients: Ingredient,
                          description: list[str],
                          estimated_time: int,
                          difficulty: Difficulty,
                          related_links: str):
    """
    TEST 2: Check if the Recipe class initialises correctly with additional arguments.
    """

    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert recipe.estimatedTime == estimated_time
    assert recipe.difficulty == difficulty
    assert recipe.relatedLinks == related_links
    
def test_init_error(name: str,
                    ingredients: list[Ingredient],
                    description: list[str]):
    """
    TEST 3: Check if the Recipe class handles exceptions properly.
    """
    
    # Wrong name type (list[str])
    with pytest.raises(Exception) as e_info:
        Recipe(["Nazwa", "przepisu", "w", "liście"], ingredients, description)

    assert e_info.type is TypeError
    
    # Wrong ingredients type (str)
    with pytest.raises(Exception) as e_info:
        Recipe(name, str(ingredients), description)

    assert e_info.type is TypeError
    
    # Wrong ingredients count (list w/ one element)
    with pytest.raises(Exception) as e_info:
        Recipe(name, [ingredients[1]], description)

    assert e_info.type is TypeError
    
    # Wrong description type (int)
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, 3)

    assert e_info.type is TypeError
    
def test_init_with_kwargs_error(name: str,
                                ingredients: list[Ingredient],
                                description: list[str]):
    """
    TEST 4: Check if the Recipe class handles more exceptions properly.
    """
    
    # Wrong estimatedTime type (str)
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               estimatedTime="4 min")

    assert e_info.type is TypeError

    # Wrong difficulty type (str)
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               difficulty="trudny")

    assert e_info.type is TypeError
    
    # Wrong relatedLinks type (int)
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               relatedLinks=4)

    assert e_info.type is TypeError

# Tests of __str__
def test_str(name: str,
             ingredients: Ingredient,
             description: list[str],
             estimated_time: int,
             difficulty: Difficulty,
             related_links: str,
             expected_string: str):
    """
    TEST 5: Check if the Recipe class has right string representation.
    """
    
    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert str(recipe) == expected_string