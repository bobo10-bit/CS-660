# Overall Strength: The code is organized because related data and methods are grouped together in a class and method 
# names make it easy to undersatnd each part of the program.
# Overall Weakness: I have to often move between multiple methods to understand the program which makes it harder to 
# understand the overall flow of the program
class GradeAnalyzer:
    # Strength: The method name makes it easy to understand what it does
    # Strength: Each method only does one task which makes the code easier to read
    def __init__(self, grades):
        self.grades = grades

    def get_count(self):
        return len(self.grades)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        return max(self.grades)

    def get_lowest(self):
        return min(self.grades)

    def get_pass_rate(self):
        passing_count = sum(1 for grade in self.grades if grade >= 70)
        return (passing_count / len(self.grades)) * 100
    
    # New feature: Calculate the median grade
    def get_median(self):
        # Sort the grades to find the middle value(s).
        sorted_grades = sorted(self.grades)
        middle = len(sorted_grades) // 2

        # If there is an even number of grades, average the two middle grades.
        if len(sorted_grades) % 2 == 0:
            return (sorted_grades[middle - 1] + sorted_grades[middle]) / 2
        # If there is an odd number of grades, return the middle grade.
        else:
            return sorted_grades[middle]

    # Strength: This method keeps all the output in one place
    # Weakness: To understand the method requires to look at other methods that it calls
    def print_results(self):
        print("Grade Analysis Results:")
        print(f"Total students: {self.get_count()}")
        print(f"Average grade: {self.get_average():.1f}")
        print(f"Highest grade: {self.get_highest()}")
        print(f"Lowest grade: {self.get_lowest()}")
        print(f"Pass rate: {self.get_pass_rate():.1f}%")
        # New feature: Print the median grade.
        print(f"Median grade: {self.get_median():.1f}")

def analyze_grades():
    # Strength: The main functino is short and easy to follow
    grades = [85, 92, 78, 96, 88, 73, 91, 87, 94, 82]
    analyzer = GradeAnalyzer(grades)
    analyzer.print_results()

if __name__ == "__main__":
    analyze_grades()