from city import City
from genetic_algorithm import genetic_algorithm
from input_prompts import (prompt_example_input, prompt_custom_input, prompt_try_again)

def main():
    """
    The main function that runs the program.
    """
    while True:
        use_example_input = prompt_example_input()

        if use_example_input:
            # this is the example function provided in the task for a quick test
            cities = [City(x=60, y=200), City(x=180, y=200),
                      City(x=80, y=180), City(x=140, y=180), City(x=20, y=160),
                      City(x=100, y=160), City(x=200, y=160)]
            population_size = 100
            elite_size = 20
            mutation_rate = 0.01
            generations = 500
            convergence_limit = 50
            best_route = genetic_algorithm(cities, population_size, elite_size, mutation_rate, generations, convergence_limit)

        else:
            cities, population_size, elite_size, mutation_rate, generations, convergence_limit = prompt_custom_input()
            best_route = genetic_algorithm(cities, population_size, elite_size, mutation_rate, generations, convergence_limit)




        print(f"Best route found: {best_route}")
        print(f"Total distance: {best_route.total_distance()}")

        if not prompt_try_again():
            break


if __name__ == "__main__":
    main()
