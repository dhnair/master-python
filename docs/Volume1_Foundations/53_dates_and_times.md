# Chapter 53: Dates and Times

## 1. Introduction
Python's `datetime` module helps work with dates and times.

---

## 2. Getting Current Date and Time
```python
from datetime import datetime
now = datetime.now()
print(now)
```

---

## 3. Formatting Dates
```python
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

---

## 4. Parsing Strings into Dates
```python
from datetime import datetime
dt = datetime.strptime("2023-01-01", "%Y-%m-%d")
print(dt)
```

---

## 5. Timedelta for Arithmetic
```python
from datetime import timedelta
tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow)
```

---

## 6. Date Objects
```python
from datetime import date
d = date.today()
print(d)
```

---

## 7. Time Objects
```python
from datetime import time
t = time(14, 30)
print(t)
```

---

## 8. Next Steps
✅ You now know how to handle dates and times.  
Next: **Math operations**.
