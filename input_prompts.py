from typing import List, Callable
from city import City
from genetic_algorithm import remove_duplicate_cities

def prompt_example_input() -> bool:
    """
    Prompts the user to use the example input or not.

    :return: A boolean value indicating whether the user wants to use the example input or not.
    """
    return input("Use example input? (y/n): ").strip().lower() == 'y'



def prompt_int(message: str, condition: Callable[[int], bool], error_message: str) -> int:
    """
    Prompts the user for custom input values for the genetic algorithm.

    :return: A tuple containing the cities, population_size, elite_size, mutation_rate, generations, and convergence_limit.
    """
    while True:
        try:
            value = int(input(message))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def prompt_float(message: str, condition: Callable[[float], bool], error_message: str) -> float:
    """
    Prompts the user for a float input value, with a custom validation function and error message.

    :param message: The message to display when prompting for the float value.
    :param condition: A function to validate the user's input.
    :param error_message: The error message to display if the input is invalid.
    :return: The user's input for the float value.
    """
    while True:
        try:
            value = float(input(message))
            if condition(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter a float value.")

def prompt_cities(num_cities: int) -> List[City]:
    """
    Prompts the user for city coordinates and creates a list of City objects.

    :param num_cities: The number of cities the user wants to enter.
    :return: A list of City objects created from the user's input.
    """
    while True:
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

        print(f"Cities before removing duplicates: {cities}")
        cities = remove_duplicate_cities(cities)
        print(f"Cities after removing duplicates: {cities}")
        
        if len(cities) < 2:
            print("Duplicate cities have been removed.")
            print("Please enter at least 2 unique cities.")
        else:
            break
    return cities



def prompt_convergence_limit(prompt_message, validation_function, error_message, default=50):
    """
    Prompts the user for the convergence limit, with an optional default value.

    :param prompt_message: The message to display when prompting for the convergence limit.
    :param validation_function: A function to validate the user's input.
    :param error_message: The error message to display if the input is invalid.
    :param default: The default value for the convergence limit (optional).
    :return: The user's input for the convergence limit, or the default value if left empty.
    """
    while True:
        user_input = input(f"{prompt_message} (or leave it empty to use the default value {default}): ")
        if user_input == "":
            return default
        try:
            value = int(user_input)
            if validation_function(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter an integer value.")



def prompt_custom_input() -> tuple:
    """
    Prompts the user for custom input values for the genetic algorithm.

    :return: A tuple containing the cities, population_size, elite_size, mutation_rate, generations, and convergence_limit.
    """
    num_cities = prompt_int("Enter the number of cities: ", lambda x: x >= 2, "Please enter at least 2 cities.")
    cities = prompt_cities(num_cities)

    cities = remove_duplicate_cities(cities)
    while len(cities) < 2:
        print("Please enter at least 2 unique cities.")
        cities = prompt_cities(num_cities)
        cities = remove_duplicate_cities(cities)

    population_size = prompt_int("Enter the population size: ", lambda x: x > 0, "Please enter a positive population size.")
    elite_size = prompt_int("Enter the elite size: ", lambda x: 0 < x < population_size or (population_size == 1 and x == 1), "Please enter an elite size greater than 0 and less than the population size.")
    mutation_rate = prompt_float("Enter the mutation rate (e.g., 0.01): ", lambda x: 0 <= x <= 1, "Please enter a mutation rate between 0 and 1.")
    generations = prompt_int("Enter the number of generations: ", lambda x: x > 0, "Please enter a positive number of generations.")
    convergence_limit = prompt_convergence_limit("Enter the convergence limit", lambda x: x > 0, "Please enter a positive convergence limit.")
    return cities, population_size, elite_size, mutation_rate, generations ,convergence_limit




def prompt_try_again() -> bool:
    """
    Prompts the user to check if they want to try the algorithm again.

    :return: A boolean value indicating whether the user wants to try again or not.
    """
    return input("Do you want to try again? (y/n): ").strip().lower() == 'y'