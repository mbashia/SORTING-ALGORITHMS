# syntax for slicing a list or array is arr[start:end].start is the index of the first element you want to include
# end is the index of the first element you want to exclude
# If you omit start, the slice starts at the beginning of the list.
# If you omit end, the slice goes to the end of the list.
# slicing does not necessary have to occur at the middle
# an array or a list can be sliced into any number of slices
numbers = [7, 45, 6, 4, 37, 7, 6, 9, 0, 2, ]
mid = len(numbers) // 2
left = numbers[:mid]
right = numbers[mid:]
print(left)
print(right)

numbers_2 = numbers[0:3]
print(numbers_2)
numbers_3 = numbers[4:7]
print(numbers_3)
