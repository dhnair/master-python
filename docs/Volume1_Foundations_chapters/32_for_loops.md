# Volume 1: Foundations
## Chapter 32: for Loops

### 1. Introduction
A **for loop** is used to iterate over a sequence of items (like a list, string, or range).  
It is the most common looping construct in Python when you know the number of iterations in advance.  

---

### 2. Basic for Loop
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

---

### 3. Iterating Over Strings
Strings are sequences, so you can loop through characters:

```python
for char in "Python":
    print(char)
```

---

### 4. Using the range() Function
`range()` generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

You can specify start, stop, and step:

```python
for i in range(2, 10, 2):
    print(i)   # 2, 4, 6, 8
```

---

### 5. Looping with Index and Value
Use `enumerate()` when you need both index and value.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

### 6. Nested for Loops
```python
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

### 7. Using else with for
The `else` block runs if the loop finishes normally (not broken).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

---

### 8. Breaking Out of Loops
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### 9. Skipping Iterations with continue
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:
```
0
1
3
4
```

---

### 10. Practical Examples
- Summing numbers:
```python
total = 0
for i in range(1, 6):
    total += i
print("Sum =", total)
```

- Iterating over a dictionary:
```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, "=", value)
```

---

### 11. When to Use for Loops
- Iterating over lists, strings, or dictionaries.  
- When you know or can define the range of iterations.  
- For cleaner, more readable code compared to while loops.  

---

### 12. Next Steps
✅ You now understand for loops and how to iterate over sequences.  
In the next chapter, we’ll explore the **range() function** in more detail.