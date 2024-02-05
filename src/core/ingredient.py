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

        # Assign name
        if isinstance(name, str):
            self.name = name.lower()
        else:
            raise TypeError(f"Parameter 'name' has wrong type: {type(name)}. " \
                            "Should be str.")
        
        # Assign measure
        if isinstance(measure, Number):
            if measure > 0:
                self.measure = measure
            else:
                raise ValueError(f"Parameter 'measure' has wrong value: {measure}. " \
                                 "Should be positive.")
        else:
            raise TypeError(f"Parameter 'measure' has wrong type: {type(measure)}. " \
                            "Should be any number type.")
        
        # Assign measurement unit
        if isinstance(unit, str):
            if unit == '':
                self.unit = "pcs."  # If no unit is provided, interpret as countable pieces
            else:
                self.unit = unit.lower()
        else:
            raise TypeError(f"Parameter 'unit' has wrong type: {type(unit)}. " \
                            "Should be str.")
    
    def __str__(self):
        """
        Returns user-oriented representation of this class.
        """
        return f"{self.name}: {self.measure} {self.unit}"
    
    def __repr__(self):
        """
        Returns developer-oriented representation of this class
        """
        return f"{type(self).__name__}(name={self.name}, measure={self.measure}, unit={self.unit})"