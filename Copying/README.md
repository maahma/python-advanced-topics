# Shallow vs Deep Copy
When copying objects in Python, it's important to understand whether the copy is shallow or deep, especially for compound objects like lists of lists or dictionaries containing other mutable objects

## Shallow Copy
- It creates a new object, but does not create copies of nested objects inside it
- The new object refers to the same nested objects as the original

### Syntax
```python
copy.copy(obj)
```

### Example
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] – original is affected
```

## Deep Copy
- It creates a new object and recursively copies all nested objects
- It ensures the new object is completely independent

### Syntax
```python
copy.deepcopy(obj)
```

### Example
```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]] – original is unaffected
```