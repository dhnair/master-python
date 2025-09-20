# Chapter 43: Creating Your Own Modules

## 1. Introduction
A **module** is just a Python file with functions, variables, or classes.  
Creating your own modules helps organize code.

---

## 2. Creating a Module
1. Create a file `mymath.py`:
```python
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
```

2. Use it in another file:
```python
import mymath
print(mymath.add(2,3))
```

---

## 3. Module Search Path
Python looks for modules in:
- Current directory  
- PYTHONPATH environment variable  
- Standard library path  

```python
import sys
print(sys.path)
```

---

## 4. Organizing with Packages
A **package** is a directory with an `__init__.py` file.  
Example structure:
```
mypackage/
    __init__.py
    module1.py
    module2.py
```

Use:
```python
from mypackage import module1
```

---

## 5. Best Practices
- Use lowercase filenames.  
- Group related functions in one module.  
- Keep modules small and focused.  

---

## 6. Next Steps
✅ You now know how to create your own modules.  
In the next chapter, we’ll revisit **virtual environments**.
