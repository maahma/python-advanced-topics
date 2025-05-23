# List Comprehension
- List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

### Syntax
```python
newlist = [_expression_ for _item_ in _iterable_ if _condition_ == True]
```
- The `condition` is like a filter that only accepts items that evaluate to `true`
- The `iterable` can be any iterable object, like a list, tuple, set etc. 
### Without List Comprehension
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  

newlist = []  
  
for x in fruits:  
  if "a" in x:  
    newlist.append(x)  
  
print(newlist)

# Output
# ['apple', 'banana', 'mango']
```
### With List Comprehension
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
  
newlist = [x for x in fruits if "a" in x]  
print(newlist)

# Output
# ['apple', 'banana', 'mango']
```
## Exercises
1. Write a list comprehension that generates a list of the squares of even numbers from 1 to 20 (inclusive).
2. Given a list of names, use a list comprehension to create a new list containing the uppercase version of the names that start with the letter "a" (case insensitive).

    **Example input**:
    ```python
    names = ["Alice", "bob", "Anna", "Mark", "adam"]
    ```
    
    **Expected output**:
    ```python
    ["ALICE", "ANNA", "ADAM"]
    ```

3. Create a list of tuples (x, y, x*y) for all combinations where x is from 1 to 3 and y is from 1 to 3 using a nested list comprehension.

    **Expected output**:
    ```python
    [(1, 1, 1), (1, 2, 2), ..., (3, 3, 9)]
    ```

4. Given a 2D list like:

    ```python
    matrix = [[1, 2], [3, 4], [5, 6]]
    ```
    Use a list comprehension to flatten it into a single list:
    ```python
    [1, 2, 3, 4, 5, 6]
    ```