# Chapter 51: Using finally and else

## 1. Introduction
Python's `try` statement can include optional `else` and `finally` blocks:  
- `else` runs if no exception occurs.  
- `finally` always runs, regardless of whether an exception occurs.  

---

## 2. Using else
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division by zero")
else:
    print("No error, result =", x)
```

---

## 3. Using finally
```python
try:
    f = open("example.txt", "w")
    f.write("Hello")
finally:
    f.close()
    print("File closed")
```

---

## 4. Combining else and finally
```python
try:
    x = int("42")
except ValueError:
    print("Invalid number")
else:
    print("Conversion succeeded:", x)
finally:
    print("Done processing")
```

---

## 5. Why Use else?
Keeps success-path logic separate from error handling.

---

## 6. Why Use finally?
Guarantees cleanup (e.g., closing files, releasing resources).

---

## 7. Next Steps
✅ You now understand how to use `else` and `finally` in exception handling.  
Next: **Common built-in exceptions**.
