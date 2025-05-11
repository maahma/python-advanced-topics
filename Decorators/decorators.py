# Decorators without annotation
def my_decorator(function):
        def wrapper():
            print("I am decorating your function")
            function()  # Call the original function after the decoration
        return wrapper

def hello_maaha():
    print("hello maaha")

decorated_function = my_decorator(hello_maaha)
decorated_function()

# -------------------------------------------------------------------------

# Decorators with annotation
def my_decorator(function):
        
        def wrapper():
            print("I am decorating your function")
            function()
        return wrapper

@my_decorator
def hello_maaha():
    print("hello maaha")

hello_maaha()

# -------------------------------------------------------------------------

# Passing arguments to decorators
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

# -------------------------------------------------------------------------

# Decorators returning values
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