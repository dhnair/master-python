# Chapter 34: Loop Control (break, continue, pass)

## 1. Introduction
Python provides special statements to control the flow of loops:  
- `break` → exits the loop early  
- `continue` → skips the current iteration  
- `pass` → does nothing (placeholder)  

These give you more fine-grained control over loop execution.  

---

## 2. The break Statement
`break` stops the loop entirely, even if the condition is still true.

```python
for i in range(10):
    if i == 5:
        break
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

## 3. The continue Statement
`continue` skips the rest of the current iteration and goes to the next one.

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

## 4. The pass Statement
`pass` is a placeholder that does nothing.  
It is useful when you need a syntactically valid block but don’t want to add code yet.

```python
for i in range(3):
    if i == 1:
        pass  # do nothing
    print("i =", i)
```

---

## 5. break in while Loops
```python
x = 0
while True:
    print(x)
    x += 1
    if x > 3:
        break
```

---

## 6. continue in while Loops
```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

Output:
```
1
2
4
5
```

---

## 7. Nested Loops with break
`break` only exits the **innermost** loop.

```python
for i in range(2):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

Output:
```
0 0
1 0
```

---

## 8. Practical Examples
- **Finding a number in a list**:
```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 5:
        print("Found 5!")
        break
```

- **Skipping odd numbers**:
```python
for i in range(1, 6):
    if i % 2 != 0:
        continue
    print(i)
```

---

## 9. Common Mistakes
- Using `break` when you only meant to skip an iteration (use `continue`).  
- Overusing `pass` instead of writing meaningful code.  
- Forgetting that `break` only exits the current loop, not all loops.  

---

## 10. Next Steps
✅ You now understand how to use `break`, `continue`, and `pass` to control loop behavior.  
In the next chapter, we’ll explore **nested loops** and how to work with loops inside loops effectively.