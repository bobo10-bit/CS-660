# Part 1: Invaliud Inputs
# Function to count down from n to 1

print("Part 1: Invalid Inputs")
def count(n):
    # Catches type errors
    try:
        # If the input is not a number then raise a TypeError
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")

        # Once it hits 0 it stops the recursion
        if n == 0:
            return

        # Print the number and call a recursion that subtracts 1 from n
        print(n)
        count(n - 1)

    # If there is an error then print the error message
    except TypeError as e:
        print("Input must be a number" + "\n")

#Valid input
count(5)
# Invalid input
count("hello")

# Part 2: Nested or structured data
# Function to process nested data
print("Part 2: Nested or Structured Data")
def process(data):
    # Catches type errors
    try:
        # Loops through each item in the data
        for item in data:
            # Checks if the item is a list 
            if isinstance(item, list):
                # If it is a list then recursivly call the function again
                process(item)
            else:
                # If its not a list then print the item
                print(item)

    # Prints an error message if the data is not iterable
    except TypeError:
        print("Invalid data \n")

# Valid data
data = [1, [2, [3, 4]], 5]
process(data)

#Invalid data
process(10)

# Part 3: Data Structures and Output
# Function to find the innermost leaf data
print("Part 3: Data Structures and Output")
def find_leaf(data):
    # For each item in the data check if it is a list or not
    for item in data:
        # checks if the item is a list 
        if isinstance(item, list):
            # Recursively call the function again if it is a list
            find_leaf(item)
        else:
            # Assume that the item is the deepest leaf data
            deepest = True
            # Check if there is any more nested loops
            for x in data:
                # If there are more nested loops then set deepest to False
                if isinstance(x, list):
                    deepest = False

            # If there is no more nested loops then print the item
            if deepest:
                print(item)

# Example usage
data = [[1, [2, [3, 4]]], 5]
find_leaf(data)

import json

# Load the catalog dataset
with open(r"C:\Users\eleme\Downloads\catalog.json", "r") as file:
    data = json.load(file)

# Part 4: Manipulating Dataset
# Uses a lambda function to double the mass of a galaxy
print("Part 4: Manipulating Dataset")

# Select the galaxies data from the astronomical catalog
galaxies = data["astronomical_catalog"]["galaxies"]

# Double the mass of each galaxy using a lambda function
doubled_masses = list(map(lambda galaxy: galaxy["mass_solar_masses"] * 2, galaxies))

# Print the original and doubled mass
for galaxy, doubled_mass in zip(galaxies, doubled_masses):
    print("Original mass:", galaxy["mass_solar_masses"])
    print("Doubled mass:", doubled_mass)
print("\n")

# Part 5: Higher-Order Function
print("Part 5: Higher-Order Function")

# Select the galaxies data
galaxies = data["astronomical_catalog"]["galaxies"]

# Function that accepts another function
def process_galaxies(galaxies, function):
    for galaxy in galaxies:
        print(function(galaxy))

# Function to get the galaxy name
def get_name(galaxy):
    return galaxy["name"]

# Process the dataset
process_galaxies(galaxies, get_name)

print("\n")

# Part 6: Function as an Argument
print("Part 6: Function as an Argument")

# Function that accepts another function
def process_galaxy(galaxy, function):
    return function(galaxy)

# Function that gets the galaxy name
def get_name(galaxy):
    return galaxy["name"]

# Use get_name as an argument
for galaxy in galaxies:
    print(process_galaxy(galaxy, get_name))
