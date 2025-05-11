def outer_function(message):
    def inner_function():
        print(message)  # Remembers 'message' from outer scope
    return inner_function

closure_example = outer_function("Hello, I am a closure!")
closure_example()  # Output: Hello, I am a closure!
print(closure_example.__closure__)