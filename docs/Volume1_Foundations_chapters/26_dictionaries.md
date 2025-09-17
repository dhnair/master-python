# Volume 1: Foundations
## Chapter 26: Dictionaries

### 1. Introduction
A **dictionary** in Python is a collection of key-value pairs.  
Each key must be unique, and it maps to a value.  
Dictionaries are powerful for storing structured data.  

---

### 2. Creating Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "London"}
print(person)

empty_dict = {}
another = dict(name="Bob", age=30)
```

---

### 3. Accessing Values
Access a value by its key:

```python
print(person["name"])   # Alice
```

Using `.get()` avoids errors if the key doesn’t exist:

```python
print(person.get("job", "Not specified"))  # Not specified
```

---

### 4. Adding and Updating Entries
```python
person["job"] = "Engineer"   # add new key-value pair
person["age"] = 26           # update existing key
print(person)
```

---

### 5. Removing Entries
```python
person.pop("city")      # remove by key
print(person)

person.popitem()        # removes last inserted pair
print(person)

del person["name"]      # delete by key
print(person)

person.clear()          # remove all items
print(person)           # {}
```

---

### 6. Iterating Through Dictionaries
```python
person = {"name": "Alice", "age": 25}

# keys
for key in person:
    print(key)

# values
for value in person.values():
    print(value)

# key-value pairs
for key, value in person.items():
    print(key, ":", value)
```

---

### 7. Checking Keys
```python
person = {"name": "Alice", "age": 25}
print("name" in person)     # True
print("job" not in person)  # True
```

---

### 8. Dictionary Methods
```python
person = {"name": "Alice", "age": 25}

print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 25])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 25)])

copy_person = person.copy()
```

---

### 9. Nested Dictionaries
Dictionaries can contain other dictionaries:

```python
students = {
    "A001": {"name": "Alice", "age": 20},
    "A002": {"name": "Bob", "age": 22}
}
print(students["A001"]["name"])  # Alice
```

---

### 10. Dictionary Comprehensions
```python
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

### 11. When to Use Dictionaries
- When data needs to be accessed by a key (not an index).  
- For structured records (student info, product details).  
- For fast lookups and updates.  

---

### 12. Next Steps
✅ You now understand dictionaries: how to create, access, update, and use them effectively.  
In the next chapter, we’ll cover **booleans and logic** in Python.