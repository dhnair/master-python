# Volume 1: Foundations
## Chapter 20: Operators

### 1. Introduction
**Operators** are symbols that perform operations on variables and values.  
Python supports several categories of operators:  
- Arithmetic  
- Comparison  
- Logical  
- Assignment  
- Bitwise  
- Membership  
- Identity  

---

### 2. Arithmetic Operators
Used for basic math operations.  

```python
x = 10
y = 3

print(x + y)  # 13 (Addition)
print(x - y)  # 7  (Subtraction)
print(x * y)  # 30 (Multiplication)
print(x / y)  # 3.333... (Division)
print(x // y) # 3 (Floor Division)
print(x % y)  # 1 (Modulus / Remainder)
print(x ** y) # 1000 (Exponentiation)
```

---

### 3. Comparison Operators
Used to compare values (result is `True` or `False`).  

```python
x = 5
y = 10

print(x == y)  # False (Equal to)
print(x != y)  # True  (Not equal to)
print(x > y)   # False (Greater than)
print(x < y)   # True  (Less than)
print(x >= 5)  # True  (Greater or equal)
print(y <= 10) # True  (Less or equal)
```

---

### 4. Logical Operators
Used to combine conditional statements.  

```python
a = True
b = False

print(a and b) # False (Both must be True)
print(a or b)  # True  (At least one True)
print(not a)   # False (Negation)
```

---

### 5. Assignment Operators
Used to assign values to variables.  

```python
x = 10
x += 5   # same as x = x + 5
print(x) # 15

x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x /= 4   # x = x / 4 → 6.0
x %= 4   # x = x % 4 → 2.0
x **= 3  # x = x ** 3 → 8.0
```

---

### 6. Bitwise Operators
Work on binary (bit-level) data.  

```python
x = 6   # 110 in binary
y = 3   # 011 in binary

print(x & y)  # 2 (AND → 010)
print(x | y)  # 7 (OR  → 111)
print(x ^ y)  # 5 (XOR → 101)
print(~x)     # -7 (NOT → flips bits)
print(x << 1) # 12 (Left shift → 1100)
print(x >> 1) # 3  (Right shift → 011)
```

---

### 7. Membership Operators
Used to test if a value exists in a sequence.  

```python
fruits = ["apple", "banana"]

print("apple" in fruits)   # True
print("orange" not in fruits) # True
```

---

### 8. Identity Operators
Used to compare object references (memory addresses).  

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)     # False (different objects, same content)
print(a == b)     # True  (same values)
print(a is c)     # True  (same object reference)
```

---

### 9. Operator Precedence
Some operators are evaluated before others (like in math).  

Order of precedence (highest to lowest):  
1. `()` → Parentheses  
2. `**` → Exponent  
3. `*`, `/`, `//`, `%` → Multiplication/division  
4. `+`, `-` → Addition/subtraction  
5. Comparison (`==`, `<`, `>`, etc.)  
6. Logical (`not`, `and`, `or`)  

Example:

```python
result = 2 + 3 * 4
print(result)  # 14, because multiplication happens before addition
```

---

### 10. Next Steps
✅ You now know how to use Python’s operators: arithmetic, comparison, logical, assignment, bitwise, membership, and identity.  
In the next chapter, we’ll explore **working with strings** in detail.