## Itertools
- `itertools` is a Python module that provides a set of fast, memory-efficient tools for creating iterators
- These tools allow you to perform complex iteration tasks easily without writing complex loops manually
- They are especially useful for:
    - Generating combinations, permutations, and Cartesian products
    - Creating infinite sequences of values
    - Filtering and grouping iterable data efficiently

### Common itertools Functions
1. `itertools.count(start=0, step=1)`
    - Creates an infinite iterator that generates numbers starting from `start`, increasing by `step`
    ```python
    import itertools
    counter = itertools.count(5, 2)  # Start at 5, step by 2
    print(next(counter))  # Output: 5
    print(next(counter))  # Output: 7
    print(next(counter))  # Output: 9
    ```

2. `itertools.cycle(iterable)`
    - Creates an infinite iterator that cycles through the elements of an iterable
    ```python
    import itertools

    colors = itertools.cycle(["Red", "Green", "Blue"])
    print(next(colors))  # Output: Red
    print(next(colors))  # Output: Green
    print(next(colors))  # Output: Blue
    print(next(colors))  # Output: Red (starts again)
    ```
3. `itertools.repeat(value, times=None)`
    - Repeats a value for a specified number of times (or infinitely if not specified)
    ```python
    import itertools

    repeated = itertools.repeat("Hello", 3)
    print(list(repeated))  

    # Output: ['Hello', 'Hello', 'Hello']
    ```
4. `itertools.chain(*iterables)`
    - Chains multiple iterables together into a single sequence
    ```python
    import itertools

    combined = itertools.chain([1, 2, 3], "ABC", (4, 5))
    print(list(combined))  

    # Output: [1, 2, 3, 'A', 'B', 'C', 4, 5]
    ```

5. `itertools.combinations(iterable, r)`
    - Generates all unique combinations (order does not matter) of length `r` from the iterable
    ```python
    import itertools

    letters = ["A", "B", "C"]
    combinations = itertools.combinations(letters, 2)
    print(list(combinations))  

    # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
    ```

6. `itertools.permutations(iterable, r)`
    - Generates all unique permutations (order matters) of length `r` from the iterable
    ```python
    import itertools

    letters = ["A", "B", "C"]
    permutations = itertools.permutations(letters, 2)
    print(list(permutations))  

    # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    ```

7. `itertools.product(*iterables, repeat=1)`
    - Generates the Cartesian product of the given iterables
    ```python
    import itertools

    colors = ["Red", "Green"]
    sizes = ["S", "M"]
    product = itertools.product(colors, sizes)
    print(list(product))  

    # Output: [('Red', 'S'), ('Red', 'M'), ('Green', 'S'), ('Green', 'M')]
    ```

### Exercises
1. **Create an Infinite Counter :** 
    - Use `itertools.count()` to create an infinite counter that starts from 10 and increases by 3
    - Use a for loop to print the first 10 values from this counter

2. **Generate Combinations of Student Pairs :**
    - Given a list of student names: `["Alice", "Bob", "Charlie", "Daisy", "Evan"]`
    - Use `itertools.combinations()` to generate all possible unique pairs of students
    - Print each pair on a separate line
    - Example Output:
        ```python 
        ('Alice', 'Bob')
        ('Alice', 'Charlie')
        ... 
        ```

3. **Cartesian Product for Restaurant Menu**
    - Create a list of main courses: `["Pizza", "Burger"]`
    - Create a list of drinks: `["Coke", "Lemonade"]`
    - Use `itertools.product()` to create a complete menu showing all combinations of main course and drink
    - Example Output:
        ```python 
        ('Pizza', 'Coke')
        ('Pizza', 'Lemonade')
        ('Burger', 'Coke')
        ('Burger', 'Lemonade')
        ```

4. **Grouping Words by Length**
    - Create a list of words: `["apple", "car", "banana", "dog", "elephant", "cat"]`
    - Use `itertools.groupby()` to group the words by their length
    - Print the length of the words and the list of words of that length
    - Expected Output:
        ```python
        Length 5: ['apple']
        Length 3: ['car', 'dog', 'cat']
        Length 6: ['banana']
        Length 8: ['elephant']
        ```