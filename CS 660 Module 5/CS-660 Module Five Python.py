numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Imperative
print("Imperative Approach:")
# Create a empty list for the odd squared numbers
squaredList = []
# Loop trought each number is the number list
for n in numberList:
    # If the number is odd, square it and append it to the squared list
    if n % 2 != 0:
        squaredList.append(n ** 2)
# Print the squared list
print(squaredList)

# Object-Oriented
print("\nObject-Oriented Approach:")
class NumberProcessor:
    # Initialize the class with a list of numbers
    def __init__(self, numbers):
        self.numbers = numbers

    # Method to get the odd squared numbers and returns sqaures odd numbers
    def get_odd_squared(self):
        squaredList = [n ** 2 for n in self.numbers if n % 2 != 0]
        return squaredList

# Create an instance of the NumberProcessor class with the number list
processor = NumberProcessor(numberList)
# Call the get_odd_squared method and print the result
print(processor.get_odd_squared())

# Functional
print("\nFunctional Approach:")
# Uses lambda functions to filter out even numbers, then maps the remaining odd numbers to their squared values.
squared_odds = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numberList)))
# Prints the results
print(squared_odds)