"""
Name: Parker J
Date: 2/24/2025
Assignment: Homework 6- Python Introduction
Description: The user will enter 2 numbers and the line of code will then add, subtract, multiply and divide all the inputed numbers
"""
# lets the user put in the required numbers
x = input("Put in a number")
y = input("Put in another number")

# shows the x value and the y value
print(f'x = {x}')
print(f'y = {y}')

# setting up the sum, difference, product and dividend for the equations
sum = int(x) + int(y)
diff = int(x) - int(y)
prod = int(x) * int(y)
div = int(x) / int(y)

# allows the code to both show the x and y value being put together, while also showing the symbols in the equation
print(f'{x} + {y} = {sum}')
print(f'{x} - {y} = {diff}')
print(f'{x} * {y} = {prod}')
print(f'{x} / {y} = {div}')