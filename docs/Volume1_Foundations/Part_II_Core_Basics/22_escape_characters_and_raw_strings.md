# Chapter 22: Escape Characters and Raw Strings

## 1. Introduction
Sometimes you need special characters inside strings, like a newline or a tab.  
Python uses **escape sequences** to represent these characters.  
A **raw string** can be used when you want to ignore escape sequences.  

---

## 2. What is an Escape Character?
- An escape character starts with a **backslash (`\`)**.  
- It tells Python to treat the next character in a special way.  

---

## 3. Common Escape Sequences
```python
print("Hello\nWorld")   # Newline
print("Hello\tWorld")   # Tab
print("She said \"Hi\"") # Double quotes inside string
print('It\'s Python')   # Single quote inside string
print("C:\\Users\\Name") # Backslash itself
```

Output:
```
Hello
World
Hello   World
She said "Hi"
It's Python
C:\Users\Name
```

---

## 4. Multiline Strings
You can also use triple quotes (`"""` or `'''`) to handle multi-line text without needing `\n`:

```python
text = """Line one
Line two
Line three"""
print(text)
```

---

## 5. Unicode and Special Characters
Python strings support Unicode.  
You can include characters using escape sequences:

```python
print("\u03C0")  # π (Greek letter pi)
print("\u00A9")  # © symbol
```

---

## 6. Raw Strings
- A raw string is created by prefixing with `r` or `R`.  
- Escape sequences inside raw strings are not processed.  

```python
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents
```

Without `r`:

```python
path = "C:\Users\Name\Documents"
print(path)  # Error or unexpected result
```

---

## 7. When to Use Raw Strings
- File paths in Windows (`C:\...`).  
- Regular expressions (`\d`, `\s`, etc.).  
- Any time you want Python to treat backslashes literally.  

---

## 8. Common Mistakes
- Forgetting to escape backslashes:  
  ```python
  print("C:\new_folder")   # Error or unwanted behavior
  ```
  Better:
  ```python
  print("C:\\new_folder")  # Escaped backslash
  print(r"C:\new_folder")  # Raw string
  ```

---

## 9. Next Steps
✅ You now understand escape characters and raw strings.  
In the next chapter, we’ll dive into **lists**, one of Python’s most versatile data types.