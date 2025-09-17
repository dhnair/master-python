# Volume 1: Foundations
## Chapter 65: Mini Project — Student and Course Manager

### 1. Introduction
Let’s apply OOP concepts (classes, attributes, methods, inheritance, encapsulation) to build a small project.

---

### 2. Requirements
- Manage students and courses.  
- Add/remove students.  
- Enroll students in courses.  
- Show enrollments.  

---

### 3. Student Class
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
```

---

### 4. Course Class
```python
class Course:
    def __init__(self, title):
        self.title = title
        self.students = []
    def add_student(self, student):
        self.students.append(student)
```

---

### 5. Manager Class
```python
class Manager:
    def __init__(self):
        self.students = []
        self.courses = []
    def add_student(self, student):
        self.students.append(student)
    def add_course(self, course):
        self.courses.append(course)
```

---

### 6. Putting It Together
```python
s1 = Student("Alice")
s2 = Student("Bob")
c1 = Course("Math")
c2 = Course("Science")

m = Manager()
m.add_student(s1)
m.add_student(s2)
m.add_course(c1)
m.add_course(c2)

s1.enroll(c1)
s2.enroll(c2)

print(s1.name, "enrolled in", [c.title for c in s1.courses])
print(s2.name, "enrolled in", [c.title for c in s2.courses])
```

---

### 7. Next Steps
✅ You built a small OOP project.  
Next: **Capstone Project — File Manager CLI**.
