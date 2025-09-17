# Volume 1: Foundations
## Chapter 23: Lists

### 1. Introduction
A **list** is an ordered, changeable collection of items.  
Lists are one of the most commonly used data structures in Python because they are flexible and easy to use.  

---

### 2. Creating Lists
Lists are defined using square brackets `[]`:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

---

### 3. Accessing List Elements
Use **indexes** (starting at 0):

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last element)
```

---

### 4. Modifying Lists
Lists are mutable, meaning you can change them:

```python
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

---

### 5. Adding Items
- Append to the end:

```python
fruits.append("orange")
```

- Insert at a position:

```python
fruits.insert(1, "mango")
```

---

### 6. Removing Items
```python
fruits.remove("apple")   # remove by value
print(fruits)

fruits.pop(1)            # remove by index
print(fruits)

last = fruits.pop()      # remove last item
print(last)

fruits.clear()           # remove all items
print(fruits)  # []
```

---

### 7. List Slicing
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])  # [20, 30]
print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]
print(numbers[::-1]) # reversed list
```

---

### 8. Checking Membership
```python
fruits = ["apple", "banana"]
print("apple" in fruits)   # True
print("mango" not in fruits) # True
```

---

### 9. Iterating Over a List
```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

---

### 10. Useful List Methods
```python
numbers = [3, 1, 4, 1, 5]

print(len(numbers))      # 5
print(numbers.count(1))  # 2
print(numbers.index(4))  # 2
numbers.sort()
print(numbers)           # [1, 1, 3, 4, 5]
numbers.reverse()
print(numbers)           # [5, 4, 3, 1, 1]
```

---

### 11. Nested Lists
Lists can contain other lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6
```

---

### 12. Copying Lists
Be careful when copying lists:

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3] (changes reflected!)

# Correct way:
c = a.copy()
c[0] = 42
print(a)  # [99, 2, 3]
print(c)  # [42, 2, 3]
```

---

### 13. When to Use Lists
- When you need an **ordered collection**.  
- When you need to frequently modify elements.  
- For storing sequences of data like names, scores, or items.  

---

### 14. Next Steps
✅ You now understand how to create, access, modify, and use lists.  
In the next chapter, we’ll explore **tuples**, which are similar to lists but immutable.