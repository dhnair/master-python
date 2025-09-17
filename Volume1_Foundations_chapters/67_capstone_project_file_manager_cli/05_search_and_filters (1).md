# Capstone Project: File Manager CLI
## Chapter 5: Search and Filters

### 1. Introduction
A file manager should support **searching files** by name, extension, or size.  

---

### 2. Searching by Name
```python
def search_by_name(path, name):
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                print(os.path.join(root, file))
```

---

### 3. Filtering by Extension
```python
def search_by_extension(path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
```

---

### 4. Filtering by Size
```python
def search_by_size(path, min_size):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) >= min_size:
                print(file_path)
```

---

### 5. Integrating with CLI
```python
if args.command == "search":
    search_by_name(".", args.path)
```

---

### 6. Next Steps
✅ We can now search and filter files.  
Next: **Error handling** to make the program more robust.
