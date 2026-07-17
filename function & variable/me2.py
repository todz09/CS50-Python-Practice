def get_passing_students(student_list):
    
    '''passed_students = [student.get("name","Unknown") for student in student_list if student.get("marks",0) >= 40]'''
    passed_students = [student["name"] for student in student_list if "marks" in student and "name" in student and student["marks"] >= 40]

    
    '''for student in student_list:
        if student["marks"] >= 40:
            passed_students.append(student["name"])'''
    
    return passed_students

student = [
    {"name": "John", "marks": 58},
    {"name": "Hail", "score": 48},
    {"name": "Alwin", "marks": 38},
    {"name": "Price", "marks": 39}
]

passed = get_passing_students(student)
print("Passed Students : ", passed)