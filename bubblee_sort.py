# compares two numbers at a time. if one number is greater than the other, the two numbers are swapped in the
# first parse.the parses are repeated until the list is sorted


def bubble_sort(number):
    for i in range(len(number)):
        swapped = True
        for j in range(len(number) - 1):
            if number[j] > number[j + 1]:  # swapping the two numbers
                swapped = True
                temp = number[j]
                number[j] = number[j + 1]
                number[j + 1] = temp
        if not swapped:
            break


numbers = [6, 4, 3, 7, 9, 8, 1, 2, ]
bubble_sort(numbers)
print(numbers)
# code can be improved by figuring out a way which we wont loop through already sorted elements of the list
