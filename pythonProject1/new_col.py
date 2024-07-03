with open("Book2.csv","r") as f:
    modified_lines=[]
    lines=f.readlines()
    for line in lines:
        name, grade = line.strip().split(',')
        grade = int(grade)
        if grade >= 40:
            grade_letter="A"
        elif grade >= 30:
            grade_letter="B"
        elif grade >= 20:
            grade_letter="C"
        else:
            grade_letter="F"
        modified_line = f"{name},{grade},{grade_letter}\n"
        modified_lines.append(modified_line)
with open("Book3.csv","wt") as file:
    file.writelines(modified_lines)







