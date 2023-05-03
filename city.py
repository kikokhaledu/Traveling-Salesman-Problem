import math

class City:
    """
    Represents a city with x and y coordinates.
    """
    def __init__(self, x: float, y: float):
        """
        Initializes a new City instance.

        :param x: The x coordinate of the city.
        :param y: The y coordinate of the city.
        """
        self.x = x
        self.y = y

    def distance(self, other: 'City') -> float:
        """
        Calculates the Euclidean distance between this city and another city.

        :param other: Another City instance to calculate the distance from.
        :return: The Euclidean distance between the two cities.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):

        return f"City({self.x}, {self.y})"
