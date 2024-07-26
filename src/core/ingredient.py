from numbers import Number 

class Ingredient:
    """
    Contains informations about a single ingredient from the recipe.

    Parameters:
        name (str): Name of the ingredient
        measure (float): Measure of said ingredient
        unit (str): Measurement unit
    """

    def __init__(self, name: str, measure: float, unit: str = ''):
        """
        Initialises Ingredient object:

        Parameters:
            name (str): Name of the ingredient
            measure (float): Measure of said ingredient
            unit (str): Measurement unit
        """
        
        # Check if argument types are correct and make sense
        if not isinstance(name, str):
            raise TypeError(f"Parameter 'name' has wrong type: {type(name)}. " \
                            "Should be str.")
        if not isinstance(measure, Number):
            raise TypeError(f"Parameter 'measure' has wrong type: {type(measure)}. " \
                            "Should be any number type.")
        if measure <= 0:
            raise ValueError(f"Parameter 'measure' has wrong value: {measure}. " \
                             "Should be positive.")
        if not isinstance(unit, str):
            raise TypeError(f"Parameter 'unit' has wrong type: {type(unit)}. " \
                            "Should be str.")
        
        # Assign values
        self.name = name.lower()
        self.measure = measure
        self.unit = "pcs."  if  unit == ''  else  unit.lower()
    
    def __str__(self):
        """ Returns user-oriented representation of this class. """
        return f"{self.name}: {self.measure} {self.unit}"
    
    def __repr__(self):
        """ Returns developer-oriented representation of this class. """
        return f"{type(self).__name__}(name={self.name}, measure={self.measure}, unit={self.unit})"
    
    def __eq__(self, cls: object) -> bool:
        return all([getattr(self, attribute) == getattr(cls, attribute) for attribute in self.__dir__])