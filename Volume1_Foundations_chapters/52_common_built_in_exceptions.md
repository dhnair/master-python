# Volume 1: Foundations
## Chapter 52: Common Built-in Exceptions

### 1. Introduction
Python provides many built-in exception types. Knowing the most common ones helps write better error handling.

---

### 2. Common Exceptions
- **ValueError** → wrong value
```python
int("abc")  # ValueError
```

- **TypeError** → wrong type
```python
"2" + 3  # TypeError
```

- **IndexError** → invalid list index
```python
[1, 2][5]  # IndexError
```

- **KeyError** → missing dictionary key
```python
{"a": 1}["b"]  # KeyError
```

- **ZeroDivisionError** → divide by zero
```python
10 / 0
```

- **FileNotFoundError** → missing file
```python
open("missing.txt")
```

- **ImportError / ModuleNotFoundError** → module not found
```python
import nonexistent
```

- **AttributeError** → attribute doesn’t exist
```python
"hello".not_a_method()
```

---

### 3. Handling Multiple Exceptions
```python
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)
```

---

### 4. Next Steps
✅ You now know common built-in exceptions.  
Next: **Dates and times** in Python.
