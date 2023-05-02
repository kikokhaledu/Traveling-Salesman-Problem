import math
import random
from typing import List


class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: 'City') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"City({self.x}, {self.y})"


class Route:
    def __init__(self, cities: List[City]):
        self.cities = cities

    def total_distance(self) -> float:
        distance = sum(self.cities[i].distance(self.cities[i+1]) for i in range(len(self.cities)-1))
        distance += self.cities[-1].distance(self.cities[0])
        return distance

    def fitness(self) -> float:
        return 1 / self.total_distance()

    def __repr__(self):
        return f"Route({self.cities})"


def generate_initial_population(size: int, cities: List[City]) -> List[Route]:
    population = []
    for _ in range(size):
        random.shuffle(cities)
        population.append(Route(cities[:]))
    return population


def selection(population: List[Route], elite_size: int) -> List[Route]:
    population.sort(key=lambda route: route.fitness(), reverse=True)
    selected_population = population[:elite_size]

    cumulative_fitness = [route.fitness() for route in population[elite_size:]]
    cumulative_fitness = [sum(cumulative_fitness[:i+1]) for i in range(len(cumulative_fitness))]

    for _ in range(len(population) - elite_size):
        r = random.uniform(0, cumulative_fitness[-1])
        idx = next(i for i, fitness in enumerate(cumulative_fitness) if fitness > r)
        selected_population.append(population[elite_size + idx])

    return selected_population


def crossover(parent1: Route, parent2: Route) -> Route:
    start = random.randint(0, len(parent1.cities)-1)
    end = random.randint(start+1, len(parent1.cities))

    child_cities = parent1.cities[start:end]
    for city in parent2.cities:
        if city not in child_cities:
            child_cities.append(city)

    return Route(child_cities)


def mutation(route: Route, mutation_rate: float) -> Route:
    mutated_cities = route.cities.copy()
    for i in range(len(mutated_cities)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(mutated_cities) - 1)
            mutated_cities[i], mutated_cities[swap_with] = mutated_cities[swap_with], mutated_cities[i]

    return Route(mutated_cities)


def evolution(population: List[Route], elite_size: int, mutation_rate: float) -> List[Route]:
    selected_population = selection(population, elite_size)

    new_population = selected_population[:elite_size]
    for _ in range(len(population) - elite_size):
        parent1, parent2 = random.sample(selected_population, 2)
        child = crossover(parent1, parent2)
        mutated_child = mutation(child, mutation_rate)
        new_population.append(mutated_child)

    return new_population


def genetic_algorithm(cities: List[City], population_size: int, elite_size: int, mutation_rate: float, generations: int) -> Route:
    population = generate_initial_population(population_size, cities)

    for _ in range(generations):
        population = evolution(population, elite_size, mutation_rate)

    best_route = min(population, key=lambda route: route.total_distance())
    return best_route


def prompt_example_input() -> bool:
    return input("Use example input? (y/n): ").strip().lower() == 'y'


def prompt_custom_input() -> tuple:
    while True:
        num_cities = int(input("Enter the number of cities: "))
        if num_cities >= 2:
            break
        print("Please enter at least 2 cities.")

    print("Enter city coordinates as x, y (one city per line):")
    cities = []
    for _ in range(num_cities):
        while True:
            try:
                city_coordinates = input().split(',')
                city_x = float(city_coordinates[0])
                city_y = float(city_coordinates[1])
                cities.append(City(city_x, city_y))
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter city coordinates as x, y:")

    population_size = int(input("Enter the population size: "))
    elite_size = int(input("Enter the elite size: "))
    mutation_rate = float(input("Enter the mutation rate (e.g., 0.01): "))
    generations = int(input("Enter the number of generations: "))
    return cities, population_size, elite_size, mutation_rate, generations


def prompt_try_again() -> bool:
    return input("Do you want to try again? (y/n): ").strip().lower() == 'y'


def main():
    while True:
        use_example_input = prompt_example_input()

        if use_example_input:
            cities = [City(x=60, y=200), City(x=180, y=200),
                      City(x=80, y=180), City(x=140, y=180), City(x=20, y=160),
                      City(x=100, y=160), City(x=200, y=160)]
            population_size = 100
            elite_size = 20
            mutation_rate = 0.01
            generations = 500
        else:
            cities, population_size, elite_size, mutation_rate, generations = prompt_custom_input()

        best_route = genetic_algorithm(cities, population_size, elite_size, mutation_rate, generations)

        print(f"Best route found: {best_route}")
        print(f"Total distance: {best_route.total_distance()}")

        if not prompt_try_again():
            break


if __name__ == "__main__":
    main()


