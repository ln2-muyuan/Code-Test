import os

print(os.getcwd())
print(os.path.exists(os.getcwd() + '/test.py'))

numbers = [1, 2, 3, 4, 5]
square = lambda x: x * x
print(list(map(square, numbers)))

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
upper = lambda x: x.upper()
print(list(map(upper, names)))


numbers = [1, 2, 3, 4, 5]
is_odd = lambda x: x % 2 != 0
print(list(filter(is_odd, numbers)))