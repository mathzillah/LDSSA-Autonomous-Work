"""- A `class` named `Triangle` with two input variables, `base` and `height`, that are attributes of the class. This class should have also a method named `get_area` that calculates and returns the area in the following way: `(base * height) / 2`.    
- A function named `is_equilateral` that accepts three variables as an input. If they have all the same value, return True, otherwise return False.   
- A variable named `description` with the following string value `this is a module named triangle`. """

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return self.base*self.height/2
    
def is_equilateral(side1, side2, side3):
    return side1==side2==side3
    
description = "this is a module named triangle"