'''
Read size of the list from user, say N
Read N number of elements of the list
Read the search element from the user
Ask the function sequentially_search() to do the job!
The function will return the index of 1st occurance of the element, else -1
'''
def sequentially_search(search_element, elements):
    for i in range(len(elements)):
        if elements[i] == search_element:
            return i
    return -1

input_size = int(input('Enter size of the list: '))

elements = []  # elements = list()

print(f'Enter the {input_size} elements of the list')
for i in range(input_size):
    element = float(input())
    elements.append(element)

print('User given elements are \n', elements)
search_element = float(input('Enter the element to be searched: '))

search_index = sequentially_search(search_element, elements)

if search_index == -1:
    print(f'The search element {search_element} was not found in the list')
else:
    print(f'The search element {search_element} was found at position {search_index + 1}')