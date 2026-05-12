import quick_sort as qs
import sys

# numbers = [71, 50, 25, 23, 22, 19, 19, 18, 17, 15, 3, 1]
# numbers = [int(value) for value in sys.argv[1:] ]

numbers = [1, 50, 23, 25, 52, 19, 19, 91, 7, 15, 43, 71]
print('Numbers before Sort: \n', numbers)
qs.quick_sort(numbers, 0, len(numbers)-1)
print('Numbers after Sort: \n', numbers)

