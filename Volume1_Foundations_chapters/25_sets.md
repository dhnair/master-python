# Volume 1: Foundations
## Chapter 25: Sets

### 1. Introduction
A **set** is an unordered collection of unique items.  
Sets are useful when you want to store values without duplicates or perform mathematical set operations.  

---

### 2. Creating Sets
Sets use curly braces `{}` or the `set()` function:

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}  (duplicates removed)

empty_set = set()  # correct way
```

⚠️ `{}` creates an empty dictionary, not a set.  

---

### 3. Adding and Removing Elements
```python
fruits = {"apple", "banana"}

fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

fruits.remove("banana")  # ❌ KeyError if not found
fruits.discard("pear")   # ✅ safe, no error if not found

popped = fruits.pop()    # removes a random element
print(popped)
```

---

### 4. Checking Membership
```python
animals = {"cat", "dog", "bird"}
print("cat" in animals)   # True
print("lion" not in animals) # True
```

---

### 5. Set Operations
Sets support union, intersection, difference, and symmetric difference:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric difference → {1, 2, 4, 5}
```

---

### 6. Updating Sets
```python
a = {1, 2}
a.update([2, 3, 4])
print(a)  # {1, 2, 3, 4}
```

---

### 7. Frozen Sets
A **frozenset** is an immutable set:

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ Error: frozenset is immutable
```

You can use frozensets as dictionary keys or store them in other sets.  

---

### 8. Iterating Through Sets
```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

(Remember: order is not guaranteed.)  

---

### 9. When to Use Sets
- Removing duplicates from a collection.  
- Checking membership quickly.  
- Performing mathematical set operations.  
- Using frozensets for immutable collections.  

---

### 10. Next Steps
✅ You now understand sets and frozensets.  
In the next chapter, we’ll explore **dictionaries**, Python’s key-value data structure.