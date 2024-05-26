def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error division by zero."
    else:
        return x / y
print("Welcome to Calculator")
print("Operations are:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    try:
        choice = int(input("Enter your choice (between 1 to 4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice please enter a valid operation.")
            continue
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        break
    except ValueError:
        print("Invalid input please enter numbers only.")