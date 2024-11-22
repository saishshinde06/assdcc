def input_student_grades():
    students = []
    grades = []
    
    while True:
        name = input("Enter student's name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {name}: "))
        except ValueError:
            print("Invalid input. Please enter a valid grade.")
            continue

        students.append(name)
        grades.append(grade)
    
    return students, grades

# Function to calculate the average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Function to find the highest and lowest grade
def find_highest_lowest(grades, students):
    if len(grades) == 0:
        return None, None
    highest_grade = max(grades)
    lowest_grade = min(grades)
    highest_student = students[grades.index(highest_grade)]
    lowest_student = students[grades.index(lowest_grade)]
    
    return (highest_student, highest_grade), (lowest_student, lowest_grade)

# Function to print the summary of grades
def print_summary(students, grades):
    if len(students) == 0:
        print("No student data available.")
        return
    
    average = calculate_average(grades)
    highest, lowest = find_highest_lowest(grades, students)
    
    print("\nGrade Summary:")
    print(f"Total number of students: {len(students)}")
    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {highest[1]} (Student: {highest[0]})")
    print(f"Lowest grade: {lowest[1]} (Student: {lowest[0]})")
    
    # Display individual grades
    print("\nIndividual Grades:")
    for student, grade in zip(students, grades):
        print(f"{student}: {grade}")

# Main function to execute the project
def main():
    print("Welcome to the Student Grades Analyzer!")
    
    # Input student grades
    students, grades = input_student_grades()
    
    # Generate the summary report
    print_summary(students, grades)

# Run the program
if __name__ == "__main__":
    main()