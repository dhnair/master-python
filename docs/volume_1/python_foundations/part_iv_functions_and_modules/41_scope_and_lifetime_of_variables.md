# Chapter 41: Scope and Lifetime of Variables

## 1. Introduction
**Scope** defines where a variable can be accessed in a program.  
**Lifetime** defines how long the variable exists in memory.

---

## 2. Local Scope
Variables defined inside a function are local to that function.

```python
def my_func():
    x = 10  # local variable
    print(x)

my_func()
# print(x)  # ❌ Error: x not defined here
```

---

## 3. Global Scope
Variables defined outside any function are global.

```python
y = 20  # global variable

def show():
    print(y)

show()
print(y)  # accessible everywhere
```

---

## 4. Modifying Globals Inside Functions
Use `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

---

## 5. Enclosing Scope (Nonlocal)
Nested functions can access variables from the enclosing function.

```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)

outer()  # inner
```

---

## 6. Built-in Scope
Python has reserved keywords and built-in functions (like `len`, `print`).

```python
print(len([1,2,3]))
```

---

## 7. Variable Lifetime
- Local variables live only during function execution.  
- Global variables live as long as the program runs.  

---

## 8. Best Practices
- Minimize use of global variables.  
- Prefer returning values instead of modifying globals.  
- Use meaningful variable names.  

---

## 9. Next Steps
✅ You now understand scope and lifetime of variables.  
In the next chapter, we’ll learn about **importing modules**.
