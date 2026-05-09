def insertion_sort(numbers):
    for i in range(len(numbers)):
        element = numbers[i]
        j = i - 1
        while j >= 0 and element < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = element
    return numbers