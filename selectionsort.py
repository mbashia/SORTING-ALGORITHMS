def selection_sort(number):
    length = len(numbers)
    for i in range(length - 1):  # index starts at zero to iterate through the whole array
        min_position = i  # set the minimum position
        for j in range(i + 1, length):
            if numbers[j] < numbers[
                min_position]:  # checking all numbers of the array against the number with mean position
                min_position = j
        temp = numbers[i]  # swapping the elements
        numbers[i] = numbers[min_position]
        numbers[min_position] = temp


numbers = [6, 4, 3, 7, 9, 8, 1, 2, ]
selection_sort(numbers)
print(numbers)
