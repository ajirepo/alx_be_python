def safe_divide(numerator, denominator):
    try:
       result = float(numerator)/float(denominator)
       return f"The result of the division is {result}"
    except ZeroDivisionError as Exception:
        return ("Error: Cannot divide by zero.")
    except ValueError as Exception:
        return ("Error: Please enter numeric values only.")
