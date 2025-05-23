# Sets
- Sets are unordered, mutable collection with no duplicates

## Set Operations
```python
# Creating sets
set1 = {1, 2, 3}
set2 = set([3, 4, 5])

# Adding elements
set1.add(4)

# Removing elements
set1.remove(2)

# Union
union_set = set1 | set2

# Intersection
intersection_set = set1 & set2  

# Difference
difference_set = set1 - set2 

# Checking membership
is_member = 3 in set1
```