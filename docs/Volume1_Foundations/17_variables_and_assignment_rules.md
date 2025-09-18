# Chapter 17: Variables and Assignment Rules

## 1. Introduction
A **variable** is a name that stores a value in memory.  
In Python, you don’t need to declare a variable type — Python figures it out automatically.  
This is called **dynamic typing**.  

---

## 2. Creating Variables
Assign a value to a variable with the `=` operator:

```python
x = 10
name = "Alice"
pi = 3.14
```

---

## 3. Variable Naming Rules
- Must start with a letter or underscore (`_`).  
- Can contain letters, numbers, and underscores.  
- Case-sensitive (`Name` and `name` are different).  
- Cannot be a Python keyword (`if`, `while`, `class`, etc.).  

✅ Valid examples:  
```python
user_name = "Bob"
age2 = 25
_price = 99.99
```

❌ Invalid examples:  
```python
2cool = "nope"      # cannot start with a number
first-name = "Eve"  # hyphen not allowed
class = "Physics"   # reserved keyword
```

---

## 4. Reassigning Variables
You can change a variable’s value at any time:

```python
x = 5
x = "hello"
```

Here, `x` first held a number, then a string.  

---

## 5. Multiple Assignments
You can assign multiple variables at once:

```python
a, b, c = 1, 2, 3
```

Or give multiple variables the same value:

```python
x = y = z = 0
```

---

## 6. Constants in Python
Python does not have true constants, but by convention:  
- Use ALL_CAPS names for values that should not change.  

```python
PI = 3.14159
MAX_USERS = 100
```

---

## 7. Checking Variable Type
Use the built-in `type()` function:

```python
x = 42
print(type(x))   # <class 'int'>
```

---

## 8. Deleting Variables
You can delete a variable with `del`:

```python
x = 10
del x
```

Trying to use `x` now will give an error.  

---

## 9. Best Practices
- Use descriptive names (`age` instead of `a`).  
- Follow lowercase_with_underscores convention.  
- Avoid single-letter names except in loops (`i`, `j`).  

---

## 10. Next Steps
✅ You now understand how variables work and the rules for naming them.  
In the next chapter, we’ll explore Python’s **basic data types**.