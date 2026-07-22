import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)           # .reader -> is a csv built in function to read what's in the csv file
                                        # .DictReader -> can use this for better and larger data when the name of the columns are specified in the csv
    for name, home in reader:
        students.append({"name": name, "home": home})
        
for student in sorted(students, key = lambda student : student ["name"]):
    print(f"{student['name']} is living in {student['home']}")