def main():
    x = input("Enter a number: ")
    print(f"The square of {x} is {square(x)}")


def square(num):
    return num * num

if __name__ == "__main__":
    main()