# Chapter 18: Basic Data Types

## 1. Introduction
Python has several built-in data types that form the foundation of the language.  
Understanding these is essential because you will use them in almost every program.  

---

## 2. Numbers
Python has different types of numbers:
- **Integers (`int`)** → whole numbers  
- **Floating-point numbers (`float`)** → decimal numbers  
- **Complex numbers (`complex`)** → numbers with real and imaginary parts  

Examples:

```python
a = 10        # int
b = 3.14      # float
c = 2 + 3j    # complex
```

Check their types:

```python
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
```

---

## 3. Strings
A **string** is text enclosed in quotes.

```python
name = "Alice"
greeting = 'Hello, world!'
```

Strings can be joined:

```python
first = "Py"
second = "thon"
print(first + second)  # Python
```

---

## 4. Booleans
A **boolean** is either `True` or `False`.

```python
is_active = True
is_logged_in = False
```

Booleans often come from comparisons:

```python
print(5 > 3)   # True
print(2 == 4)  # False
```

---

## 5. None
`None` is a special type representing the absence of a value.

```python
result = None
print(result)  # None
```

---

## 6. Lists
A **list** is an ordered, changeable collection.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
```

Lists can be modified:

```python
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```

---

## 7. Tuples
A **tuple** is an ordered, unchangeable collection.

```python
point = (3, 4)
print(point[0])  # 3
```

---

## 8. Sets
A **set** is an unordered collection of unique items.

```python
numbers = {1, 2, 3, 3}
print(numbers)  # {1, 2, 3}
```

---

## 9. Dictionaries
A **dictionary** stores data as key-value pairs.

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
```

---

## 10. Dynamic Typing in Python
You can reassign a variable to a different type:

```python
x = 10
print(type(x))  # int
x = "hello"
print(type(x))  # str
```

---

## 11. Checking Data Types
Use `type()` and `isinstance()`:

```python
x = 3.14
print(type(x))               # <class 'float'>
print(isinstance(x, float))  # True
```

---

## 12. Next Steps
✅ You now know Python’s basic data types: numbers, strings, booleans, None, lists, tuples, sets, and dictionaries.  
In the next chapter, we’ll learn about **type conversion and casting**.