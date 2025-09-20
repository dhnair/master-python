# Chapter 58: What is Object-Oriented Programming (OOP)?

## 1. Introduction
Object-Oriented Programming (OOP) is a paradigm based on "objects".  
Objects combine **data** (attributes) and **behavior** (methods).

---

## 2. Why OOP?
- Encapsulation: group data + functions.  
- Reusability: write once, reuse with inheritance.  
- Abstraction: hide complexity.  
- Modularity: divide large programs into manageable parts.  

---

## 3. Classes and Objects
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says woof!")

my_dog = Dog("Buddy")
my_dog.bark()
```

---

## 4. OOP Terminology
- **Class** → blueprint.  
- **Object (instance)** → created from class.  
- **Attributes** → variables inside objects.  
- **Methods** → functions inside objects.  

---

## 5. Procedural vs OOP
- Procedural → functions and data separate.  
- OOP → functions + data bundled together.  

---

## 6. Next Steps
✅ You now understand the basics of OOP.  
Next: **Creating classes and objects**.
