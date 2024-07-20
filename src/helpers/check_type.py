from typing import Any, Type, Union, get_origin, get_args


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
        elif origin_type is dict:
            key_type, value_type = inner_types
            return all(checkType(k, key_type) and checkType(v, value_type) for k, v in variable.items())
    
    # If none of the above, return False
    return False