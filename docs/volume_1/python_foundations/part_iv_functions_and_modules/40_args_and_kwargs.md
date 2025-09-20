# Chapter 40: *args and **kwargs

## 1. Introduction
`*args` and `**kwargs` let functions accept an arbitrary number of positional and keyword arguments respectively.

---

## 2. Using *args (Positional Varargs)
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # 10
```

---

## 3. Using **kwargs (Keyword Varargs)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, '=', value)

print_info(name='Alice', age=30)
```

---

## 4. Mixing Positional, *args, Defaults, **kwargs
Parameter order: positional, *args, default parameters, **kwargs.

```python
def func(a, *args, b=10, **kwargs):
    print(a, args, b, kwargs)

func(1, 2, 3, b=20, x=99)
```

---

## 5. Unpacking with * and **
You can unpack sequences and dicts when calling functions:

```python
nums = [1, 2, 3]
print(add_numbers(*nums))  # unpacks list into positional args

options = {'name': 'Bob', 'age': 25}
print_info(**options)  # unpacks dict into keyword args
```

---

## 6. Practical Example
```python
def shopping_cart(*items, **details):
    print('Items:', items)
    print('Details:', details)

shopping_cart('apple', 'banana', payment='card', discount=True)
```

---

## 7. Next Steps
✅ You now understand *args and **kwargs.  
Next chapter: **Scope and lifetime of variables**.
