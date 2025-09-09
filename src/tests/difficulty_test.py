import pytest
from ..core import Difficulty


def test_init():
    """
    TEST 1: Check if the Difficulty class contains only of atributes EASY, MEDIUM and HARD.
    """
    
    assert len(Difficulty) == 3
    assert Difficulty.EASY in Difficulty
    assert Difficulty.MEDIUM in Difficulty
    assert Difficulty.HARD in Difficulty

def test_compare():
    """
    TEST 2: Check if EASY value of the Difficulty class is lower than MEDIUM and HARD etc.
    Also, check equality of two Difficulty instances.
    """

    assert Difficulty.EASY < Difficulty.MEDIUM
    assert Difficulty.MEDIUM < Difficulty.HARD
    assert Difficulty.HARD > Difficulty.EASY

    assert Difficulty.MEDIUM == Difficulty.MEDIUM

def test_compare_error():
    """
    TEST 3: Check if a wrong comparison raises an exception.
    """

    with pytest.raises(Exception) as e_info:
        print(Difficulty.EASY < 4)

    assert e_info.type is TypeError

def test_str():
    """
    TEST 4: Check if string representation of Difficulty atributes is correct.
    """

    outStr = str(Difficulty.EASY)
    assert outStr == "Easy"

    outStr = str(Difficulty.MEDIUM)
    assert outStr == "Medium"

    outStr = str(Difficulty.HARD)
    assert outStr == "Hard"