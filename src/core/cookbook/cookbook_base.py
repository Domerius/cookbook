from typing import List
from abc import ABC

from ..recipe import Recipe


class CookbookBase(ABC):
    """
    An abstract class containing pieces of the Cookbook class necessary for the remaining parts of the class.
    """

    def __init__(self, recipes: List[Recipe]) -> None:
        super(CookbookBase, self).__init__(recipes)
        self._recipes = recipes