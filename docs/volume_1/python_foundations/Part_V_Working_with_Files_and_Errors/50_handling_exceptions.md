# Chapter 50: Handling Exceptions

## 1. Introduction
Exceptions are errors that occur during execution. Python provides `try`/`except` blocks to handle them gracefully.

---

## 2. Basic try-except
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 3. Multiple Except Clauses
```python
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Division error")
```

---

## 4. Catching Any Exception
```python
try:
    risky_code()
except Exception as e:
    print("Error:", e)
```

---

## 5. Using else with try
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)
```

---

## 6. Finally Block
```python
try:
    file = open("example.txt")
finally:
    file.close()
```

---

## 7. Best Practices
- Catch specific exceptions first.  
- Avoid bare `except:` unless necessary.  
- Clean up resources with `finally` or context managers.

---

## 8. Next Steps
✅ You now understand exception handling.  
Next: **Using finally and else** in more detail.
