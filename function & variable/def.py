'''def hello(to = "World"):
    print("Hello", to)

hello()
name = input("Enter Name : ")
hello(name)'''


def main():
    name = input("Enter Name : ")
    hello(name)
    
def hello(to = "World"):
    print("Hello, ", to)
    
main()