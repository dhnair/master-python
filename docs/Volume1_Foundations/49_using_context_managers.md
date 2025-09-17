# Volume 1: Foundations
## Chapter 49: Using Context Managers

### 1. Introduction
Context managers handle setup and cleanup automatically. The most common use is file handling with `with`.

---

### 2. Basic Example
```python
with open("example.txt", "r") as f:
    data = f.read()
print("File closed?", f.closed)
```

---

### 3. Custom Context Managers
Create your own with a class implementing `__enter__` and `__exit__`.

```python
class MyResource:
    def __enter__(self):
        print("Resource acquired")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")

with MyResource() as r:
    print("Using resource")
```

---

### 4. Contextlib Module
Simplify creation with `contextlib`.

```python
from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Start")
    yield
    print("End")

with simple_manager():
    print("Inside block")
```

---

### 5. Benefits
- Automatic cleanup  
- Cleaner code  
- Error safety

---

### 6. Next Steps
✅ You now understand context managers.  
Next: **Handling exceptions**.
