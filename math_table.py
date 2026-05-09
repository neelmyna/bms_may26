import sys

user_number = int(sys.argv[1])

for i in range(1, 21):
    # print(f'{user_number} * {i} = {user_number * i}')
    print('%d * %02d = %03d'%(user_number, i, user_number * i))