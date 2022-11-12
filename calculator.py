print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

math_operator = input('Hello user, please select the Mathematics Operator you would like to use, (ie: +,-,*,/) or Type \'temp\' for Celsius to Farenheit conversion: ')

if math_operator == '+':
    num_1 = input('Enter first number: ')
    num_2 = input('Enter Second number: ')
    print(f'The Sum of {num_1} + {num_2} = {int(num_1) + int(num_2)}')
elif math_operator == '-':
    num_1 = input('Enter first number: ')
    num_2 = input('Enter Second number: ')
    print(f'The Subtraction of {num_1} - {num_2} = {int(num_1) - int(num_2)}')
elif math_operator == '*':
    num_1 = input('Enter first number: ')
    num_2 = input('Enter Second number: ')
    print(f'The Multiplication of {num_1} * {num_2} = {int(num_1) * int(num_2)}')
elif math_operator == '/':
    num_1 = input('Enter first number: ')
    num_2 = input('Enter Second number: ')
    print(f'The Multiplication of {num_1} * {num_2} = {int(num_1) / int(num_2)}')
elif math_operator.lower() == 'temp':
    num_1 = input('Enter the Temperature in Celsius for conversion: ')
    print(f'The Temperature of {num_1}°C in Farenheit = {int(num_1) * 9/5 + 32}°F')
else:
    print('Sorry the Math Operator you have entered is invalid, please select an operator within this list [+,-,*,/] or type\'temp\' for Celsius to Farenheit conversion.' )
