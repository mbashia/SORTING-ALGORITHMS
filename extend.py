# the extend()is used to add multiple items to a list or a tuple
# it does not form a new list rather it modifies the original list
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)
# you can also use strings and tuples as the arguement in  the method
numbers.extend((6,7,8))
print(numbers)
numbers.extend('victor mbacia')
print(numbers)