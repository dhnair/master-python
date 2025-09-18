# Chapter 63: Basic Inheritance

## 1. Introduction
Inheritance allows a class (child) to reuse code from another class (parent).

---

## 2. Simple Inheritance
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()
```

---

## 3. Accessing Parent Methods
Use `super()`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Beagle")
print(dog.name, dog.breed)
```

---

## 4. Method Resolution Order (MRO)
Python supports multiple inheritance; MRO decides which method to call.

```python
print(Dog.__mro__)
```

---

## 5. Best Practices
- Inherit when classes are logically related.  
- Prefer composition (has-a) if inheritance doesn’t fit well.  

---

## 6. Next Steps
✅ You now understand inheritance.  
Next: **Encapsulation basics**.
