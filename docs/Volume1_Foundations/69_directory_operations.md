# Capstone Project: File Manager CLI
## Chapter 69: Directory Operations

### 1. Introduction
Directories organize files. Our CLI should allow:  
- Creating directories  
- Listing contents  
- Navigating paths  

---

### 2. Creating Directories
```python
import os

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory created")
    except Exception as e:
        print("Error:", e)
```

---

### 3. Listing Contents
```python
def list_directory(path):
    try:
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print("Directory not found")
```

---

### 4. Getting Current Working Directory
```python
print("Current directory:", os.getcwd())
```

---

### 5. Changing Directory (optional)
```python
os.chdir("..")
print("Now in:", os.getcwd())
```

---

### 6. Integrating with CLI
```python
if args.command == "list":
    list_directory(args.path or ".")
elif args.command == "mkdir":
    create_directory(args.path)
```

---

### 7. Next Steps
✅ Directory operations are working.  
Next: **Search and filters** for files.
