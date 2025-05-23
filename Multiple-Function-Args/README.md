# Multiple Function Arguments
- Python allows functions to accept a variable number of arguments using `*args` and `**kwargs`

## `*args` (Non-keyword Variable Arguments)
- Collects extra positional arguments as a tuple

### Example
```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))  # Output: 6
```

## `**kwargs` (Keyword Variable Arguments)
- Collects extra keyword arguments as a dictionary

```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
```

## Mixing `*args` and `**kwargs`
- We can use both in the same function
- Remember: `*args` comes before `**kwargs`

```python
def greet_people(greeting, *names, **custom_messages):
    for name in names:
        msg = custom_messages.get(name, "")
        print(f"{greeting}, {name}! {msg}")

greet_people("Hello", "Alice", "Bob", Alice="Good to see you!")
# Output:
# Hello, Alice! Good to see you!
# Hello, Bob!
```

## Argument Unpacking
- We can also use `*` and `**` to unpack arguments when calling functions:

```python
def multiply(x, y):
    return x * y

args = (3, 4)
print(multiply(*args))  # Output: 12

kwargs = {'x': 5, 'y': 6}
print(multiply(**kwargs))  # Output: 30
```