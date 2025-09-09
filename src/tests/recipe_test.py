from __future__ import annotations
from typing import List
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


# Tests of __init__
def test_init(name: str,
              ingredients: Ingredient,
              description: List[str]):
    """
    TEST 1: Check if the Recipe class initialises correctly.
    """
    
    # Expected description
    expected_description = ''
    for paragraph in description:
        expected_description += "\t{}\n".format(paragraph)

    recipe = Recipe(name, ingredients, description)
    
    assert recipe.nameFull == name
    assert recipe.ingredients == ingredients
    assert recipe.description == expected_description
    
def test_init_with_kwargs(name: str,
                          ingredients: Ingredient,
                          description: List[str],
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
                    ingredients: List[Ingredient],
                    description: List[str]):
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
                                ingredients: List[Ingredient],
                                description: List[str]):
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
def test_str_short(name: str,
                  ingredients: Ingredient,
                  description: List[str],
                  estimated_time: int,
                  difficulty: Difficulty,
                  related_links: str):
    """
    TEST 5: Check if the Recipe class with only basic arguments has right string representation.
    """

    """
    |=== Expected string ===|
    Naleśniki z serem
    
    Ingredients:
       - mąka: 500 g
       - ser biały: 20 dag
       - mleko: 0.2 l
    
    Description:
        Wymieszaj mąkę z serem. Wlej mleko i z miksuj.
        Podpiekaj na patelni aż się zetnie.
        Całość podawać z ulubionymi dodatkami!
    """

    expected_string_basic = "{}\n\n".format(name)
    expected_string_basic += "Ingredients:\n"
    for ingredient in ingredients:
        expected_string_basic += "\t- {}\n".format(str(ingredient))
    expected_string_basic += "\n"
    expected_string_basic += "Description:\n\t{}".format("\n\t".join(description))
    
    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert str(recipe) == expected_string_basic

def test_str_long(name: str,
                  ingredients: Ingredient,
                  description: List[str],
                  estimated_time: int,
                  difficulty: Difficulty,
                  related_links: str):
    """
    TEST 6: Check if the Recipe class with all argument has right string representation.
    """

    """
    |=== Expected string ===|
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
            
    expected_string_full = "{}\n\n".format(name)
    expected_string_full += "Difficulty: {}\n\n".format(difficulty)
    expected_string_full += "Estimated time: {} min\n\n".format(estimated_time)
    expected_string_full += "Ingredients:\n"
    for ingredient in ingredients:
        expected_string_full += "\t- {}\n".format(str(ingredient))
    expected_string_full += "\n"
    expected_string_full += "Description:\n\t{}".format("\n\t".join(description))
    expected_string_full += "\n\nRelated links:"
    for link in related_links:
        expected_string_full += "\n\t{}".format(link)
    
    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert str(recipe) == expected_string_full

def eq_test(name: str,
            ingredients: Ingredient,
            description: List[str],
            estimated_time: int,
            difficulty: Difficulty,
            related_links: str):
    
    recipe_1 = Recipe(name, ingredients, description,
                      estimated_time=estimated_time, difficulty=difficulty, related_links=related_links)
    recipe_2 = recipe_1
    assert recipe_1 == recipe_2

def get_json_test(name: str,
                  ingredients: Ingredient,
                  description: List[str],
                  estimated_time: int,
                  difficulty: Difficulty,
                  related_links: str):
    
    json_data = {}
    json_data["nameFull"] = name
    json_data["ingredients"] = ingredients
    json_data["description"] = "\t{}\n".format('\n\t'.join(description))
    json_data["estimatedTime"] = estimated_time
    json_data["difficulty"] = difficulty
    json_data["relatedLinks"] = related_links

    recipe = Recipe(name, ingredients, description,
                    estimated_time=estimated_time, difficulty=difficulty, related_links=related_links)
    
    assert recipe.getJSON() == json_data

def from_json_test(name: str,
              ingredients: Ingredient,
              description: List[str],
              estimated_time: int,
              difficulty: Difficulty,
              related_links: str):
    
    expected_recipe = Recipe(name, ingredients, description,
                             estimated_time=estimated_time, difficulty=difficulty, related_links=related_links)
    json_data = expected_recipe.getJSON()
    assert Recipe.fromJSON(json_data) == expected_recipe