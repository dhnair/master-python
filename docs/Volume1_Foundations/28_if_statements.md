# Chapter 28: if Statements

## 1. Introduction
The **if statement** is used to make decisions in Python.  
It allows your program to execute certain code only if a condition is true.  

---

## 2. Basic if Statement
```python
age = 18

if age >= 18:
    print("You are an adult")
```

Output:
```
You are an adult
```

---

## 3. Indentation Matters
Python uses **indentation** (spaces) to define blocks of code.  

❌ Wrong:
```python
if True:
print("Hello")   # Error: expected an indented block
```

✅ Correct:
```python
if True:
    print("Hello")
```

---

## 4. Using Comparison Operators in if
```python
temperature = 25

if temperature > 30:
    print("It's hot!")
if temperature < 10:
    print("It's cold!")
if temperature == 25:
    print("Perfect weather!")
```

---

## 5. if with Boolean Variables
```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")
```

---

## 6. if with Expressions
Any expression that evaluates to `True` or `False` can be used:

```python
name = "Alice"

if name:   # non-empty strings are True
    print("Name provided")
```

---

## 7. Nested if Statements
You can put an `if` inside another `if`:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

---

## 8. Common Mistakes
- Forgetting the colon (`:`) after the condition.  
- Misusing `=` instead of `==`:

```python
x = 5
if x == 5:   # ✅ correct
    print("x is 5")

# if x = 5:  # ❌ invalid
```

---

## 9. Practical Example
```python
password = "python123"
user_input = "python123"

if user_input == password:
    print("Login successful")
```

---

## 10. Next Steps
✅ You now know how to use `if` statements for decision-making.  
In the next chapter, we’ll expand on this with **elif and else** clauses.