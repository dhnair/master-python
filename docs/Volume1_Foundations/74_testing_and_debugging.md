# Capstone Project: File Manager CLI
## Chapter 74: Testing and Debugging

## 1. Introduction
Testing ensures our program works as expected.  
Debugging helps us find and fix issues.

---

## 2. Manual Testing
Run commands from CLI:
```bash
python file_manager.py list .
python file_manager.py read test.txt
python file_manager.py delete test.txt
```

---

## 3. Unit Testing with unittest
```python
import unittest
import os

class TestFileManager(unittest.TestCase):
    def test_write_and_read(self):
        fm = FileManager()
        fm.write("test.txt", "hello")
        self.assertTrue(os.path.exists("test.txt"))
        fm.read("test.txt")
        os.remove("test.txt")

if __name__ == "__main__":
    unittest.main()
```

---

## 4. Debugging with print and logging
```python
print("Debug: entering function")
```

Better: use logging with debug level.

```python
logging.debug("Entering write_file")
```

---

## 5. Next Steps
✅ We can now test and debug our project.  
Next: **Final wrap-up**.
