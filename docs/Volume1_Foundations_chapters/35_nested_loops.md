# Volume 1: Foundations
## Chapter 35: Nested Loops

### 1. Introduction
A **nested loop** is a loop inside another loop.  
They are useful when working with multi-dimensional data (like matrices), comparing items from two collections, or performing repeated tasks across multiple dimensions.

---

### 2. Basic Nested for Loop
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

Output:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

---

### 3. Nested while Loops
```python
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

---

### 4. Mixed Loops (for + while)
```python
for char in ["A", "B"]:
    i = 0
    while i < 2:
        print(char, i)
        i += 1
```

---

### 5. Nested Loops with Lists (Matrices)
```python
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value)
```

Output:
```
1
2
3
4
5
6
```

---

### 6. Using break and continue in Nested Loops
`break` exits the innermost loop; `continue` skips to the next iteration of the innermost loop.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # stops inner loop only
        print(i, j)
```

---

### 7. Practical Example — Multiplication Table
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

Output:
```
1 2 3 
2 4 6 
3 6 9 
```

---

### 8. Performance Considerations
Nested loops increase time complexity multiplicatively (e.g., O(n*m) or O(n^2) for two nested loops of size n). For large inputs, consider algorithmic improvements or using libraries (NumPy, itertools).

---

### 9. Common Mistakes and Tips
- Forgetting to reset inner-loop counters in `while` loops.  
- Excessive nesting → harder to read and maintain. Break logic into functions when nesting gets deep.  
- Remember to maintain correct indentation.  

---

### 10. Next Steps
✅ You now understand nested loops and how to use them effectively.  
Next chapter: **Comprehensions**, a concise way to create collections in Python.
