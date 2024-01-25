import pytest
from ..core import Ingredient

@pytest.fixture()
def ingredient_uncountable_lowercase():
    return Ingredient("mąka pszenna", 500, "g")

@pytest.fixture()
def ingredient_uncountable_capitalized():
    return Ingredient("Mąka żytnia", 0.5, "Kg")

@pytest.fixture()
def ingredient_countable():
    return Ingredient("jajka", 5)

def test_init(ingredient_uncountable_lowercase: Ingredient):
    """
    TEST 1: Check if the Ingredient class initialises correctly
    """

    assert ingredient_uncountable_lowercase.name == "mąka pszenna"
    assert ingredient_uncountable_lowercase.measure == 500.0
    assert ingredient_uncountable_lowercase.unit == "g"

def test_str(ingredient_uncountable_lowercase: Ingredient):
    """
    TEST 2: Check if string representation of the Ingredient class is correct
    """

    assert str(ingredient_uncountable_lowercase) == "mąka pszenna: 500 g"

def test_lowercase(ingredient_uncountable_capitalized: Ingredient):
    """
    TEST 3: Check if the Ingredient class converts strings to lowercase
    """

    assert ingredient_uncountable_capitalized.name == "mąka żytnia"
    assert ingredient_uncountable_capitalized.unit == "kg"

def test_countable(ingredient_countable: Ingredient):
    """
    TEST 4: Check if the Ingredient class manages countable articles
    """

    assert ingredient_countable.unit == "pcs."
    assert str(ingredient_countable) == "jajka: 5 pcs."

def test_init_error():
    """
    TEST 5: Check if the Ingredient class handles exceptions properly
    """
    
    # Wrong name type
    with pytest.raises(Exception) as e_info:
        Ingredient(-1, 500, "ml")

    assert e_info.type is TypeError

    # Wrong measure type
    with pytest.raises(Exception) as e_info:
        Ingredient("mleko", "", "ml")

    assert e_info.type is TypeError

    # Wrong unit type
    with pytest.raises(Exception) as e_info:
        Ingredient("mleko", 500, -1)

    assert e_info.type is TypeError
