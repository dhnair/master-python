# Chapter 19: Type Conversion and Casting

## 1. Introduction
Sometimes you need to change a value from one type to another.  
For example, converting a string `"123"` into a number `123`.  
This process is called **type conversion** or **casting**.  

Python supports two types of conversions:  
- **Implicit Conversion (Type Casting by Python)**  
- **Explicit Conversion (Manual Casting by the Programmer)**  

---

## 2. Implicit Type Conversion
Python automatically converts smaller data types to larger ones when needed.  

Example:

```python
x = 10        # int
y = 2.5       # float
z = x + y     # int + float
print(z)      # 12.5
print(type(z))  # <class 'float'>
```

Here, Python automatically converted `x` into a float.  

---

## 3. Explicit Type Conversion
You can manually convert a value to another type using built-in functions.  

- Convert to integer:  

```python
x = int("42")
print(x)        # 42
print(type(x))  # <class 'int'>
```

- Convert to float:  

```python
y = float("3.14")
print(y)        # 3.14
```

- Convert to string:  

```python
z = str(100)
print(z)        # "100"
print(type(z))  # <class 'str'>
```

---

## 4. Converting Between Data Types
- List to Tuple:

```python
numbers = [1, 2, 3]
t = tuple(numbers)
print(t)  # (1, 2, 3)
```

- Tuple to List:

```python
t = (4, 5, 6)
lst = list(t)
print(lst)  # [4, 5, 6]
```

- List to Set:

```python
numbers = [1, 2, 2, 3]
s = set(numbers)
print(s)  # {1, 2, 3}
```

- Dictionary Keys to List:

```python
person = {"name": "Alice", "age": 25}
keys = list(person.keys())
print(keys)  # ['name', 'age']
```

---

## 5. Converting Booleans
Booleans (`True` or `False`) can also be converted.  

```python
print(int(True))   # 1
print(int(False))  # 0
print(bool(0))     # False
print(bool(42))    # True
print(bool(""))    # False
print(bool("hi"))  # True
```

---

## 6. Common Pitfalls
- Converting non-numeric strings to numbers will fail:  

```python
x = int("hello")  # ValueError
```

- Floating-point to integer conversion **truncates** (does not round):  

```python
print(int(3.99))  # 3
```

---

## 7. When to Use Conversion
- When reading user input (always a string by default).  
- When working with files or APIs that return text.  
- When preparing data for mathematical operations.  

---

## 8. Next Steps
✅ You now understand how to convert between Python data types.  
In the next chapter, we’ll dive into **operators** and how they work with different types.