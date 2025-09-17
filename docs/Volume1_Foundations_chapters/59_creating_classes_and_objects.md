# Volume 1: Foundations
## Chapter 59: Creating Classes and Objects

### 1. Introduction
In Python, classes define the structure of objects. Objects are instances of classes.

---

### 2. Creating a Class
```python
class Car:
    def drive(self):
        print("The car is moving")
```

---

### 3. Creating Objects
```python
my_car = Car()
my_car.drive()
```

---

### 4. Adding Attributes
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Corolla")
print(car.brand, car.model)
```

---

### 5. Multiple Objects
```python
car1 = Car("Ford", "Fiesta")
car2 = Car("Tesla", "Model 3")
print(car1.brand, car2.brand)
```

---

### 6. Next Steps
✅ You now know how to create classes and objects.  
Next: **The `__init__` constructor**.
