import pytest
from ..core import Recipe, Ingredient, Difficulty
from typeguard import TypeCheckError

# @pytest.fixture()
# def ():
#     return 

def test_init():
    """
    TEST 1: Check if the Recipe class initialises correctly
    """

    name = "Naleśniki z serem"
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    ingredients = [ingredient1, ingredient2, ingredient3]
    description = ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
        "Podpiekaj na patelni aż się zetnie.", \
        "Całość podawać z ulubionymi dodatkami!"]
    descriptionOut = "Wymieszaj mąkę z serem. Wlej mleko i z miksuj.\n" \
        "Podpiekaj na patelni aż się zetnie.\n" \
        "Całość podawać z ulubionymi dodatkami!"
    recipe = Recipe(name, ingredients, description)
    
    assert recipe.nameFull == name
    assert recipe.ingredients == ingredients
    assert recipe.description == descriptionOut
    
def test_init_with_kwargs():
    """
    TEST 2: Check if the Recipe class initialises correctly with additional arguments
    """

    name = "Naleśniki z serem"
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    ingredients = [ingredient1, ingredient2, ingredient3]
    description = ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
        "Podpiekaj na patelni aż się zetnie.", \
        "Całość podawać z ulubionymi dodatkami!"]
    estimatedTime = 20
    difficulty = Difficulty.EASY
    relatedLinks = "https:\\stronainternetowa.com"
    recipe = Recipe(name, ingredients, description, estimatedTime=estimatedTime, difficulty=difficulty, relatedLinks=relatedLinks)
    
    assert recipe.estimatedTime == estimatedTime
    assert recipe.difficulty == difficulty
    assert recipe.relatedLinks == relatedLinks
    
def test_init_error():
    """
    TEST 3: Check if the Recipe class handles exceptions properly 
    """

    name = "Naleśniki z serem"
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    ingredients = [ingredient1, ingredient2, ingredient3]
    description = ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
        "Podpiekaj na patelni aż się zetnie.", \
        "Całość podawać z ulubionymi dodatkami!"]
    
    # Wrong name type
    with pytest.raises(Exception) as e_info:
        Recipe(["Nazwa", "przepisu", "w", "liście"], ingredients, description)

    assert e_info.type is TypeError
    
    # Wrong ingredients type
    with pytest.raises(Exception) as e_info:
        Recipe(name, str(ingredients), description)

    assert e_info.type is TypeCheckError
    
    # Wrong ingredients count
    with pytest.raises(Exception) as e_info:
        Recipe(name, [ingredient1], description)

    assert e_info.type is TypeError
    
    # Wrong description type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, -1)

    assert e_info.type is TypeCheckError
    
def test_init_with_kwargs_error():
    """
    TEST 4: Check if the Recipe class handles more exceptions properly 
    """

    name = "Naleśniki z serem"
    ingredient1 = Ingredient("Mąka", 500, "g")
    ingredient2 = Ingredient("ser biały", 20, "dag")
    ingredient3 = Ingredient("Mleko", 0.2, "l")
    ingredients = [ingredient1, ingredient2, ingredient3]
    description = ["Wymieszaj mąkę z serem. Wlej mleko i z miksuj.", \
        "Podpiekaj na patelni aż się zetnie.", \
        "Całość podawać z ulubionymi dodatkami!"]
    
    # Wrong estimatedTime type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description, estimatedTime="20 min")

    assert e_info.type is TypeCheckError

    # Wrong difficulty type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description, difficulty="Trudne")

    assert e_info.type is TypeCheckError
    
    # Wrong relatedLinks type
    with pytest.raises(Exception) as e_info:
        Recipe(name, ingredients, description, relatedLinks=-1)

    assert e_info.type is TypeCheckError