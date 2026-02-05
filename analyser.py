full_names =  ["Andiswa Ndzimande", "Anele Dhludhla", "Noxolo Shabangu", "Slindile Mthimunye", "Lerato Tala"]
grade = [90.05 ,79.85,76.8, 80,77.02]
students = []

num_students = int(input("Enter the number of students (1-5): "))
    
for i in range(num_students):
    student_dict = {"full_name": full_names[i], "grade":grade[i]}
  
    students.append(student_dict)
print(student_dict)
    
    
highest_score = float(max(grade[:num_students]))
lowest_score = float(min(grade[:num_students]))
total_marks = float(sum(grade[:num_students]))
class_average = int(total_marks/ num_students)
    
print(students)
print(f"This is programming class's highest_score : {highest_score}")
print(f"This is programming class's lowest_score: {lowest_score}")
print(f"This is programming class's total marks : {total_marks}")
print(f"This is programming class's  average pass mark: {class_average}")


