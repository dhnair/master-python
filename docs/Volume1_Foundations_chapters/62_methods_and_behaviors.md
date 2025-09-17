# Volume 1: Foundations
## Chapter 62: Methods and Behaviors

### 1. Introduction
Methods define behaviors of objects. They are functions defined inside a class.  

---

### 2. Instance Methods
The most common method type. Always include `self`.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name, "says woof!")

dog = Dog("Buddy")
dog.bark()
```

---

### 3. Class Methods
Operate on the class itself, not instances. Use `@classmethod`.

```python
class Dog:
    count = 0
    def __init__(self, name):
        Dog.count += 1
    @classmethod
    def get_count(cls):
        return cls.count

print(Dog.get_count())
```

---

### 4. Static Methods
Behave like regular functions but live in class namespace. Use `@staticmethod`.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))
```

---

### 5. Special Methods
Python classes can override built-ins like `__str__`, `__len__`.

```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p)
```

---

### 6. Next Steps
✅ You now know about instance, class, static, and special methods.  
Next: **Basic inheritance**.
