# Volume 1: Foundations
## Chapter 60: The __init__ Constructor

### 1. Introduction
The `__init__` method is a special constructor in Python classes.  
It runs automatically when a new object is created.

---

### 2. Basic Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name, p.age)
```

---

### 3. Default Values
```python
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p = Person("Bob")
print(p.name, p.age)  # Bob 18
```

---

### 4. Why Use __init__?
- Initialize attributes.  
- Set default states.  
- Validate input during object creation.  

---

### 5. Best Practices
- Keep `__init__` simple.  
- Don’t overload it with logic — use helper methods.  

---

### 6. Next Steps
✅ You now understand the `__init__` constructor.  
Next: **Instance vs class variables**.
