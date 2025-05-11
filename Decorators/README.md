## Decorators
- A decorator is a function that takes another function as input, adds some kind of functionality to it and returns a new function
- It's used for :
	- logging
	- access control
	- timing execution
	- memoization (caching)
	- input/output validation

### Decorators without using annotation
```python
    def my_decorator(function):
        def wrapper():
            print("I am decorating your function")
            function()  # Call the original function after the decoration
        return wrapper

    def hello_maaha():
        print("hello maaha")

    decorated_function = my_decorator(hello_maaha)
    decorated_function()
```

### Decorators with annotation
- Instead of calling the `my_decorator` function, we can directly call the `hello_maaha` function using annontation
- With the `@my_decorator` syntax, `hello_maaha` is directly replaced with the decorated version of the function.

```python
    def my_decorator(function):
        
        def wrapper():
            print("I am decorating your function")
            function()
        return wrapper

    @my_decorator
    def hello_maaha():
        print("hello maaha")

    hello_maaha()
```

### Decorators taking arguments
- The above decorators can't take arguments because the `function()` inside `wrapper()` that's calling `hello_maaha()` doesn't accepts arguments, so to change that we can pass `args` and `kwargs` to our wrapper functions

```python
    def my_decorator(function):
        
        def wrapper(*args, **kwargs):
            print("I am decorating your function")
            function(*args, **kwargs)
        return wrapper

    @my_decorator
    def hello_maaha(greeting):
        print("hello maaha")
        print(greeting)

    hello_maaha("Lets learn Python today")
```

### Decoraters returning values
- We can use the return statement for decorators to return values

```python
    def my_decorator(function):
        
        def wrapper(*args, **kwargs):
            print("I am decorating your function")
            return_stmt = function(*args, **kwargs)
            print(return_stmt)
        return wrapper

    @my_decorator
    def hello_maaha(greeting):
        print("hello maaha")
        return greeting

    hello_maaha("Lets learn Python today")
```