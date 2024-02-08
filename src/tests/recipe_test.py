from __future__ import annotations
import pytest
from ..core import Recipe, Ingredient, Difficulty
from typeguard import TypeCheckError

# Recipe's name fixtures
@pytest.fixture()
def name():
    return "Naleśniki z serem"

@pytest.fixture()
def name_wrong_type():
    return ["Nazwa", "przepisu", "w", "liście"]

# Recipe's ingredients fixtures
@pytest.fixture()
def ingredients():
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    return [ingredient1, ingredient2, ingredient3]

@pytest.fixture()
def ingredients_wrong_type(ingredients: Ingredient):
    return str(ingredients)

@pytest.fixture()
def ingredients_wrong_value(ingredients: Ingredient):
    return [ingredients[1]]

# Recipe's description fixtures
@pytest.fixture()
def description():
    return ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
            "Podpiekaj na patelni aż się zetnie.", \
            "Całość podawać z ulubionymi dodatkami!"]

@pytest.fixture()
def expected_description():
    return "Wymieszaj mąkę z serem. Wlej mleko i z miksuj.\n" \
        "Podpiekaj na patelni aż się zetnie.\n" \
        "Całość podawać z ulubionymi dodatkami!"

@pytest.fixture()
def description_wrong_type():
    return 3

# Recipe's additional argument fixtures
@pytest.fixture()
def estimated_time():
    return 20

@pytest.fixture()
def estimated_time_wrong_type():
    return "4"

@pytest.fixture()
def difficulty():
    return Difficulty.EASY

@pytest.fixture()
def difficulty_wrong_type():
    return "trudny"

@pytest.fixture()
def related_links():
    return "https://stronainternetowa.com"

@pytest.fixture()
def related_links_wrong_type():
    return 5

# Recipe's general fixtures
@pytest.fixture()
def expected_string(name: str,
                    ingredients: Ingredient,
                    description: list[str],
                    estimated_time: int,
                    difficulty: Difficulty,
                    related_links: str):
    
    str_out = f"{name}\n\n"
    str_out += f"Difficulty: {difficulty}\n\n"
    str_out += f"Estimated time: {estimated_time} min\n\n"
    str_out += "Ingredients:\n"
    for ingredient in ingredients:
        str_out += f"\t- {str(ingredient)}"
    str_out += "\n\n"
    str_out += f"Description:\n{"\n".join(description)}"
    str_out += f"\n\nRelated links: {related_links}"

    return str_out

            # Naleśniki z serem

            # Difficulty: easy

            # Estimated time: 20 min

            # Ingredients:
            #    - mąka: 500 g   - ser biały: 20 dag     - mleko: 0.2 l
            # Description:
            # Wymieszaj mąkę z serem. Wlej mleko i z miksuj.
            # Podpiekaj na patelni aż się zetnie.
            # Całość podawać z ulubionymi dodatkami!

            # Related links: https://stronainternetowa.com

# Tests of __init__
def test_init(name: str,
              ingredients: Ingredient,
              description: list[str],
              expected_description: str):
    """
    TEST 1: Check if the Recipe class initialises correctly
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
    TEST 2: Check if the Recipe class initialises correctly with additional arguments
    """

    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert recipe.estimatedTime == estimated_time
    assert recipe.difficulty == difficulty
    assert recipe.relatedLinks == related_links
    
def test_init_error(name: str,
                    name_wrong_type: list[str],
                    ingredients: list[Ingredient],
                    ingredients_wrong_type: str,
                    ingredients_wrong_value: list[Ingredient],
                    description: list[str],
                    description_wrong_type: int):
    """
    TEST 3: Check if the Recipe class handles exceptions properly 
    """
    
    # Wrong name type
    with pytest.raises(Exception) as e_info:
        Recipe(name_wrong_type, ingredients, description)

    assert e_info.type is TypeError
    
    # Wrong ingredients type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients_wrong_type, description)

    assert e_info.type is TypeCheckError
    
    # Wrong ingredients count
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients_wrong_value, description)

    assert e_info.type is TypeError
    
    # Wrong description type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description_wrong_type)

    assert e_info.type is TypeCheckError
    
def test_init_with_kwargs_error(name: str,
                                ingredients: list[Ingredient],
                                description: list[str],
                                estimated_time_wrong_type: str,
                                difficulty_wrong_type: str,
                                related_links_wrong_type: int):
    """
    TEST 4: Check if the Recipe class handles more exceptions properly 
    """
    
    # Wrong estimatedTime type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               estimatedTime=estimated_time_wrong_type)

    assert e_info.type is TypeCheckError or e_info.type is TypeError

    # Wrong difficulty type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               difficulty=difficulty_wrong_type)

    assert e_info.type is TypeCheckError or e_info.type is TypeError
    
    # Wrong relatedLinks type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description,
               relatedLinks=related_links_wrong_type)

    assert e_info.type is TypeCheckError or e_info.type is TypeError

# Tests of __str__
def test_str(name: str,
             ingredients: Ingredient,
             description: list[str],
             estimated_time: int,
             difficulty: Difficulty,
             related_links: str,
             expected_string: str):
    """
    TEST 5: Check if the Recipe class has right string representation
    """
    
    recipe = Recipe(name, ingredients, description,
                    estimatedTime=estimated_time, difficulty=difficulty, relatedLinks=related_links)
    
    assert str(recipe) == expected_string