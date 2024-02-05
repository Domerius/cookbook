import pytest
from ..core import Ingredient


# Name fixtures
@pytest.fixture()
def name_lowercase():
    return "mąka pszenna"

@pytest.fixture()
def name_capitalized():
    return "Mąka żytnia"

@pytest.fixture()
def name_countable():
    return "jajka"

@pytest.fixture()
def name_wrong_type():
    return 1

# Measure fixtures
@pytest.fixture()
def measure_uncountable():
    return 500

@pytest.fixture()
def measure_countable():
    return 5

@pytest.fixture()
def measure_wrong_type():
    return "5"

@pytest.fixture()
def measure_wrong_value():
    return -1

# Unit fixtures
@pytest.fixture()
def unit_lowercase():
    return "g"

@pytest.fixture()
def unit_capitalized():
    return "Kg"

@pytest.fixture()
def unit_wrong_type():
    return 9


def test_init(name_lowercase: str,
              measure_uncountable:Ingredient,
              unit_lowercase: str):
    """
    TEST 1: Check if the Ingredient class initialises correctly
    """

    ingredient = Ingredient(name_lowercase, measure_uncountable, unit_lowercase)
    assert ingredient.name == "mąka pszenna"
    assert ingredient.measure == 500
    assert ingredient.unit == "g"

def test_str(name_lowercase: str,
             measure_uncountable: Ingredient,
             unit_lowercase: str):
    """
    TEST 2: Check if string representation of the Ingredient class is correct
    """

    ingredient = Ingredient(name_lowercase, measure_uncountable, unit_lowercase)
    assert str(ingredient) == "mąka pszenna: 500 g"

def test_lowercase(name_capitalized: str,
                   measure_uncountable: Ingredient,
                   unit_capitalized: str):
    """
    TEST 3: Check if the Ingredient class converts strings to lowercase
    """

    ingredient = Ingredient(name_capitalized, measure_uncountable, unit_capitalized)
    assert ingredient.name == "mąka żytnia"
    assert ingredient.unit == "kg"

def test_countable(name_countable: str,
                   measure_countable: Ingredient):
    """
    TEST 4: Check if the Ingredient class manages countable articles
    """

    ingredient = Ingredient(name_countable, measure_countable)
    assert ingredient.unit == "pcs."
    assert str(ingredient) == "jajka: 5 pcs."

def test_init_error(name_lowercase: str,
                    name_wrong_type: int,
                    measure_uncountable: int,
                    measure_wrong_type: str,
                    measure_wrong_value: int,
                    unit_lowercase: str,
                    unit_wrong_type: int):
    """
    TEST 5: Check if the Ingredient class handles exceptions properly
    """
    
    # Wrong name type
    with pytest.raises(Exception) as e_info:
        Ingredient(name_wrong_type, measure_uncountable, unit_lowercase)

    assert e_info.type is TypeError

    # Wrong measure type
    with pytest.raises(Exception) as e_info:
        Ingredient(name_lowercase, measure_wrong_type, unit_lowercase)

    assert e_info.type is TypeError

    # Wrong measure value
    with pytest.raises(Exception) as e_info:
        Ingredient(name_lowercase, measure_wrong_value, unit_lowercase)

    assert e_info.type is ValueError

    # Wrong unit type
    with pytest.raises(Exception) as e_info:
        Ingredient(name_lowercase, measure_uncountable, unit_wrong_type)

    assert e_info.type is TypeError
