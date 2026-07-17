numbers = []

'''for i in range(1,6):
    num = float(input(f"Enter Number {i}: "))
    numbers.append(num)'''
    
while len(numbers)<5:
    current_count = len(numbers) + 1
    user_input = input(f"Enter Number {current_count} : ")
    
    try:
        num = float(user_input)
        numbers.append(num)
        
    except ValueError:
        print("Invalid Input, Please enter a Valid Input")
        
highest = max(numbers)
lowest = min(numbers)
average = sum(numbers) / len(numbers)

print("The highest number is : ",highest)
print("The lowest number is : ",lowest)
print("The average of the list is : ",average)