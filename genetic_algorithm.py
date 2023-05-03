import random
import concurrent.futures
from typing import List, Tuple
from city import City
from route import Route

def generate_initial_population(size: int, cities: List[City]) -> List[Route]:
    """
    Generates an initial population of routes for the genetic algorithm.

    :param size: The size of the population to generate.
    :param cities: A list of City instances to create the routes from.
    :return: A list of Route instances representing the initial population.
    """
    population = []
    for _ in range(size):
        print("cities object passed to generate_initial_population for debugging :",cities)
        random.shuffle(cities)
        population.append(Route(cities[:]))
    return population


def selection(population: List[Route], elite_size: int) -> List[Route]:
    """
    Selects routes from the population based on their fitness.

    :param population: A list of Route instances representing the current population.
    :param elite_size: The number of elite routes to keep without change.
    :return: A list of selected Route instances for the next generation.
    """
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
    """
    Performs crossover between two parent routes to generate a new route.

    :param parent1: A Route instance representing the first parent route.
    :param parent2: A Route instance representing the second parent route.
    :return: A new Route instance generated from the crossover of parent1 and parent2.
    """
    start = random.randint(0, len(parent1.cities)-1)
    end = random.randint(start+1, len(parent1.cities))

    child_cities = parent1.cities[start:end]
    for city in parent2.cities:
        if city not in child_cities:
            child_cities.append(city)

    return Route(child_cities)


def mutation(route: Route, mutation_rate: float) -> Route:
    """
    Applies mutation to the given route based on the mutation rate.

    :param route: A Route instance to apply mutation on.
    :param mutation_rate: The mutation rate (float between 0 and 1).
    :return: A new Route instance with mutations applied.
    """
    mutated_cities = route.cities.copy()
    for i in range(len(mutated_cities)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(mutated_cities) - 1)
            mutated_cities[i], mutated_cities[swap_with] = mutated_cities[swap_with], mutated_cities[i]

    return Route(mutated_cities)


def evolution(population: List[Route], elite_size: int, mutation_rate: float) -> List[Route]:
    """
    Evolves the given population using selection, crossover, and mutation.

    :param population: A list of Route instances representing the current population.
    :param elite_size: The number of elite routes to keep without change.
    :param mutation_rate: The mutation rate (float between 0 and 1).
    :return: A list of Route instances representing the evolved population.
    """
    selected_population = selection(population, elite_size)

    new_population = selected_population[:elite_size]
    for _ in range(len(population) - elite_size):
        parent1, parent2 = random.sample(selected_population, 2)
        child = crossover(parent1, parent2)
        mutated_child = mutation(child, mutation_rate)
        new_population.append(mutated_child)

    return new_population

def selection_and_evolution(population: List[Route], elite_size: int, mutation_rate: float) -> Tuple[List[Route], Route]:
    """
    Performs selection and evolution on the given population.

    :param population: A list of Route instances representing the current population.
    :param elite_size: The number of elite routes to keep without change.
    :param mutation_rate: The mutation rate (float between 0 and 1).
    :return: A tuple with the new population and the best route found in the new population.
    """
    selected_population = selection(population, elite_size)
    new_population = selected_population[:elite_size]
    
    for _ in range(len(population) - elite_size):
        parent1, parent2 = random.sample(selected_population, 2)
        child = crossover(parent1, parent2)
        mutated_child = mutation(child, mutation_rate)
        new_population.append(mutated_child)
    
    best_route = min(new_population, key=lambda route: route.total_distance())
    return new_population, best_route

def adaptive_mutation_rate(generations_without_improvement: int) -> float:
    """
    Adjusts the mutation rate based on the number of generations without improvement.

    :param generations_without_improvement: The number of generations without improvement.
    :return: The adjusted mutation rate.
    """
    if generations_without_improvement < 10:
        return 0.01
    elif generations_without_improvement < 25:
        return 0.05
    else:
        return 0.1
    
def genetic_algorithm(cities: List[City], population_size: int, elite_size: int, mutation_rate: float, generations: int, convergence_limit: int) -> Route:
    """
    Executes the genetic algorithm to find the shortest route between the given cities.

    :param cities: A list of City instances representing the cities.
    :param population_size: The size of the population.
    :param elite_size: The number of elite routes to keep without change.
    :param mutation_rate: The initial mutation rate (float between 0 and 1).
    :param generations: The number of generations to run the algorithm.
    :param convergence_limit: The number of generations without improvement to stop the algorithm.
    :return: The best Route instance found by the genetic algorithm.
    """    
    cities = remove_duplicate_cities(cities)
    population = generate_initial_population(population_size, cities)
    
    best_route = min(population, key=lambda route: route.total_distance())
    generations_without_improvement = 0
    
    for _ in range(generations):
        mutation_rate = adaptive_mutation_rate(generations_without_improvement)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            new_population, new_best_route = executor.submit(selection_and_evolution, population, elite_size, mutation_rate).result()

        if new_best_route.total_distance() < best_route.total_distance():
            best_route = new_best_route
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1
        
        if generations_without_improvement >= convergence_limit:
            break

        population = new_population

    return best_route

def remove_duplicate_cities(cities: List[City]) -> List[City]:
    """
    Removes duplicate cities from the given list of cities.
    :param cities: A list of City instances with possible duplicates.
    :return: A list of unique City instances.
    """
    unique_cities = []
    temp_set = set()

    for city in cities:
        city_tuple = (city.x, city.y)
        if city_tuple not in temp_set:
            temp_set.add(city_tuple)
            unique_cities.append(city)

    return unique_cities
