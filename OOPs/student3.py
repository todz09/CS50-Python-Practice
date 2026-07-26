class Student():
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name Missing")
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House ")
        self.name = name
        self.house = house
    
    def __str__(self):          
        return f"{self.name} is from {self.house}"
    
    @property # Getter -> function or a clas which gets a certain attribute or variable 
    def house(self):
        return self._house 
    
    @house.setter # Setter -> function that sets some value
    def house(self, house):
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    
def main():
    student = get_student()
    student.house = "Number four, Privet Drive"
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
    