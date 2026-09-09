# Overall Strength: Each function only performs one task, so it is easy to understand what each part of the program is 
# responsible for.
# Overall weakness: Hard to understand how exactly each function is performing its calculation such as how this function 
# calculates averages or how this function finds the max
from functools import reduce, partial

# Weakness: The Lambda functions are harder to understand
calculate_count = len
calculate_sum = sum
calculate_average = lambda grades: sum(grades) / len(grades)
find_maximum = lambda grades: reduce(max, grades)
find_minimum = lambda grades: reduce(min, grades)
# New feature: Calculate the median grade
calculate_median = lambda grades: (
    # Sorts the grade then finds the middle value
    (sorted(grades)[len(grades) // 2 - 1] + sorted(grades)[len(grades) // 2]) / 2
    # If the grades are even find the average middle two grades
    if len(grades) % 2 == 0
    # Otherwise return the middle grade
    else sorted(grades)[len(grades) // 2]
)

is_passing = lambda grade: grade >= 70
count_passing = lambda grades: len(list(filter(is_passing, grades)))
calculate_pass_rate = lambda grades: (count_passing(grades) / len(grades)) * 100

def create_analysis_functions():
    # Strength: breaking the calculations into seperate calculations make the code easier to follow
    return [
        lambda grades: f"Total students: {calculate_count(grades)}",
        lambda grades: f"Average grade: {calculate_average(grades):.1f}",
        lambda grades: f"Highest grade: {find_maximum(grades)}",
        lambda grades: f"Lowest grade: {find_minimum(grades)}",
        lambda grades: f"Pass rate: {calculate_pass_rate(grades):.1f}%",
        # New feature: Display the median grade
        lambda grades: f"Median grade: {calculate_median(grades):.1f}"
    ]

def generate_report(grades):
    analysis_functions = create_analysis_functions()
    # Weakness: Using Lambda and map functions make it harder to understand compared to a simple loop
    return list(map(lambda func: func(grades), analysis_functions))

def print_report(report_lines):
    print("Grade Analysis Results:")
    # Weakness: Using a for loop would be easier to understand
    list(map(print, report_lines))

def analyze_grades():
    # Strength: The main function is short and shows the program flow
    grades = [85, 92, 78, 96, 88, 73, 91, 87, 94, 82]
    report = generate_report(grades)
    print_report(report)

if __name__ == "__main__":
    analyze_grades()