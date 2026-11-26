
# ================================
# FUNCTION CALCULATOR
# ================================

# ---------- PART 1: four functions ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# ---------- MAIN PROGRAM ----------
print("FUNCTION CALCULATOR")

# ---------- PART 2, 3 and 4 ----------

try:
    # Ask for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask for operation
    operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

    # Perform calculation
    if operation == "add":
        print("Result:", add(num1, num2))

    elif operation == "subtract":
        print("Result:", subtract(num1, num2))

    elif operation == "multiply":
        print("Result:", multiply(num1, num2))

    elif operation == "divide":
        print("Result:", divide(num1, num2))

    else:
        print("Unknown operation.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Thank you for using the Function Calculator!")
