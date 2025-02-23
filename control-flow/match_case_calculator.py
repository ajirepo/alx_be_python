num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case operation if operation == "addition":
        print("The result is", num1 + num2)
    case operation if operation == "substract":
        print("The result is", num1 - num2)
    case operation if operation == "multiply":
        print("The result is", num1 * num2)
    case operation if operation == "divide":
        print("The result is", num1 / num2)
    case _:
        print("Cannot divide by zero.")
