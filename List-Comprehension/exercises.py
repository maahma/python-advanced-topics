# Question 1 : Write a list comprehension that generates a list of the squares of even numbers from 1 to 20 (inclusive).
square_arr = [x**2 for x in range(1, 21) if x%2==0]
print (square_arr)

# Question 2 : Given a list of names, use a list comprehension to create a new list containing the uppercase version of the names that start with the letter "a" (case insensitive).
names = ["Alice", "bob", "Anna", "Mark", "adam"]
upper_arr = [x.upper() for x in names if x.lower().startswith("a")]
print(upper_arr)

# Question 3 : Create a list of tuples (x, y, x*y) for all combinations where x is from 1 to 3 and y is from 1 to 3 using a nested list comprehension.
t = [(x, y, x*y) for x in range(1, 4) for y in range(1, 4)]
print(t)

# Question 4 : Given a 2D list, use a  list comprehension to flatten it into a single list
matrix = [[1, 2], [3, 4], [5, 6]]
flat_arr = [num for arr in matrix for num in arr]
print(flat_arr)