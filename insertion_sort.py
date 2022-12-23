#  divides the list into two parts that is unsorted and sorted parts
#  we go through the unsorted part picking values and placing them in the sorted part in the right order
# this means some values in the sorted part will have to be shifted to right or left as we insert values from
# the unsorted part


def insertion_sort(numbers):
    for i in range(1, len(numbers)):  # iterate through all unsorted elements of array
        j = i  # inner while loop starts at the index of the outer loop and checks the list to the left if we need to #
        # swap
        while numbers[j - 1] > numbers[j] and j > 0:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            j -= 1


numbers = [6, 4, 3, 7, 9, 8, 1, 2, 4, 5, 7, 8, 9, 6, 3]
insertion_sort(numbers)
print(numbers)
