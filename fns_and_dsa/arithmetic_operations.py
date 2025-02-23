def perform_operation(num1, num2, operation):
    operation = "add,subtract,multiply"
    if operation == "add":
        return num1+num2
    elif operation == "substract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif num2 == 0:
       print("Cannot divide by zero.")
