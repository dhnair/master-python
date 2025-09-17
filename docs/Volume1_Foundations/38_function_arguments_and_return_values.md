# Volume 1: Foundations
## Chapter 38: Function Arguments and Return Values

### 1. Introduction
Functions take inputs (arguments) and may produce outputs (return values). Understanding how arguments are passed and how returns work is essential.

---

### 2. Positional Arguments
```python
def multiply(a, b):
    return a * b

print(multiply(2, 3))  # 6
```

---

### 3. Keyword Arguments (Named Arguments)
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet(age=30, name="Alice")
```

---

### 4. Default Return Value (None)
If a function does not return explicitly, it returns `None`.

```python
def say_hi():
    print("Hi")

result = say_hi()
print(result)  # None
```

---

### 5. Returning Multiple Values
Functions can return tuples which can be unpacked.

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = stats([1, 2, 3])
print(low, high, total)
```

---

### 6. Arguments vs Parameters
- **Parameters** are names in function definition.  
- **Arguments** are actual values passed to the function.

---

### 7. Type Hints (Optional)
Python supports optional type hints for better readability and tooling:

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

### 8. Best Practices
- Validate arguments where appropriate.  
- Return early if inputs are invalid.  
- Keep return types consistent for easier use.

---

### 9. Next Steps
✅ You now understand arguments and return values.  
Next: **Default and keyword arguments**.
