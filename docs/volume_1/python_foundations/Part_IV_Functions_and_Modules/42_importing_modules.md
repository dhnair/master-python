# Chapter 42: Importing Modules

## 1. Introduction
Modules are Python files containing reusable code (functions, classes, variables).  
You can import them into your program using the `import` statement.

---

## 2. Importing a Whole Module
```python
import math
print(math.sqrt(16))  # 4.0
```

---

## 3. Importing Specific Items
```python
from math import pi, sqrt
print(pi)      # 3.14159...
print(sqrt(25)) # 5.0
```

---

## 4. Using Aliases
```python
import numpy as np
print(np.array([1,2,3]))
```

---

## 5. Importing All Items (Not Recommended)
```python
from math import *
print(sin(0))
```
⚠️ Can cause name conflicts.

---

## 6. Importing Custom Modules
If you have a file `mymath.py`:

```python
# mymath.py
def square(x): return x*x
```

Use it in another script:

```python
import mymath
print(mymath.square(5))
```

---

## 7. Reloading Modules
Sometimes you need to reload a module (during development).

```python
import importlib, mymath
importlib.reload(mymath)
```

---

## 8. Next Steps
✅ You now know how to import modules.  
In the next chapter, we’ll learn about **creating your own modules**.
