# Chapter 30: Nested Conditionals

## 1. Introduction
A **nested conditional** is an `if` statement inside another `if`.  
They let you check conditions within conditions, useful when decisions depend on multiple factors.  

---

## 2. Basic Nested if
```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

---

## 3. Nested if-else
```python
x = 15

if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not a positive number")
```

---

## 4. Multiple Levels of Nesting
You can nest deeper, but code becomes harder to read.

```python
x = 12

if x > 0:
    if x < 20:
        if x % 3 == 0:
            print("Positive number < 20 and divisible by 3")
```

---

## 5. Combining Conditions Instead
Often you can avoid deep nesting with logical operators.

❌ Nested:
```python
if age >= 18:
    if has_ticket:
        print("Welcome")
```

✅ Better:
```python
if age >= 18 and has_ticket:
    print("Welcome")
```

---

## 6. When Nested Conditionals are Useful
- Complex decision-making where one condition depends on another.  
- Validating multiple layers of requirements (e.g., login + role check).  
- When clarity is better served by nesting than by a long combined condition.  

---

## 7. Common Mistakes
- Too many nested levels → code becomes unreadable.  
- Forgetting to properly indent nested blocks.  
- Overusing nesting where `elif` or logical operators would be simpler.  

---

## 8. Practical Example
```python
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

---

## 9. Best Practices
- Limit nesting to 2–3 levels maximum.  
- Refactor deeply nested conditionals into functions.  
- Use `elif` or compound conditions for clarity when possible.  

---

## 10. Next Steps
✅ You now understand nested conditionals and when to use them.  
In the next chapter, we’ll explore **while loops**, which allow repeating actions while a condition is true.