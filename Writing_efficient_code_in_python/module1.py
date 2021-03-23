# The Zen of Python by Tim Peters
import this

help(enumerate)

# Enumerate can help start with different index by using 'start'
arr1 = [4, 7, 9, 3, 4]
for idx, i in enumerate(arr1, start=5):
    print(idx, i)

# Map applies a fuction to each element
# Map provides a clean and efficient way to apply a function
# to an object iteratively without writing a for loop.
list(map(lambda x: x+10, arr1))

# * can be used with range to unpack an object within a list
[*range(0, 11)]
[1, 2, *range(3, 15), 15]
arr2 = ['dick', 'harry', 'norman']
[*enumerate(arr2, start=1)]

# Capitalize and print arr2
# Use map to apply lambda function to arr2
# Use * to unpack map object in a list
[*map(lambda x:str.upper(x), arr2)]
