class Ingredient:
    def __init__(self, name: str, measure: float, unit: str):
        self.__name = name
        self.__measure = measure
        self.__unit = unit
        # TODO: Classification into categories (eg. liquids, spices).
    
    def __str__(self):
        return f"{self.__measure} {self.__unit} of {self.__name}"
    
    def __repr__(self):
        return f"{type(self).__name__}(name='{self.__name}', measure={self.__measure}, unit={self.__unit})"