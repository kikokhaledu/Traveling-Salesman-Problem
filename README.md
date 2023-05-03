# Traveling Salesman Problem Solver
This application uses a genetic algorithm to solve the Traveling Salesman Problem (TSP). The Traveling Salesman Problem is an optimization problem where the goal is to find the shortest route that visits a set of cities and returns to the starting city.
## Features
* Command-line interface for user input
* Customizable parameters for the genetic algorithm
* Input validation and error handling
* Example input for quick testing
* Multi-threaded processing for improved performance
* Modular design for easy code maintenance

## Input Validation
The application validates user input in various ways:

* Number of cities must be greater than or equal to 2 also handles duplicate cities and the edge case where you enter 2 cities only and they are duplicate.
* Population size must be positive.
* Elite size must be greater than 0 and less than the population size.
* Mutation rate must be between 0 and 1 (inclusive).
* Number of generations must be positive.
* Convergence limit must be positive.
* City coordinates must be valid float values.

If the user provides invalid input, an appropriate error message is displayed, and the user is prompted to enter the correct value.

## Inputs
The application prompts the user for the following inputs:
1. Whether to use the example input or provide custom input.
2. If custom input is chosen:
* The number of cities to visit.
* Coordinates for each city (one per line) in the format `x`, `y`.
* The size of the population.
* The elite size (number of top solutions to keep from one generation to the next).
* The mutation rate (probability of swapping cities in a route).
* The number of generations to run the algorithm for.
* The convergence limit (number of generations without improvement before the algorithm stops).
## Outputs
Once the genetic algorithm finishes running, the application displays:
* The best route found.
* The total distance of the best route.

## How the Application Works

1. The user provides input for cities and algorithm parameters.
2. The algorithm generates an initial population of routes.
3. The algorithm iterates through the specified number of generations, performing the following steps:
* Selects the fittest routes based on their fitness scores.
* Performs crossover (combines routes to create new routes) and mutation (randomly swaps cities within a route) to create a new population.
* Checks for convergence (no improvement in the best route after a certain number of generations).

4. The application displays the best route and its total distance.

To run the application, simply execute the main.py script.

```bash
python main.py
```
Follow the prompts to provide input for cities and algorithm parameters. Once the algorithm completes, the best route and its total distance will be displayed.