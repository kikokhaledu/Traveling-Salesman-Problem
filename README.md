# Traveling Salesman Problem Solver

This Python script solves the Traveling Salesman Problem (TSP) using a Genetic Algorithm. Given a set of cities and the distances between each pair of cities, the script finds the shortest possible route that visits each city exactly once and returns to the starting city.

## Requirements

- Python 3.6 or higher

## How to use

1. Clone or download the repository containing the `tsp.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `tsp.py` script.
4. Run the following command:

```bash
python tsp.py
```
5. Follow the prompts to either use the example input or enter your own custom input.

## Example and example Input usage 

To run the script with the example data, execute the following command:

```bash
python tsp.py
```
When prompted, choose to use the example input by entering `y`. The script will then run the genetic algorithm and output the best route found along with its total distance.

If you choose to use the example input, the script will use the following data:

```python
cities = [City(x=60, y=200), City(x=180, y=200),
City(x=80, y=180), City(x=140, y=180), City(x=20, y=160),
City(x=100, y=160), City(x=200, y=160)]
best_route = genetic_algorithm(cities, population_size=100,
elite_size=20, mutation_rate=0.01, generations=500)
```
## Custom Input
If you choose to enter custom input, you will be prompted to provide the following information:

* The number of cities.
* The coordinates of each city (one city per line, formatted as x, y).
* The population size for the genetic algorithm.
* The elite size (number of top-performing individuals to keep in each generation).
* The mutation rate (e.g., 0.01 for 1% chance of mutation).
* The number of generations for the genetic algorithm to run.

## Output

The script will output the best route found and its total distance.

