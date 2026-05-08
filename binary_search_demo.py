import sys
import binary_search

input_numbers = []

for i in range(1, len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print(f'User given elements are \n', input_numbers)

search_element = float(input('Enter the element to be searched: '))

search_index = binary_search(search_element, input_numbers)

if search_index == -1:
    print(f'The search element {search_element} was not found in the list')
else:
    print(f'The search element {search_element} was found at position {search_index + 1}')