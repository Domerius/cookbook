import pytest

from ..core import Recipe, Ingredient, Difficulty
from ..core.cookbook import Cookbook


@pytest.fixture()
def recipe_1():
    name = ...
    ingredients = ...
    description = ...
    difficulty = ...
    estimated_time = ...
    related_links = ...

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_2():
    name = ...
    ingredients = ...
    description = ...
    difficulty = ...
    estimated_time = ...
    related_links = ...

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_3():
    name = ...
    ingredients = ...
    description = ...
    difficulty = ...
    estimated_time = ...
    related_links = ...

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_4():
    name = ...
    ingredients = ...
    description = ...
    difficulty = ...
    estimated_time = ...
    related_links = ...

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_5():
    name = ...
    ingredients = ...
    description = ...
    difficulty = ...
    estimated_time = ...
    related_links = ...

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipes(recipe_1: Recipe,
            recipe_2: Recipe,
            recipe_3: Recipe,
            recipe_4: Recipe,
            recipe_5: Recipe):
    
    return [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]


def init_test():
    # Get all files and check whether they are read properly
    pass

def init_empty_test():
    pass

def sort_alphabetically_test():
    pass

def sort_ingredients_count_test():
    pass

def sort_difficulty_test():
    pass

def sort_by_estimated_time_test():
    pass

def filter_by_name_phrases_test():
    pass

def filter_ingredients_test():
    pass

def filter_difficulty_test():
    pass

def filter_by_estimated_time_test():
    pass

def add_remove_recipe_test():
    pass

def update_recipe_test():
    pass