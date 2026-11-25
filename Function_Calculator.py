try:
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))
except ValueError:
    print("Invalid number!")
add = x + y
subtract = x-y
multiply = x*y
divide = x/y
user = add or subtract or multiply or divide
if user == add:
    print(x+y)

elif user == subtract:
    print(x-y)

elif user == multiply:
    print(x*y)

elif user == divide:
    print(x/y)

else:
    print("Invalid!")
try:
    x = 0
    x / y
except ZeroDivisionError:
    ("0 is not possible!")