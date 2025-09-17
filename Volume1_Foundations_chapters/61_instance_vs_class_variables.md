# Volume 1: Foundations
## Chapter 61: Instance vs Class Variables

### 1. Introduction
Python classes can define two types of variables:  
- **Instance variables** → unique to each object.  
- **Class variables** → shared across all objects.  

---

### 2. Instance Variables
Defined inside `__init__` and tied to `self`.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # instance variable

d1 = Dog("Buddy")
d2 = Dog("Max")
print(d1.name, d2.name)
```

Output:
```
Buddy Max
```

---

### 3. Class Variables
Defined outside methods, shared by all objects.

```python
class Dog:
    species = "Canine"  # class variable
    def __init__(self, name):
        self.name = name

d1 = Dog("Buddy")
d2 = Dog("Max")
print(d1.species, d2.species)
```

Output:
```
Canine Canine
```

---

### 4. Modifying Instance vs Class Variables
```python
d1.species = "Wolf"  # creates new instance variable
print(d1.species, d2.species)  # Wolf Canine

Dog.species = "Wolf"  # modifies class variable
print(d1.species, d2.species)  # Wolf Wolf
```

---

### 5. Best Practices
- Use instance variables for object-specific data.  
- Use class variables for constants or shared defaults.  

---

### 6. Next Steps
✅ You now understand instance vs class variables.  
Next: **Methods and behaviors**.
