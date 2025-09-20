# Chapter 36: Comprehensions

## 1. Introduction
**Comprehensions** provide a concise and readable way to create lists, sets, or dictionaries from existing iterables. They often replace simple loops and temporary containers.

---

## 2. List Comprehensions: Basic Example
```python
squares = [x * x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## 3. List Comprehensions with Condition
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

---

## 4. Nested Comprehensions
```python
pairs = [(i, j) for i in range(2) for j in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
```

---

## 5. Set Comprehensions
```python
unique_mod3 = {x % 3 for x in range(10)}
print(unique_mod3)  # {0, 1, 2}
```

---

## 6. Dictionary Comprehensions
```python
squares = {x: x * x for x in range(5)}
print(squares)  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

---

## 7. Generator Expressions
Generator expressions use `()` and produce values on demand (lazy evaluation):
```python
gen = (x * x for x in range(3))
for value in gen:
    print(value)
```

Output:
```
0
1
4
```

---

## 8. Readability and When to Use
Comprehensions are great for simple transformations and filters. Avoid stuffing too much logic in a single comprehension — prefer readable code over cleverness.

---

## 9. Common Pitfalls
- Overly complex comprehensions (hard to read).  
- Reusing the same variable name inside comprehension leading to confusion.  
- Generator expressions are single-use (they are iterators).

---

## 10. Next Steps
✅ You now understand comprehensions for lists, sets, dicts, and generators.  
Next chapter: **Defining and calling functions**.
