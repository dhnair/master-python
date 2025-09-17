# Capstone Project: File Manager CLI
## Chapter 7: Refactoring with OOP

### 1. Introduction
So far, our program has procedural functions.  
We will now refactor it into a **FileManager class**.

---

### 2. Creating FileManager Class
```python
import os, shutil

class FileManager:
    def __init__(self, base_dir="."):
        self.base_dir = base_dir

    def list(self, path="."):
        try:
            for item in os.listdir(path):
                print(item)
        except Exception as e:
            print("Error:", e)

    def read(self, path):
        try:
            with open(path) as f:
                print(f.read())
        except Exception as e:
            print("Error:", e)
```

---

### 3. Adding More Methods
```python
    def write(self, path, content):
        with open(path, "w") as f:
            f.write(content)
        print("Written to", path)

    def delete(self, path):
        try:
            os.remove(path)
            print("Deleted", path)
        except Exception as e:
            print("Error:", e)
```

---

### 4. Using the Class in CLI
```python
fm = FileManager()

if args.command == "list":
    fm.list(args.path or ".")
elif args.command == "read":
    fm.read(args.path)
```

---

### 5. Benefits of OOP Refactor
- Cleaner code.  
- Encapsulation of related functions.  
- Easier to extend.  

---

### 6. Next Steps
✅ We now use OOP for file management.  
Next: **Enhancements** to make it more user-friendly.
