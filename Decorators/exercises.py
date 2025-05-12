''' 
1. Simple Decorator:
    - Write a decorator `logging_decorator` that prints `"Function is being called"` before the function is executed.
    - Apply this decorator to a function `say_hello()` that prints `"Hello!"`.
'''
def logging_decorator(function):
    def wrapper():
        print("Function is being called")
        function()
    return wrapper

@logging_decorator
def say_hello():
    print("Hello")

say_hello()

# ---------------------------------------------------------------------------------------

'''
2. Decorator with Arguments:
    - Write a decorator `time_logger` that prints `"Executing with arguments: <args, kwargs>"` before calling the function.
    - Use this decorator on a `function add_numbers(a, b)` that returns the sum of two numbers.
'''
def time_logger(function):
    def wrapper(*args, **kwargs):
        print(f"Executing with arguments: {args}, {kwargs} ")
        sum = function(*args, **kwargs)
        return sum
    return wrapper

@time_logger
def add_numbers(a,b):
    return a+b

print(add_numbers(5,5))

# ---------------------------------------------------------------------------------------

'''
3. Decorator with Return Value:
    - Write a decorator `multiply_result` that multiplies the result of the decorated function by 2.
    - Apply this decorator to a function `calculate_square(n)` that returns the square of `n`.
'''
def multiply_result(function):
    def wrapper(*args, **kwargs):
        square = function(*args, **kwargs) * 2
        return square

    return wrapper

@multiply_result
def calculate_square(n):
    return n**2

print(calculate_square(10))

# ---------------------------------------------------------------------------------------

'''
4. Combining Multiple Decorators:
    - Write two decorators:
       - `bold_decorator` - makes the text uppercase.
       - `italic_decorator` - adds underscores around the text.
    - Apply both decorators (in any order) to a function `format_text()` that returns the string `"Hello, Maaha!"`.
'''

def bold_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper         


def italic_decorator(function):
    def wrapper():
        result = "_" + function()+ "_"
        return result
    return wrapper
    
@italic_decorator
@bold_decorator
def format_text():
    return "Hello, Maaha"

print(format_text())
