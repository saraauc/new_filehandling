letter_range = []
with open("grade_range.txt","r") as f:
    range_lines = f.readlines()
    for line in range_lines:
        low, high, letter = line.strip().split(',')
        letter_range.append((int(low),int(high), letter))
def get_grade_letter(grade):
    for low, high, letter in letter_range:
        if low<=grade<=high:
            return letter
with open("Book2.csv","r") as f:
    modified_lines=[]
    lines=f.readlines()
    for line in lines:
        name,grade=line.strip().split(',')
        grade=int(grade)
        grade_letter=get_grade_letter(grade)
        modified_line=f"{name},{grade},{grade_letter}\n"
        modified_lines.append(modified_line)
with open("Book4.csv","w") as f:
    f.writelines(modified_lines)





