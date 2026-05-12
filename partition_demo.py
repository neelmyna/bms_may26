import partition as pt
import sys

numbers = []

numbers = [int(value) for value in sys.argv[1:] ]

print('Numbers before Partition: \n', numbers)
pt.partition_array(numbers)
print('Numbers after Partition: \n', numbers)
