def partition_array(numbers, low, high):
    pivot = numbers[high] # assign last element of the partitioned array as reference element
    i = low   # to access each element of the list
    j = low # to know/find the index of the pivot element

    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[high], numbers[j] = numbers[j], numbers[high]
    return j

