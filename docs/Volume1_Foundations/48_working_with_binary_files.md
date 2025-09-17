# Volume 1: Foundations
## Chapter 48: Working with Binary Files

### 1. Introduction
Text files store characters, but binary files store bytes. Examples include images, executables, and audio files.

---

### 2. Reading Binary Files
```python
with open("image.jpg", "rb") as f:
    data = f.read()
    print(len(data), "bytes")
```

---

### 3. Writing Binary Files
```python
with open("copy.jpg", "wb") as f:
    f.write(data)
```

---

### 4. Copying Files
```python
with open("image.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dst:
        dst.write(src.read())
```

---

### 5. When to Use Binary Mode
- Images  
- Audio files  
- Pickled objects  
- Any non-text data

---

### 6. Next Steps
✅ You now know how to work with binary files.  
Next: **Using context managers**.
