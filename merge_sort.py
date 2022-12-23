# merge sort uses divide and conquer and recursion to sort elements in an array
# it divides the elements in to smaller bits
# for instance a list with the following list = [3,2,5,4,] will first be divide into [3,2] and [5,4]
# it will further be divided into [3],[2], [5], [4]
# this elements will then be sorted and merged ie [2,3], [4,5]
# which will later be merged to form the final sorted array ie. [2,3,4,5]

def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)  # recursion
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    left_index = 0
    right_index = 0
    merged = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


numbers = [6, 4, 3, 7, 9, 8, 1, 2, ]
print(merge_sort(numbers))

