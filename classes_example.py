# Classes Example
# Create some classes and objects
import math
class Shape():
    '''Represents a 2-dimensional polygan

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length

    '''
    def __init__(self):
        '''Creates a new shape with default value'''
        self.num_sides = 4
        self.side_length = 10.0
    def area(self) -> float:
        '''Return the area of a square'''
        return self.side_length ** 2
    def perimter(self) -> float:
        # TODO:
        return self.side_length * self.num_sides
class Circle(Shape):
    '''Represents a circle which IS A shape.
    Attributes:
        radius: A float indicating the radius
    '''
    def __init__(self, radius: float = 5):
        '''Creates a circle with default
        '''
        # Call the superclass constructor
        super().__init__()

        self.radius = radius
        self.num_sides = 1
    def area(self) -> float:
        '''Returns the area of the circle'''
        return math.pi * (self.radius ** 2)
    def perimter(self) -> float:
        '''Return the perimeter of the circle,'''
        return str(round(2 * math.pi * self.radius, 2)) + "cm"
some_shape = Circle(4)
print(some_shape.perimter())
