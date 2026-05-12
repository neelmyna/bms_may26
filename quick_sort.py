import partition as pt

def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = pt.partition_array(numbers, low, high)
        print(numbers)
        quick_sort(numbers, low, pivot_index-1)
        quick_sort(numbers, pivot_index+1, high)

