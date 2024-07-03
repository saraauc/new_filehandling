with open('Book2.csv','rt') as file:
    lines = file.readlines()
    print(lines)
student = []
grades = []
for line in lines:
    name, grade = line.strip().split(",")
    student.append(name)
    grades.append(int(grade))
new_dict=dict(zip(student, grades))
empty_list = {}
print(empty_list)
for value in new_dict.values():
    if value >= 40:
        grade_letter = "A"
    elif value >= 30:
        grade_letter = "B"
    elif value >= 20:
        grade_letter = "C"
    else:
        grade_letter = "F"
    if grade_letter in empty_list:
        empty_list[grade_letter] += 1
    else:
        empty_list[grade_letter] = 1
print(empty_list)

