students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house": house}
        students.append(student)
        
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse =True):   #Can also use lambda function as -> key = lambda student : student["name"]
    print(f"{student['name']} is living in {student['house']}")