# Volume 1: Foundations
## Chapter 13: Understanding Python Scripts vs Modules

### 1. Introduction
In Python, you will often hear the terms **script** and **module**.  
They are both Python files, but they serve slightly different purposes.  
Understanding this difference is important when you start organizing larger projects.  

---

### 2. What is a Script?
- A **script** is a Python file meant to be run directly.  
- It usually performs a specific task when executed.  
- Example: `hello.py`  

```python
print("Hello, this is a script!")
```

Run it from the command line:

```bash
python3 hello.py
```

Output:

```
Hello, this is a script!
```

---

### 3. What is a Module?
- A **module** is a Python file that provides functions, classes, or variables for other Python files to use.  
- Instead of running it directly, you **import** it.  

Example: `mymath.py`

```python
def add(a, b):
    return a + b
```

Use it in another file `test.py`:

```python
import mymath
print(mymath.add(2, 3))
```

Output:

```
5
```

---

### 4. Using `__name__ == "__main__"`
Sometimes a file can act as **both a script and a module**.  
This is done using the special variable `__name__`.

Example: `dual.py`

```python
def greet(name):
    print("Hello,", name)

if __name__ == "__main__":
    # This runs only if the file is executed directly
    greet("World")
```

- Run directly:  

```bash
python3 dual.py
```

Output:  

```
Hello, World
```

- Import as module:

```python
import dual
dual.greet("Alice")
```

Output:  

```
Hello, Alice
```

---

### 5. Built-in Modules
Python comes with many built-in modules.  
Example:

```python
import math
print(math.sqrt(16))
```

Output:

```
4.0
```

---

### 6. Creating Your Own Modules
- Any `.py` file can be a module.  
- Keep related functions together in one file.  
- Example: `geometry.py` for shapes, `strings.py` for text utilities.  
- You can import them into any script in the same directory.  

---

### 7. Why the Distinction Matters
- **Scripts** → run tasks.  
- **Modules** → provide reusable code.  
- Understanding this distinction helps organize code into **projects** with many files.  

---

### 8. Next Steps
✅ You now understand the difference between Python scripts and modules.  
In the next chapter, we’ll cover **debugging basics** to help you fix errors in your programs.