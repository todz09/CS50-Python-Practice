class Student():
    def __init__(self, name, house, petronus):
        if not name:
            raise ValueError("Name Missing")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House ")
        self.name = name
        self.house = house
        self.petronus = petronus
    
    def __str__(self):          # __str__ -> Automatically gets passed 
        return f"{self.name} is from {self.house}"
    
    def charm(self):
        match self.petronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _ :
                return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum! ")
    print(student.charm())
    
def get_student():
    '''student = Student()
    student.name = input("name ")
    student.house = input("house ")'''
    name = input("Name ")
    house = input("House ")
    petronus = input("Peetronus: ")
    return Student(name, house,petronus)
    

if __name__ == "__main__":
    main()
    