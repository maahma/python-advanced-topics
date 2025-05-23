# Lambda Functions
A lambda function is a small anonymous function for one time use which we then throw away
- They take any number of arguments but must contain only one expression
- They help keep the **namespace clean** because we don’t have to give the function a name.
- Commonly used with **higher-order functions** like `sort()`, `map()`, `filter()`, and `reduce()``
### Syntax
```python
lambda <parameter>: <expression>
```
- The expression is automatically returned, no need to write `return`

### Example
1. Lambda function to add two numbers
    ```python
    add = lambda a, b: a + b
    print(add(3, 4))  # Output: 7
    ```

2. Lambda function to square a number
    ```python
    square = lambda a: a*a
    print(square(3))  # Output: 9
    ```

## Exercises
1. Create a lambda function that returns the cube of a number. Use it to calculate the cube of 3.

2. Write a lambda function that checks if a number is even. Use it to test the number 6.

3. Create a function `make_incrementer(n)` that returns a lambda function. The returned function should add `n` to its input.
    ```python
    add_five = make_incrementer(5)
    print(add_five(10))  # Output should be 15
    ```

4. Given a list of strings `["cat", "apple", "banana", "hat"]`, sort them by length using a lambda function and the `sorted()` function.