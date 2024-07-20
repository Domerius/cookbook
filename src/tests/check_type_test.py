import pytest
from typing import List, Set, Tuple, Dict, Union

from ..helpers import checkType


# Base fixtures
@pytest.fixture()
def base_int():
    return [1, 2, 3, 4]

@pytest.fixture()
def base_str():
    return ["First paragraph", "Second paragraph", "Third paragraph", "Forth paragraph"]

@pytest.fixture()
def base_float():
    return [0.1, 0.2, 0.3, 0.4]

@pytest.fixture()
def base_bool():
    return [True, True, False, True]

@pytest.fixture()
def base_complex():
    return [0+1j, 0+2j, 0+3j, 0+4j]

# Custom class fixture
class custom():
    pass

@pytest.fixture()
def base_custom():
    return [custom() for i in range(1,4)]


def test_basic_type(base_int: int,
                    base_str: str,
                    base_float: float,
                    base_bool: bool,
                    base_complex: complex,
                    base_custom: custom):
    """
    TEST 1: Check if the function properly recognizes a variable of built-in type or a custom mock type.
    """

    # We iterate through each built-in and a custom type
    for var_type in [(base_int, int), (base_str, str), (base_float, float), (base_bool, bool), (base_complex, complex), (base_custom, custom)]:
        assert checkType(var_type[0][0], var_type[1])

def test_basic_type_death(base_int: int,
                          base_str: str,
                          base_float: float,
                          base_bool: bool,
                          base_complex: complex,
                          base_custom: custom):
    """
    TEST 2: Check if the function properly fails given a variable of the wrong built-in type or a custom mock type.
    """

    # We permutate each built-in and a custom type with each not matching type
    for var_type in [(base_int, int), (base_str, str), (base_float, float), (base_bool, bool), (base_complex, complex), (base_custom, custom)]:
        for type in [int, str, float, bool, complex, custom]:
            if not var_type[1] != type:
                assert checkType(var_type[0][0], var_type[1])

def test_list_set_tuple(base_int: int,
                        base_str: str,
                        base_float: float,
                        base_bool: bool,
                        base_complex: complex,
                        base_custom: custom):
    """
    TEST 3: Check if the function properly recognizes a list, a set and a tuple of any built-in type or a custom mock type.
    """

    # We iterate through built-in and a custom type
    for var_type in [(base_int, int), (base_str, str), (base_float, float), (base_bool, bool), (base_complex, complex), (base_custom, custom)]:
        assert checkType(list(var_type[0]), List[var_type[1]])
        assert checkType(set(var_type[0]), Set[var_type[1]])
        assert checkType(tuple(var_type[0]), Tuple[var_type[1]])

def test_dict(base_int: int,
              base_str: str,
              base_float: float,
              base_bool: bool,
              base_complex: complex,
              base_custom: custom):
    """
    TEST 4: Check if the function properly recognizes various dictionaries.
    """

    # We iterate through each combination of built-in and a custom type
    type_matrix = [(base_int, int), (base_str, str), (base_float, float), (base_bool, bool), (base_complex, complex), (base_custom, custom)]
    for key_type in type_matrix:
        for value_type in type_matrix:
            assert checkType({key:value for (key, value) in zip(key_type[0], value_type[0])}, Dict[key_type[1], value_type[1]])

def test_empty():
    """
    TEST 5: Check if the function properly recognizes an empty container
    """

    # Create empty conatiner of each type: list, set, tuple, dictionary
    empty_list = []
    empty_set = set([])
    empty_tuple = ()
    empty_dict = {}

    assert checkType(empty_list, list)
    assert checkType(empty_set, set)
    assert checkType(empty_tuple, tuple)
    assert checkType(empty_dict, dict)

def test_union(base_int: int):
    """
    TEST 6: Check if the function properly recognizes an union of various structures.
    """

    # Iterate through each type of structure of type int
    for var_type in [base_int[0], base_int, set(base_int), tuple(base_int), {key:value for (key,value) in zip(base_int, base_int)}]:
        assert checkType(var_type, Union[int, List[int], Set[int], Tuple[int], Dict[int, int]])

def test_union_death(base_int: int):
    """
    TEST 7: Check if the function properly fails an union of various structures.
    """

    # Various structures based on integer type
    basic_int = base_int[0]
    list_int = base_int
    set_int = set(base_int)
    tuple_int = tuple(base_int)
    dict_int = {key:value for (key,value) in zip(base_int, base_int)}

    assert not checkType(basic_int, Union[str, float, bool, complex, custom])
    assert not checkType(basic_int, Union[List[int], Set[int], Tuple[int], Dict[int, int]])
    assert not checkType(list_int, Union[int, Set[int], Tuple[int], Dict[int, int]])
    assert not checkType(set_int, Union[int, List[int], Tuple[int], Dict[int, int]])
    assert not checkType(tuple_int, Union[int, List[int], Set[int], Dict[int, int]])
    assert not checkType(dict_int, Union[int, List[int], Set[int], Tuple[int]])