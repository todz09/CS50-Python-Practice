class Student():
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name Missing")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House ")
        self.name = name
        self.house = house
    
    def __str__(self):          # __str__ -> Automatically gets passed 
        return f"{self.name} is from {self.house}"

def main():
    student = get_student()
    print(student)
    
def get_student():
    '''student = Student()
    student.name = input("name ")
    student.house = input("house ")'''
    name = input("Name ")
    house = input("House ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()
    