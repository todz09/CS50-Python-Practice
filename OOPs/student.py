def main():
    student = get_student()
    if student[0] == "Padma":                               #This won't work when the return value if a tuple (tuple are immutable)
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")
    
def get_student():
    name = input("Name : ")
    house = input("House : ")
    #return (name, house)
    return [name, house]

if __name__ == "__main__":
    main()
    