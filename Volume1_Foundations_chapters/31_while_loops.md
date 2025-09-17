# Volume 1: Foundations
## Chapter 31: while Loops

### 1. Introduction
A **while loop** is used to repeat a block of code as long as a condition is true.  
It is useful when you don’t know in advance how many times to repeat an action.  

---

### 2. Basic while Loop
```python
count = 1

while count <= 5:
    print("Count:", count)
    count += 1
```

Output:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

---

### 3. Infinite Loops
If the condition never becomes false, the loop runs forever.

```python
while True:
    print("This will run forever")
```

⚠️ Stop infinite loops with **Ctrl + C** in terminal.  

---

### 4. Using a Break Condition
Always ensure there’s a way for the loop to end.

```python
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
```

---

### 5. Using else with while
The `else` block runs when the loop ends normally (not by `break`).

```python
x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print("Loop finished successfully")
```

Output:
```
1
2
3
Loop finished successfully
```

---

### 6. Nested while Loops
You can put a while loop inside another while loop.

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

### 7. Common Mistakes
- Forgetting to update the loop variable → infinite loop.  
- Using `=` instead of `==` in the condition.  
- Forgetting the colon (`:`) after the condition.  

---

### 8. Practical Examples
- Countdown timer:

```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
```

- Input validation:

```python
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted")
```

---

### 9. When to Use while Loops
- When the number of iterations is **unknown** ahead of time.  
- For waiting on user input, file availability, or network events.  
- For loops that depend on conditions instead of a fixed range.  

---

### 10. Next Steps
✅ You now know how to use while loops, avoid infinite loops, and apply break/else.  
In the next chapter, we’ll explore **for loops**, which are often used when the number of iterations is known.