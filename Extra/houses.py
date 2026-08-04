students = [{
    "name": "Alice",
    "house": "Gryffindor"
}, {
    "name": "Bob",
    "house": "Hufflepuff"
}, {
    "name": "Charlie",
    "house": "Ravenclaw"
}, {
    "name": "David",
    "house": "Slytherin"
}]

houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)