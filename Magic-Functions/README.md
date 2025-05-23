# Magic Functions
- Magic methods are the methods starting and ending with double underscores `__`
- Built in classes define many magic methods which we can see by doing `dir(<class>)` e.g. `dir(int)` will show methods like `__abs__`, `__add__` etc.
- `__init__` is an example of a magic method used for initializing a class. This is called by the `__new__` method

### Common Dunder Methods:
- `__init__`: Constructor
- `__str__`: Readable string
- `__repr__`: Debug string
- `__add__`: + operator
- `__len__`: Length with len()