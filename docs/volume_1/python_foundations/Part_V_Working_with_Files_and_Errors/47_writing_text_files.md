# Chapter 47: Writing Text Files

## 1. Introduction
Writing to files allows saving output for later use. Python uses `open()` with different modes.

---

## 2. Writing with 'w' Mode
Overwrites existing content or creates new file.

```python
with open("output.txt", "w") as f:
    f.write("Hello, file!")
```

---

## 3. Appending with 'a' Mode
Adds content to end of file.

```python
with open("output.txt", "a") as f:
    f.write("\nAnother line")
```

---

## 4. Writing Multiple Lines
```python
lines = ["First line\n", "Second line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

---

## 5. Ensuring Flush and Close
Files are closed automatically when using `with`.  
Otherwise, call `f.close()` manually.

---

## 6. Handling Encoding
```python
with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("Olá, mundo!")
```

---

## 7. Next Steps
✅ You now know how to write to files.  
Next: **Working with binary files**.
