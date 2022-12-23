# the method i have used is taking left right and equal list and concatenating  them
def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)-1]
    left = []
    right = []
    equal = []
    for item in a:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            right.append(item)
    return quick_sort(left) + equal + quick_sort(right)


numbers = [9, 8, 7, 5, 4, 3, 8, 6, 4, 3, 2, 9, 0, ]
print(quick_sort(numbers))
