'''
input_number = 12345
lucky_digit = 6

input_number = 789
lucky_digit = 6

input_number = 257
lucky_digit = 5

Algorithm:
Read the input number say N
    Go on finding sum of the digits of N until N is not Zero
    if 
        the sum is not yet a single digit number, then repeat step1
    else
        print the sum as o/p

input_number = 789
input_number = input_number // 10  # 78
789 % 10   #  9        
'''
# print('Enter a number to find your lucky digit')
# input_number = input()

import pdb
pdb.set_trace()

input_number = int(input('Enter a number to find your lucky digit: '))
print(f'Number you input is {input_number}')

sum_of_digits = 0
while input_number != 0:
    remainder = input_number % 10
    input_number = input_number // 10
    sum_of_digits += remainder
    if sum_of_digits > 9 and input_number == 0:
        input_number = sum_of_digits
        sum_of_digits = 0

print('Your lucky digit is ', sum_of_digits)