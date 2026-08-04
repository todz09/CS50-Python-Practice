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

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)