## Closures

### Pre-requisite of Closures - **First Class Functions** 
- In Python, **functions are treated as first-class citizens**.
- This means that functions can be:
    1. **Assigned to variables**
        ```python
        def hello_user(name):
            print(f"hello {name}")

        greet_user = hello_user
        greet_user("maaha")
        ```
    2. **Passed as arguments to other functions**.
        ```python
        def shout(text):
            return text.upper()

        def whisper(text):
            return text.lower()

        def process_text(func, text):
            return func(text)  # Calling the passed function

        print(process_text(shout, "Hello"))  # Output: HELLO
        print(process_text(whisper, "Hello"))  # Output: hello            
        ```
    3. **Returned from other functions** - Functions can be created inside other functions, and returned
        ```python
        def greeting_function(name):
            def greet():
                return f"Hello, {name}!"
            return greet  # Returning the inner function

        personal_greeting = greeting_function("Maaha")
        print(personal_greeting())  # Output: Hello, Maaha!
        ```
    4. **Stored in data structures (like lists, tuples, dictionaries)**
        ```python
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        operations = {
            "add": add,
            "subtract": subtract
        }

        print(operations["add"](5, 3))        # Output: 8
        print(operations["subtract"](5, 3))   # Output: 2
        ```
### What are Closures?
- Closures are basically first-class functions that "remember" the state of the outer scope (variables) in which they were created
- They maintain access to variables even after the outer function has finished executing
- Closures require:
    1. A nested function (a function defined inside another function)
    2. The nested function must use a variable from the outer function
    3. The outer function must return the inner (nested) function

#### Code Example
```python
def outer_function(message):
    def inner_function():
        print(message)  # Remembers 'message' from outer scope
    return inner_function

closure_example = outer_function("Hello, I am a closure!")
closure_example()  # Output: Hello, I am a closure!
```

### How to Identify a Closure in Python:
If you print the `__closure__` attribute of a function, you can see the variables it remembers.
```python
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

closure_example = outer_function("Hello, Closure!")
print(closure_example.__closure__)  # Will show the closure variables
```

### Exercises
#### First-Class Functions
1. Assigning Functions:
    - Write a function `square(x)` that returns `x * x`
    - Assign it to a variable `calculate_square` and use it to calculate the square of 5
2. Passing Functions as Arguments:
    - Write two functions:
        - `uppercase(text)` - returns the text in uppercase
        - `lowercase(text)` - returns the text in lowercase
    - Write another function `text_transformer(func, text)` that takes a function and a string as arguments and applies the function to the string
    - Test it with both `uppercase` and `lowercase`
3. Returning Functions:
    - Write a function `math_operation(operation)` that takes a string `("add", "subtract", "multiply", "divide")`
    - Based on the string, it should return the corresponding math function
    - Use the returned function to perform calculations
4. Storing Functions in Data Structures:
    - Create a dictionary `calculations` with keys as `"add", "subtract", "multiply", "divide"` and values as corresponding functions.
    - Use this dictionary to perform addition and subtraction.

#### Closures
1. Remembering Variables (Closure):
    - Write a function `greeting_generator(name)` that takes a name and returns a closure that always greets that name
    - The closure should return the message `"Hello, <name>!"`
    - Example:
        ```python
        greeter = greeting_generator("Maaha")
        print(greeter())  # Output: Hello, Maaha!
        ```

2. Counter Using Closures:
    - Write a function `create_counter()` that returns a closure
    - The closure should maintain a count of how many times it has been called and print the count

3. Personalized Message (Closure):
    - Write a function `personalized_message(greeting)` that takes a greeting message and returns a closure.
    - The closure should take a name as an argument and return the greeting message followed by the name.
    - Example:
        ```python
        hello_message = personalized_message("Hello")
        print(hello_message("Maaha"))  # Output: Hello, Maaha!
        ```

4. Calculating Power (Closure):
    - Write a function `power_function(exponent)` that takes an exponent value and returns a closure.
    - The closure should take a base value and return the result of base `**` exponent.
    - Example:
        ```python
        square = power_function(2)
        print(square(4))  # Output: 16

        cube = power_function(3)
        print(cube(2))  # Output: 8
        ```

5. Write a Python program that uses a nested function and a closure to create multiple multiplication functions. Specifically, use closures to create functions like `multiply_with_5()` and `multiply_with_4()`, which multiply any given number by 5 or 4, respectively.
