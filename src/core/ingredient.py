class Ingredient:
    def __init__(self, name: str, measure: float, unit: str):
        self.name = name
        self.measure = measure
        self.unit = unit
        # TODO: Classification into categories (eg. liquids, spices).
    
    def __str__(self):
        return f"{self.measure} {self.unit} of {self.name}"
    
    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', measure={self.measure}, unit={self.unit})"