x = float(input("Enter Number 1 :"))
y = float(input("Enter Number 2 :"))

operator = input("Enter The operation u want to perform : ")

if(operator == "+"):
    z = x + y
elif(operator == "-"):
    z = x - y
elif(operator == "*"):
    z = x * y
elif(operator == "/"):
    z = x / y
elif(operator == "%"):
    z = x % y
else:
    print("Enter a valid operator")
    
print(z)