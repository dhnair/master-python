# Chapter 46: Reading Text Files

## 1. Introduction
Python provides built-in tools to read text files. Reading files is essential for working with stored data.

---

## 2. Opening a File
Use `open()` with mode `'r'` (read).

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

---

## 3. Using with Statement
Always use `with` for automatic closing.

```python
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 4. Reading Line by Line
```python
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

## 5. readlines() Method
```python
with open("example.txt") as f:
    lines = f.readlines()
print(lines)
```

---

## 6. readline() Method
```python
with open("example.txt") as f:
    line = f.readline()
    print(line)
```

---

## 7. Handling File Not Found
```python
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

---

## 8. Next Steps
✅ You now know how to read text files.  
Next: **Writing text files**.
