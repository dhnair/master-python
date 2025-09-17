# Volume 1: Foundations
## Chapter 33: The range() Function

### 1. Introduction
The `range()` function is commonly used in **for loops** to generate a sequence of numbers.  
It doesn’t actually create a full list in memory but instead produces numbers on demand, making it efficient.  

---

### 2. Basic Usage
`range(stop)` generates numbers from **0 up to stop (exclusive)**.

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

---

### 3. Specifying Start and Stop
You can also give a starting value:

```python
for i in range(2, 6):
    print(i)
```

Output:
```
2
3
4
5
```

---

### 4. Using Step
The third parameter is the **step** (increment).

```python
for i in range(0, 10, 2):
    print(i)
```

Output:
```
0
2
4
6
8
```

---

### 5. Negative Steps
You can loop backwards with a negative step.

```python
for i in range(10, 0, -2):
    print(i)
```

Output:
```
10
8
6
4
2
```

---

### 6. Using range() Outside of Loops
You can convert a range to a list or tuple:

```python
print(list(range(5)))   # [0, 1, 2, 3, 4]
print(tuple(range(3)))  # (0, 1, 2)
```

---

### 7. Checking Membership in range
You can check if a number is inside a range:

```python
print(5 in range(10))    # True
print(15 in range(10))   # False
```

---

### 8. Large Ranges are Efficient
Even huge ranges don’t take up memory:

```python
r = range(1, 1_000_000)
print(len(r))     # 999999
print(r[100])     # 101
```

⚡ The values are generated on demand.  

---

### 9. Common Mistakes
- Forgetting that the **stop value is excluded**:
  ```python
  for i in range(5):
      print(i)
  # Outputs 0–4, not 0–5
  ```
- Using the wrong step (causes empty loops):
  ```python
  for i in range(5, 0, 1):  # ❌ won't run
      print(i)
  # Step should be -1 if going down
  ```

---

### 10. Practical Examples
- Printing even numbers:
```python
for i in range(0, 11, 2):
    print(i)
```

- Countdown:
```python
for i in range(5, 0, -1):
    print(i)
print("Go!")
```

---

### 11. Next Steps
✅ You now understand how to use `range()` with start, stop, and step values.  
In the next chapter, we’ll look at **loop control statements** like `break`, `continue`, and `pass`.