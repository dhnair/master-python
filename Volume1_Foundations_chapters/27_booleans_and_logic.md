# Volume 1: Foundations
## Chapter 27: Booleans and Logic

### 1. Introduction
A **boolean** is a data type with only two possible values: `True` or `False`.  
Booleans are the foundation of decision-making in programming.  

In Python, booleans often appear as the result of **comparisons** or **logical operations**.  

---

### 2. Boolean Values
```python
x = True
y = False
print(x)        # True
print(type(x))  # <class 'bool'>
```

---

### 3. Comparisons that Return Booleans
```python
print(5 > 3)   # True
print(10 == 2) # False
print(7 <= 7)  # True
```

---

### 4. The `bool()` Function
Any value can be converted to a boolean using `bool()`.  

- Falsy values (evaluated as `False`):  
  - `0`, `0.0`  
  - `""` (empty string)  
  - `[]`, `{}`, `()` (empty collections)  
  - `None`  
  - `False`  

- Everything else is `True`.  

Examples:

```python
print(bool(0))       # False
print(bool(""))      # False
print(bool("hi"))    # True
print(bool([1, 2]))  # True
```

---

### 5. Logical Operators
Logical operators combine boolean values.

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

### 6. Combining Comparisons
You can use logical operators with comparisons:

```python
x = 10
print(x > 5 and x < 20)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
```

---

### 7. Operator Precedence with Booleans
Order of evaluation:  
1. `not`  
2. `and`  
3. `or`  

Example:

```python
print(True or False and False)   # True (and is evaluated first)
```

---

### 8. Identity and Membership in Boolean Contexts
```python
fruits = ["apple", "banana"]

print("apple" in fruits)     # True
print("cherry" not in fruits) # True

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
```

---

### 9. Practical Examples
```python
age = 18
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")
```

---

### 10. Next Steps
✅ You now understand booleans, comparisons, and logical operators.  
In the next chapter, we’ll explore **if statements**, the first step into control flow.