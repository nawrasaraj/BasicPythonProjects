def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
        return x / y
    
def factorial(x):
    if x == 1: 
        return 1
    else: 
        return x * factorial(x-1)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Factorial")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if num2 == 0.0:
                print (num1, " Cannot be divided on Zero!!")
            else:
                print (num1, "/", num2, "=", divide(num1, num2))

        break
    elif choice == '5':
        num = float(input("Enter a number: "))
        print(num, " factorial is: ", factorial(num))
        break
    else:
        print("Invalid Input")