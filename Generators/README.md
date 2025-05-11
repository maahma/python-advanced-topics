## Generators
- A generator is a type of function in Python that allows you to generate values one at a time, on demand, without storing the entire sequence in memory
- It is defined using the `yield` keyword instead of `return`

### Key Characteristics:
- **Lazy Evaluation**: Generates values one by one, only when requested
- **State Retention**: Remembers its state (local variables, position) between calls
- **Iterability**: Can be used directly in a `for` loop or with `next()`

### Difference Between `yield` and `return`
1. `return`:
	- Exits the function and returns a value immediately
	- Can only be called once in a function (ending it)
2. `yield`:
	- Pauses the function and "yields" a value
	- Can be used multiple times in a function
	- The function remembers its state and can be resumed.

### Example
```python
def count_up_to_three():
	yield 1
	yield 2
	yield 3

counter = count_up_to_three()
print(next(counter))
print(next(counter))
print("hello world")
print(next(counter))

# Output
# 1
# 2
# hello world
# 3
```
### Generators in large datasets

- Generators are useful when processing a large dataset (like logs, CSV or database records)
- They avoid storing the entire dataset in memory, making them memory-efficient.

```python
def mygenerator(n):
	for x in range(n):
		yield x ** 3

values = mygenerator(9000000)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

# Output
# 0
# 1
# 8
# 27
# 64
# 125
```
### Iterating over a generator using a `for` loop
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(5):
    print(value)

# Output
# 5
# 4
# 3
# 2
# 1
```
### Exercises
1. **Fibonacci Generator**:
	- Write a generator function `fibonacci_generator()` that generates the Fibonacci sequence one number at a time
	- Use a `for` loop to print the first 10 Fibonacci numbers
	- Example Output:
		```
		0
		1
		1
		2
		3
		5
		8
		13
		21
		34
		```
2. **Infinite Even Numbers**:
	- Write a generator function `infinite_even_numbers()` that generates even numbers starting from 0
	- Use the `next()` function to print the first 5 even numbers
	- Example Output:
		```
		0
		2
		4
		6
		8
		```
3. **Filtered File Reader**:
	- Write a generator function `filtered_file_reader(filename, keyword)` that reads a text file line by line using `yield` and only yields lines that contain a specific keyword
	- Test it by creating a text file and reading lines that contain the word "Python"
	- Example Text File (`sample.txt`):
		```
		I love Python.
		Python is amazing.
		JavaScript is also great.
		But I prefer Python.
		```
	- Example Usage:

		```python
		for line in filtered_file_reader("sample.txt", "Python"):
			print(line)
		```
	- Example Output:
		```
		I love Python.
		Python is amazing.
		But I prefer Python.
		```
4. **Prime Number Generator**:
	- Write a generator function `prime_generator()` that generates prime numbers one at a time
	- Use a for loop to print the first 10 prime numbers
	- Example Output:
        ```
		2
		3
		5
		7
		11
		13
		17
		19
		23
		29
		```