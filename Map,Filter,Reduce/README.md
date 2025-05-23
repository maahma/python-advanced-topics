# Map, Filter, Reduce

## Map
- The `map()` method applies a function to all items in an iterable
- Uses the lambda function

### Syntax
```python
map(<lambda function>, <iterable>)
```

### Example
```python
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))  # [1, 4, 9]
```

## Filter
- The `filter()` method filters items for which the function returns `True`
- Uses the lambda function

### Syntax
```python
filter(<lambda function>, <iterable>)
```

### Example
```python
nums = [1, 2, 3]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2]
```

## Reduce
- The `reduce()` function reduces a list into a single value by applying a function cumulatively
- This function must be imported from `functools`
- Uses the lambda function

### Syntax
```python
from functools import reduce
reduce(function, iterable)
```

### Example
```python
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])
# Output: 10 
```
- How it works step by step:
    - Start with the first two items: 1 + 2 → 3
    - Then take the result and add the next item: 3 + 3 → 6
    - Then: 6 + 4 → 10
    - Final result: 10


Another example: finding the longest word
```python
words = ["hi", "hello", "world", "Python"]

longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)  # Output: "Python"
```

## Exercises
### Map Questions
1. Use `map()` to convert a list of strings to uppercase.
2. Given a list of numbers, use `map()` to return their cube values.
3. Use `map()` to add corresponding elements from two lists: `[1, 2, 3]` and `[4, 5, 6]`.
4. Given a list of full names, use `map()` to extract only the first names.

### Filter Questions
1. Use `filter()` to find all numbers divisible by 3 from a list.
2. Given a list of strings, filter out all empty strings.
3. Use `filter()` to remove negative numbers from a list.
4. Given a list of words, use filter() to return only words that start with a vowel.

### Reduce Questions
1. Use `reduce()` to compute the sum of a list of numbers.
2. Use `reduce()` to concatenate a list of strings into a single sentence.
3. Use `reduce()` to find the smallest number in a list.
4. Use `reduce()` to compute the factorial of a number using a list: [1, 2, 3, ..., n].

