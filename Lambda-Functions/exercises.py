# Create a lambda function that returns the cube of a number. Use it to calculate the cube of 3.
cube = lambda x: x*x*x
print(cube(3))

# Write a lambda function that checks if a number is even. Use it to test the number 6.
even = lambda x: x%2==0
print(even(6))

# Create a function make_incrementer(n) that returns a lambda function. The returned function should add n to its input.
def make_incrementer(n):
    return lambda x: x+n

add_five = make_incrementer(5)
print(add_five(10))

# Given a list of strings ["cat", "apple", "banana", "hat"], sort them by length using a lambda function and the sorted() function
sort_list = lambda arr: sorted(arr, key=lambda x: len(x))
print(sort_list(["cat", "apple", "banana", "hat"]))