# Chapter 37: Defining and Calling Functions

## 1. Introduction
A **function** is a reusable block of code that performs a specific task. Functions improve modularity and reduce repetition.

---

## 2. Defining a Simple Function
```python
def greet():
    print("Hello, world!")
```

---

## 3. Calling a Function
```python
greet()  # Output: Hello, world!
```

---

## 4. Functions with Parameters
```python
def greet(name):
    print("Hello,", name)

greet("Alice")
```

---

## 5. Returning Values
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

---

## 6. Multiple Return Values (Tuples)
```python
def min_and_max(values):
    return min(values), max(values)

low, high = min_and_max([1, 2, 3])
print(low, high)  # 1 3
```

---

## 7. Docstrings and Function Help
```python
def square(x):
    "Return square of x."
    return x * x

help(square)  # shows docstring
```

---

## 8. Pure Functions vs Side Effects
- **Pure function**: same input → same output, no side effects.  
- **Side effect**: writing to file, modifying global variables, etc. Prefer pure functions when possible.

---

## 9. Best Practices
- Use descriptive function names.  
- Keep functions short and focused (single responsibility).  
- Write docstrings for public functions.

---

## 10. Next Steps
✅ You now know how to define and call functions.  
Next chapter: **Function arguments and return values**.
