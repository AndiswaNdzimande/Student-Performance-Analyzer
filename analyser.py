#In here iam defining the structure of how i want the data to look , like which is a dictionary
student_data = [
    {"name": "Andiswa", "surname": "Ndzimande", "grade": "A+"},
    {"name": "Anele", "surname": "Dhludhla","grade": "B"},
    {"name": "Noxolo","surname": "Shabangu", "grade": "A"}
]
# creating an empty list that will store the student's records 
students = []



num_students = int(input("Enter the number of students in your subject: "))

for i in range(num_students):
    name = input("Enter student's name: ")
    surname = input("Enter student's surname: ")
    grade = float(input("Enter student's grade : "))
    
    student_dict = {"name": name,"surname":surname, "grade":(grade) }
    students.append(student_dict)
highest_score = float(max(student_dict["grade"]))
lowest_score = float(min(student_dict["grade"]))
total_marks = float(sum(student_dict["grade"]))
class_average = int(total_marks/ num_students)
    
    
    

print(students)
print(f"This is programming class's : {highest_score}")
print(f"This is programming class's : {lowest_score}")
print(f"This is programming class's : {total_marks}")
print(f"This is programming class's : {class_average}")


