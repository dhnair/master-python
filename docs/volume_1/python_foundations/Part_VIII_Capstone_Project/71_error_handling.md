# Chapter 71: Error Handling

## 1. Introduction
Robust programs handle errors gracefully.  
Our File Manager should never crash due to missing files or permission issues.

---

## 2. Handling Missing Files
```python
def safe_delete(path):
    try:
        os.remove(path)
        print("Deleted", path)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
```

---

## 3. Wrapping File Operations
All file/directory operations should be wrapped in try/except.

```python
def safe_read(path):
    try:
        with open(path) as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("Cannot decode file")
```

---

## 4. CLI Integration
```python
if args.command == "delete":
    safe_delete(args.path)
elif args.command == "read":
    safe_read(args.path)
```

---

## 5. Best Practices
- Catch specific exceptions first.  
- Provide clear error messages.  
- Use logging in larger projects.  

---

## 6. Next Steps
✅ Our program is now more robust.  
Next: **Refactor with OOP** for better design.
