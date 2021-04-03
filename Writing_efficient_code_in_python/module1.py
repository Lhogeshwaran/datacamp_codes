##
# zip, map, using * for extraction into a list, %timeit for single line
# %%timeit for timing multiple lines of code
# memory and efficiency profiling
# itertools
# Avoiding loops efficiently by using map and zip
# Pandas
# iterrows(), itertuples(), apply()


# The Zen of Python by Tim Peters
import this

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
arr2 = ['dick', 'harry', 'norman', 'bill', 'jack']
[*enumerate(arr2, start=1)]

# Capitalize and print arr2
# Use map to apply lambda function to arr2
# Use * to unpack map object in a list
[*map(lambda x:str.upper(x), arr2)]

# For timing the code
%timeit ls = [*range(1, 1000000)]
# Flags -r -n -o
%timeit -r5 -n20 ls = [*range(1, 1000000)]

# Use double % for running more than one line of code.
%%timeit
ls1 = []
for i in range(1, 1000000):
    ls1.append(i)

%timeit [s*3 for s in arr1]
%timeit [*map(lambda s : s*3, arr1)]

# Profiling
# Time
%load_ext line_profiler
%lprun -f funcname funcname(parameters)

# Memory
from hero_funcs import convert_units
%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes, hts, wts)

from collections import Counter
arr3 = ['Grass', 'Dark', 'Fire', 'Water', 'Legendary', 'Grass', 'Grass', 'Grass', 'Grass', 'Grass', 'Grass'
        , 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Legendary', 'Legendary', 'Fire', 'Water'
        , 'Fire', 'Water', 'Fire', 'Water', 'Fire', 'Water']
Counter(arr3)

from itertools import combinations
[*combinations(set(arr3), 2)]

# Set theory
# Intersection, difference, symmetric_difference, union

arr4 = [2, 4, 7, 4, 8, 1, 8, 3, 10]

%%timeit
tmp = 0
for i in arr4:
    tmp += i
print(tmp)

%timeit sum(arr4)

# Function within function

def capitalize_int(func):

    def inner(s):
        return func(s.capitalize())
    
    return inner

def reverse_string(s):

    return s[::-1]

s = 'loki'
reverse_string = capitalize_int(reverse_string)
reverse_string(s)

s.capitalize()
