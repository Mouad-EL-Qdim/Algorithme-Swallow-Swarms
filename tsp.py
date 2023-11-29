import numpy as np


# Function to calculate the total distance of a given path
def calculate_distance(path , distances):
    distance = 0
    for i in range ( len ( path ) - 1 ):
        distance += distances[path[i]][path[i + 1]]
    return distance


# Function to generate initial random solution
def generate_random_solution(num_cities):
    return np.random.permutation ( num_cities )


# Swallow Swarm Optimization Algorithm
def SSO(distances , num_swallows , num_iterations):
    best_solution = None
    best_distance = float ( 'inf' )
    num_cities = len ( distances )

    # Initialize the swallows
    swallows = [generate_random_solution ( num_cities ) for i in range ( num_swallows )]

    for iteration in range ( num_iterations ):
        for i in range ( num_swallows ):
            for j in range ( num_cities ):
                current_distance = calculate_distance ( swallows[i] , distances )

                # Create a new solution by swapping two cities
                new_solution = np.copy ( swallows[i] )
                new_solution[j] , new_solution[(j + 1) % num_cities] = new_solution[(j + 1) % num_cities] , \
                new_solution[j]

                # Calculate the new distance
                new_distance = calculate_distance ( new_solution , distances )

                # Update the solution if it's better
                if new_distance < current_distance:
                    swallows[i] = new_solution
                    current_distance = new_distance

                # Update the best solution if it's better
                if current_distance < best_distance:
                    best_solution = swallows[i]
                    best_distance = current_distance

    return best_solution , best_distance


# Test the algorithm with a sample problem
distances = [[0 , 2 , 9 , 10] , [1 , 0 , 6 , 4] , [3 , 7 , 0 , 8] , [6 , 6 , 9 , 0]]
num_swallows = 20
num_iterations = 100
best_solution , best_distance = SSO ( distances , num_swallows , num_iterations )

print ( "Best solution: " , best_solution )
print ( "Best distance: " , best_distance )
