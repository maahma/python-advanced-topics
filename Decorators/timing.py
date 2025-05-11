import time

def timing(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = function(*args, **kwargs)
        fname = function.__name__
        end_time = time.time()
        print(f"{fname} took {end_time - start_time} to execute")
        return value
    return wrapper

@timing
def counting(x):
    result = 1
    for i in range(1, x):
        result *= i

    return result

counting(100000)