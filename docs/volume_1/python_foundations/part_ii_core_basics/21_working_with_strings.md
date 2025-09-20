# Chapter 21: Working with Strings

## 1. Introduction
Strings are one of the most commonly used data types in Python.  
They represent sequences of characters and are used for storing text.  

---

## 2. Creating Strings
Strings can be created with single quotes, double quotes, or triple quotes:

```python
s1 = 'Hello'
s2 = "World"
s3 = """This is
a multi-line string."""
```

---

## 3. Accessing Characters
Strings are sequences, so you can access characters using indexes:

```python
word = "Python"
print(word[0])   # P
print(word[-1])  # n (last character)
```

---

## 4. String Slicing
You can extract substrings using slices:

```python
word = "Python"
print(word[0:3])   # Pyt
print(word[2:])    # thon
print(word[:4])    # Pyth
print(word[-3:])   # hon
```

---

## 5. Common String Operations
- Concatenation:

```python
print("Hello " + "World")  # Hello World
```

- Repetition:

```python
print("Hi! " * 3)  # Hi! Hi! Hi!
```

- Length:

```python
print(len("Python"))  # 6
```

---

## 6. Useful String Methods
```python
text = "  python programming  "

print(text.upper())    # "  PYTHON PROGRAMMING  "
print(text.lower())    # "  python programming  "
print(text.strip())    # "python programming"
print(text.replace("python", "java"))  # "  java programming  "
print(text.split())    # ['python', 'programming']
print("-".join(["a", "b", "c"]))       # "a-b-c"
```

---

## 7. String Searching
```python
sentence = "Learning Python is fun"
print("Python" in sentence)     # True
print(sentence.find("Python"))  # 9 (index where found)
```

---

## 8. Escape Sequences
Special characters can be written with a backslash:

```python
print("Line1\nLine2")   # newline
print("Hello\tWorld")   # tab
print("She said \"Hi\"") # quotes inside string
```

---

## 9. f-Strings (String Interpolation)
Introduced in Python 3.6+, f-strings allow inserting variables directly:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

## 10. Raw Strings
Useful for paths and regular expressions:

```python
path = r"C:\Users\Name\Documents"
print(path)  # C:\Users\Name\Documents
```

---

## 11. Next Steps
✅ You now know how to work with strings: indexing, slicing, methods, and formatting.  
In the next chapter, we’ll cover **escape characters and raw strings** in more detail.