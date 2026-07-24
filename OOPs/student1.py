class Student():
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name Missing")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House ")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    '''student = Student()
    student.name = input("name ")
    student.house = input("house ")'''
    name = input("Name ")
    house = input("House ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()
    