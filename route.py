from typing import List
from city import City

class Route:
    """
    Represents a route between multiple cities.
    """
    def __init__(self, cities: List[City]):
        """
        Initializes a new Route instance.

        :param cities: A list of City instances representing the cities in the route.
        """
        self.cities = cities

    def total_distance(self) -> float:
        """
        Calculates the total distance of the route.

        :return: The total distance of the route.
        """
        distance = sum(self.cities[i].distance(self.cities[i+1]) for i in range(len(self.cities)-1))
        distance += self.cities[-1].distance(self.cities[0])
        return distance

    def fitness(self) -> float:
        """
        Calculates the fitness of the route.

        :return: The fitness of the route.
        """
        return 1 / self.total_distance()

    def __repr__(self):
        return f"Route({self.cities})"
