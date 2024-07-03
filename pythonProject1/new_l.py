import os

# Read the file
with open('grades.csv', 'rt') as file:
    lines = file.readlines()

# Print the lines read from the file
print(lines)

# Initialize lists for students and grades
students = []
grades = []

# Split each line into student name and grade
for line in lines:
    try:
        name, grade = line.strip().split("\t")  # Changed delimiter to tab
        students.append(name)
        grades.append(int(grade))
    except ValueError:
        print(f"Skipping line: {line.strip()}")

# Create a dictionary to map students to their grades
new_dict = dict(zip(students, grades))

# Create an empty dictionary to store the count of each grade letter
grade_counts = {}

# Prepare lines with grade letters
updated_lines = []
for name, grade in new_dict.items():
    if grade >= 40:
        grade_letter = "A"
    elif grade >= 30:
        grade_letter = "B"
    elif grade >= 20:
        grade_letter = "C"
    else:
        grade_letter = "F"

    # Count the occurrences of each grade letter
    if grade_letter in grade_counts:
        grade_counts[grade_letter] += 1
    else:
        grade_counts[grade_letter] = 1

    # Add the grade letter to the line
    updated_lines.append(f"{name}\t{grade}\t{grade_letter}\n")

# Print the grade counts
print(grade_counts)

# Determine a new file path (e.g., the Desktop)
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
new_file_path = os.path.join(desktop_path, 'grades_with_letters.csv')

# Write the modified content to the new file
try:
    with open(new_file_path, 'wt') as file:
        file.writelines(updated_lines)
    print(f"Updated file written to {new_file_path}")
except PermissionError:
    print(f"Permission denied when trying to write to '{new_file_path}'.")
    exit()

# Print the lines with grade letters from the new file
with open(new_file_path, 'rt') as file:
    lines_with_letters = file.readlines()
    for line in lines_with_letters:
        print(line.strip())



