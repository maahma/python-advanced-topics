# Python Advanced topics

Learning and practicing advanced Python topics

### Resources used
- [Neural Nine Python Advanced Tutorials Playlist](https://www.youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc)
- [Patrick Loeber Advanced Python - Complete Course Playlist](https://www.youtube.com/playlist?list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2)
- [Advanced Python Tutorials from learnpython.org](https://www.learnpython.org/#:~:text=what%20you%27ve%20learned-,Advanced%20Tutorials,-Generators)

### Topics to learn
- [x] [Decorators](https://github.com/maahma/python-advanced-topics/tree/main/Decorators)
- [x] [Closures](https://github.com/maahma/python-advanced-topics/tree/main/Closures)
- [x] [Generators](https://github.com/maahma/python-advanced-topics/tree/main/Generators)
- [x] [Iter tools](https://github.com/maahma/python-advanced-topics/tree/main/itertools)
- [ ] List Comprehension
- [ ] Lambda Functions
- [ ] Sets
- [ ] Collections
- [ ] Serialization
- [ ] JSON in Python
- [ ] Parsing CSV Files
- [ ] Shallow vs Deep Copying
- [ ] Map, Filter, Reduce
- [ ] Magic Functions and Dunder Methods
- [ ] Multiple Function Arguments
- [ ] Asterisk
- [ ] Regular Expressions
- [ ] Exception Handling
- [ ] Encapsulation 
- [ ] Type Hinting
- [ ] Partial Functions
- [ ] Threading
- [ ] Multiprocessing
- [ ] Context Managers
- [ ] Factory Design Pattern
- [ ] Singleton Design Pattern
- [ ] Composite Design Pattern
- [ ] Logging
- [ ] Code Introspection
- [ ] Argument Parsing

### Exercises for practicing
#### 1️⃣ **Decorators and Closures**
- **Exercise:** Create a `timer` decorator that measures how long a function takes to execute.
- **Exercise:** Create a `retry` decorator that retries a function a specified number of times if it raises an exception.
- **Exercise:** Create a closure that keeps a count of how many times a function is called.

---
#### 2️⃣ **Generators and Itertools**
- **Exercise:** Create a generator function that generates Fibonacci numbers up to a specified value.
- **Exercise:** Use `itertools` to generate an infinite cycle of a list of items (`['A', 'B', 'C']`).
- **Exercise:** Use `itertools` to generate all combinations of a list of numbers.

---
#### 3️⃣ **List Comprehension and Lambda Functions**
- **Exercise:** Create a list comprehension that generates all even numbers between 1 and 100.
- **Exercise:** Use a lambda function and `map` to square all numbers in a list.
- **Exercise:** Use `filter` and lambda to filter out numbers divisible by 3 from a list.

---
#### 4️⃣ **Multiple Function Arguments and Asterisk**
- **Exercise:** Create a function that accepts any number of positional arguments and keyword arguments and prints them.
- **Exercise:** Create a function that unpacks a list of values into separate arguments.

---
#### 5️⃣ **Regular Expressions**
- **Exercise:** Write a function that uses regex to validate an email address.
- **Exercise:** Create a function that extracts all phone numbers from a text string.

---
#### 6️⃣ **Exception Handling**
- **Exercise:** Create a function that divides two numbers and handles `ZeroDivisionError`, `TypeError`, and `ValueError`.
- **Exercise:** Create a custom exception `InsufficientFundsError` for a banking application.

---
#### 7️⃣ **Sets and Collections**
- **Exercise:** Create a function that takes two lists and returns the common elements using sets.
- **Exercise:** Use `collections.Counter` to count the frequency of words in a string.

---
#### 8️⃣ **Serialization (JSON and CSV)**
- **Exercise:** Create a function that serializes a Python dictionary to a JSON file.
- **Exercise:** Write a function that reads a CSV file and converts it to a list of dictionaries.

---
#### 9️⃣ **Shallow vs Deep Copying**
- **Exercise:** Create a nested list and demonstrate the difference between shallow and deep copying using `copy` and `deepcopy`.

---
#### 🔟 **Magic Functions and Dunder Methods**
- **Exercise:** Create a class `Point` with `__add__` and `__str__` dunder methods for adding two points and printing them.
- **Exercise:** Create a class `Counter` that has a `__call__` method to count the number of times it is called.

---
#### 1️⃣1️⃣ **Encapsulation and Type Hinting**
- **Exercise:** Create a class `BankAccount` with private attributes for balance and methods to deposit and withdraw.
- **Exercise:** Add type hints to all the methods in the class.

---
#### 1️⃣2️⃣ **Partial Functions**
- **Exercise:** Use `functools.partial` to create a function that always adds 10 to any number.

---
#### 1️⃣3️⃣ **Threading and Multiprocessing**
- **Exercise:** Create a program that calculates the sum of a list of numbers using threading.
- **Exercise:** Create a program that calculates the factorial of a number using multiprocessing.

---
#### 1️⃣4️⃣ **Context Managers**
- **Exercise:** Create a custom context manager using a class for opening and closing a file.
- **Exercise:** Create a context manager using the `@contextmanager` decorator to temporarily change the working directory.

---
#### 1️⃣5️⃣ **Design Patterns (Factory, Proxy, Singleton, Composite)**
- **Exercise:** Implement a `ShapeFactory` using the Factory pattern that returns different shape objects.
- **Exercise:** Implement a Proxy pattern where an object is used to control access to a sensitive resource.
- **Exercise:** Implement a Singleton class `DatabaseConnection` that ensures only one connection object exists.

### Mini Project Ideas (Combining concepts)
1. **Task Manager CLI:**
    - Use `argparse` for command-line arguments.
    - Use JSON for saving task data.
    - Use threading to allow for timer-based tasks.
    - Use decorators for logging.
2. **Personal Finance Tracker:**
    - Use JSON for storing expenses.
    - Use CSV for importing and exporting expense data.
    - Use regex for validating descriptions and amounts.
    - Use a Factory pattern for creating different types of transactions (Expense, Income).
3. **File Organizer:**
    - Use threading to speed up file moving.
    - Use context managers to handle file operations.
    - Use closures for counting the number of files organized.
    - Use sets to avoid duplicate file names.
4. **Quiz Application:**
    - Use decorators to log user scores.
    - Use context managers for file handling (question bank).
    - Use JSON to save user progress.
    - Use closures for tracking score across multiple attempts.
5. **Chatbot with Custom Commands:**
    - Use regex to detect commands.
    - Use a Proxy pattern for restricted commands.
    - Use type hinting for better code quality.
    - Use threading for asynchronous command handling.
