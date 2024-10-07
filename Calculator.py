# this function adds 2 numbers.
def add(x,y):
    return x + y

# Subtracting 2 numbers
def sub(x,y):
    return x - y

# Multiplying 2 numbers.
def multiply(x,y):
    return x * y

#division
def division(x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.subtraction")
print("3.Multiplication")
print("4.division")

while True:
    #take input from user
    choice = input("Enter choice from 1 - 4:")
    #check if option is there
    if choice in ('1', '2', '3', '4'):
        try:
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, division(num1, num2))
        
        #check if user wants to do another calculation
        #break the loop if no
        next_calculation = input("Do you want to do another calculation? (yes/no) : ")
        break
    else:
        print("Invalid input!")
