import sys

def find_factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * find_factorial(number-1)

input_number = int(sys.argv[1])

factorial_number = find_factorial(input_number)
print(f'Factorial of {input_number} is {factorial_number}')
