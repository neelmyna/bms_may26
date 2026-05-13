arr_a = [2, 3, 4, 5, 1]
i = 5
arr_b = [12, 31, 40, 50, 10]
j = 2

merged_array = [11, 22, 33]
k = 3

# merged_array[k:] = arr_a[i:]
# merged_array[k:] = arr_b[j:]

merged_array[k:] = arr_a[i:] + arr_b[j:]
print(merged_array)

# merged_array[k:] = arr_a[i:] + arr_b[j:]
