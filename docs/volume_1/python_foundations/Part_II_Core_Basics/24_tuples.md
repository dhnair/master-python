# Chapter 24: Tuples

## 1. Introduction
A **tuple** is an ordered collection of items, similar to a list.  
The key difference is that **tuples are immutable** — once created, their elements cannot be changed.  

Tuples are often used when you want to group data that should not change.  

---

## 2. Creating Tuples
Tuples use parentheses `()`:

```python
numbers = (1, 2, 3)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)
```

A tuple with one item needs a trailing comma:

```python
single = (5,)
print(type(single))  # <class 'tuple'>
```

---

## 3. Accessing Elements
Like lists, tuples use indexes:

```python
colors = ("red", "green", "blue")
print(colors[0])   # red
print(colors[-1])  # blue
```

---

## 4. Immutability of Tuples
Tuples cannot be changed after creation:

```python
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # ❌ TypeError
```

But you can **reassign the variable** to a new tuple:

```python
colors = ("yellow", "green", "blue")
```

---

## 5. Tuple Operations
- Concatenation:

```python
a = (1, 2)
b = (3, 4)
print(a + b)  # (1, 2, 3, 4)
```

- Repetition:

```python
print(("hi",) * 3)  # ('hi', 'hi', 'hi')
```

- Membership:

```python
print(2 in (1, 2, 3))  # True
```

---

## 6. Tuple Slicing
```python
numbers = (10, 20, 30, 40, 50)
print(numbers[1:3])   # (20, 30)
print(numbers[:3])    # (10, 20, 30)
print(numbers[::-1])  # (50, 40, 30, 20, 10)
```

---

## 7. Tuple Methods
Tuples have only two methods (since they are immutable):

```python
nums = (1, 2, 2, 3)
print(nums.count(2))  # 2
print(nums.index(3))  # 3
```

---

## 8. Nested Tuples
Tuples can contain other tuples:

```python
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][0])  # 3
```

---

## 9. Packing and Unpacking
You can pack values into a tuple and unpack them into variables:

```python
person = ("Alice", 25, "Engineer")

name, age, job = person
print(name)  # Alice
print(age)   # 25
print(job)   # Engineer
```

---

## 10. When to Use Tuples
- When you need **immutable data**.  
- When you want to use a collection as a dictionary key (lists cannot be keys, but tuples can).  
- For grouping related items together, like `(latitude, longitude)`.  

---

## 11. Next Steps
✅ You now understand tuples: how to create them, access them, and why immutability is important.  
In the next chapter, we’ll explore **sets**, which are collections of unique items.