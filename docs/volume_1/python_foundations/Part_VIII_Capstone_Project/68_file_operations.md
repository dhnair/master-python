# Chapter 68: File Operations

## 1. Introduction
File operations are core to any file manager.  
We’ll implement **read, write, delete, copy, and move**.

---

## 2. Reading a File
```python
def read_file(path):
    try:
        with open(path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
```

---

## 3. Writing to a File
```python
def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print("File written successfully")
```

---

## 4. Deleting a File
```python
import os

def delete_file(path):
    try:
        os.remove(path)
        print("File deleted")
    except FileNotFoundError:
        print("File not found")
```

---

## 5. Copying and Moving Files
```python
import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)
    print("File copied")

def move_file(src, dst):
    shutil.move(src, dst)
    print("File moved")
```

---

## 6. Integrating with CLI
```python
if args.command == "read":
    read_file(args.path)
elif args.command == "write":
    write_file(args.path, "Hello World")
elif args.command == "delete":
    delete_file(args.path)
```

---

## 7. Next Steps
✅ File operations are implemented.  
Next: **Directory operations** (create, list, navigate).
