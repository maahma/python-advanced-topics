# Map Questions
# 1. Use `map()` to convert a list of strings to uppercase.
string_list = ["apple", "banana", "mango"]
upper = list(map(lambda x: x.upper(), string_list))
print(upper)

# 2. Given a list of numbers, use `map()` to return their cube values.
num_list = [1, 2, 3, 4]
cube = list(map(lambda x: x*x*x, num_list))
print(cube)

# 3. Use `map()` to add corresponding elements from two lists: `[1, 2, 3]` and `[4, 5, 6]`.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
add = list(map(lambda x, y: x + y, list_1, list_2))
print(add)

# 4. Given a list of full names, use `map()` to extract only the first names.
full_names = ["Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Evans"]
first_name = list(map(lambda x: x.split()[0], full_names))
print(first_name)

# Filter Questions
# 1. Use `filter()` to find all numbers divisible by 3 from a list.
num = [2,3,4,5,6,9,11,21,32,33,43,26,81,90]
div = list(filter(lambda x: x%3==0, num))
print(div)

# 2. Given a list of strings, filter out all empty strings.
s_list = ["strawberry", "", "apple", "mango", "", "", "banana"]
fruits = list(filter(lambda x: x != "", s_list)) 
print(fruits)

# 3. Use `filter()` to remove negative numbers from a list.
num = [2,3,-4,5,-6,9,11,-21,32,33,-43,26,-81,-90]
pos_nums = list(filter(lambda x: x > 0, num))
print(pos_nums)

# 4. Given a list of words, use filter() to return only words that start with a vowel.
words = ["apple", "banana", "orange", "grape", "umbrella", "strawberry", "elephant", "kiwi"]
vowel = list(filter(lambda x: x[0] in "aeiou", words))
print(vowel)

# Reduce Questions
# 1. Use `reduce()` to compute the sum of a list of numbers.
from functools import reduce
numbers = [5, 10, 15, 20]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)

# 2. Use `reduce()` to concatenate a list of strings into a single sentence.
words = ["Learning", "Python", "is", "fun"]
s = reduce(lambda x, y: x + " " + y, words)
print(s)

# 3. Use `reduce()` to find the smallest number in a list.
numbers = [42, 17, 23, 8, 34]
smallest = reduce(lambda x, y: x if x < y else y, numbers)
print(smallest)

# 4. Use `reduce()` to compute the factorial of a number using a list: [1, 2, 3, ..., n].
n = 5
nums = [i for i in range(1, n+1)]
factorial = reduce(lambda x, y: x*y, nums)
print(factorial)