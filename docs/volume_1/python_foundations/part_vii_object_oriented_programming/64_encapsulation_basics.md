# Chapter 64: Encapsulation Basics

## 1. Introduction
Encapsulation is about restricting access to certain data or methods in a class.  
Python uses naming conventions instead of strict enforcement.

---

## 2. Public Attributes
Accessible everywhere.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)
```

---

## 3. Protected Attributes
Prefix with `_` (convention: treat as internal use).

```python
class Person:
    def __init__(self, name):
        self._name = name

p = Person("Bob")
print(p._name)  # accessible but discouraged
```

---

## 4. Private Attributes
Prefix with `__` triggers name mangling.

```python
class Person:
    def __init__(self, name):
        self.__name = name

p = Person("Eve")
# print(p.__name)  # ❌ AttributeError
print(p._Person__name)  # still accessible
```

---

## 5. Getters and Setters
Control access with methods.

```python
class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
```

---

## 6. Using @property
```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value

p = Person(20)
p.age = 30
print(p.age)
```

---

## 7. Next Steps
✅ You now understand encapsulation basics.  
Next: **Mini project — Student and Course Manager**.
