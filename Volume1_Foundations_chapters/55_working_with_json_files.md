# Volume 1: Foundations
## Chapter 55: Working with JSON Files

### 1. Introduction
JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. Python provides the `json` module.

---

### 2. Writing JSON
```python
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)
```

---

### 3. Reading JSON
```python
with open("data.json") as f:
    obj = json.load(f)
print(obj)
```

---

### 4. Converting Between JSON and Strings
```python
s = json.dumps(data)
print(s)
obj = json.loads(s)
print(obj)
```

---

### 5. Handling Non-Serializable Data
Custom objects need conversion before JSON encoding.

```python
from datetime import datetime
data = {"time": datetime.now().isoformat()}
```

---

### 6. Pretty Printing JSON
```python
print(json.dumps(data, indent=4))
```

---

### 7. Next Steps
✅ You now know how to read and write JSON in Python.  
Next: **Configuration files**.
