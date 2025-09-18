# Chapter 39: Default and Keyword Arguments

## 1. Introduction
Default values and keyword arguments let you write flexible functions with sensible defaults and clear calls.

---

## 2. Default Arguments Example
```python
def greet(name='Guest'):
    print('Hello,', name)

greet()          # Hello, Guest
greet('Alice')   # Hello, Alice
```

---

## 3. Keyword Arguments Example
```python
def describe(name, age):
    print(f"{name} is {age} years old")

describe(age=25, name='Bob')
```

---

## 4. Mixing Positional and Keyword Arguments
Positional arguments must come before keyword arguments when calling a function:

```python
def display(a, b, c):
    print(a, b, c)

display(1, c=3, b=2)
```

---

## 5. Mutable Default Argument Pitfall
Avoid using mutable defaults (lists, dicts) directly.

Bad example:
```python
def add_item(item, collection=[]):
    collection.append(item)
    return collection
```

Better pattern:
```python
def add_item(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection
```

---

## 6. Best Practices
- Use immutable default values when possible.  
- Use keyword arguments to improve readability for functions with many parameters.

---

## 7. Next Steps
✅ You now understand default and keyword arguments.  
Next: **\*args and \*\*kwargs**.
