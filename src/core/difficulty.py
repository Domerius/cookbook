from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    
    def __str__(self):
        return self.name.lower()
    
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            raise TypeError(f"The Difficulty class instances may be compared only between each other. " \
                            f"Encountered types: {self.__class__} and {other.__class__}.")
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        else:
            raise TypeError(f"The Difficulty class instances may be compared only between each other. " \
                            f"Encountered types: {self.__class__} and {other.__class__}.")
    
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        else:
            raise TypeError(f"The Difficulty class instances may be compared only between each other. " \
                            f"Encountered types: {self.__class__} and {other.__class__}.")