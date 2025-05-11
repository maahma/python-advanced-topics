# Decorators without annotation
def my_decorator(function):
        
        def wrapper():
            function()
            print("I am decorating your function")
        return wrapper

def hello_maaha():
    print("hello maaha")

my_decorator(hello_maaha)()

# -------------------------------------------------------------------------

# Decorators with annotation
def my_decorator(function):
        
        def wrapper():
            function()
            print("I am decorating your function")
        return wrapper

@my_decorator
def hello_maaha():
    print("hello maaha")

hello_maaha()

# -------------------------------------------------------------------------

# Passing arguments to decorators
def my_decorator(function):
        
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print("I am decorating your function")
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
            return_stmt = function(*args, **kwargs)
            print(return_stmt)
            print("I am decorating your function")
        return wrapper

@my_decorator
def hello_maaha(greeting):
    print("hello maaha")
    return greeting

hello_maaha("Lets learn Python today")