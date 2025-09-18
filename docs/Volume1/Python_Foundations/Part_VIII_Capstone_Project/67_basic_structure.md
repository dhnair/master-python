# Chapter 67: Basic Structure

## 1. Introduction
Before adding file operations, we need a **skeleton CLI structure**.  
This will allow the program to accept commands and arguments from the terminal.

---

## 2. Using argparse
We’ll use Python’s `argparse` library for handling command-line arguments.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="File Manager CLI")
    parser.add_argument("command", help="Command to run (list, create, delete, etc.)")
    parser.add_argument("path", nargs="?", help="Target file or directory")

    args = parser.parse_args()
    print("Command:", args.command)
    print("Path:", args.path)

if __name__ == "__main__":
    main()
```

Run from terminal:
```bash
python file_manager.py list .
```

Output:
```
Command: list
Path: .
```

---

## 3. Project Structure
```
capstone_file_manager/
    file_manager.py
```

---

## 4. Next Steps
✅ Now we have a basic CLI structure that accepts commands.  
Next: **Implementing file operations** (read, write, delete).
