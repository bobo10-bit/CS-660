# Overall strength: Easy to follow because the program executes ina  clear step by step order. 
# Overall weakness: As you expand the function by adding more features it can make it more cluttered and harder to read

def analyze_grades():
    # Strength: The list of grades is clearely defined
    grades = [85, 92, 78, 96, 88, 73, 91, 87, 94, 82]

    # Strength: the varables clearly define their purpose
    total = 0
    count = 0
    highest = grades[0]
    lowest = grades[0]
    passing_count = 0
    # New Feature: Variable to hold the median value
    median = 0

    # Strength: Simple loop makes the control flow easy to follow
    for grade in grades:
        total += grade
        count += 1
        
        if grade > highest:
            highest = grade
        
        if grade < lowest:
            lowest = grade
            
        if grade >= 70:
            passing_count += 1

    average = total / count
    pass_rate = (passing_count / count) * 100

    # New feature: Find the median grade
    # Sort the grades from low to high
    sorted_grades = sorted(grades)
    # Find the middle grade
    middle = count // 2

    # If there is a odd number of grades the middle grade is the median
    # If there is a even number then the median is the two grades divided by two
    if count % 2 == 0:
        median = (sorted_grades[middle - 1] + sorted_grades[middle]) / 2
    else:
        median = sorted_grades[middle]
    

    # Strength: easy to understand print results
    print("Grade Analysis Results:")
    print(f"Total students: {count}")
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
    print(f"Pass rate: {pass_rate:.1f}%")
    # New Feature: Print the median
    print(f"Median grade: {median:.1f}")


if __name__ == "__main__":
    analyze_grades()