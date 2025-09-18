# Chapter 11: Running Python Scripts from the Command Line

## 1. Introduction
While the Python REPL is great for quick experiments, real projects require saving code into files.  
You can then run these **Python scripts** from the command line.  

---

## 2. Creating Your First Python Script
1. Open any text editor (Notepad, VS Code, PyCharm, etc.).  
2. Type the following code:

```python
print("Hello from a Python script!")
```

3. Save the file as `hello.py`.  

---

## 3. Running on Windows
1. Open **Command Prompt**.  
2. Navigate to the folder where you saved `hello.py`. Example:

```bash
cd C:\Users\YourName\Documents
```

3. Run the script with:

```bash
python hello.py
```

If you have multiple versions of Python, use:

```bash
py hello.py
```

---

## 4. Running on macOS/Linux
1. Open **Terminal**.  
2. Navigate to the folder where you saved `hello.py`. Example:

```bash
cd ~/Documents
```

3. Run the script with:

```bash
python3 hello.py
```

---

## 5. Using Absolute and Relative Paths
You don’t always need to `cd` into the directory. You can run a script by giving its path:  

```bash
python3 ~/Documents/hello.py
```

Or from the current folder:  

```bash
python3 ./hello.py
```

---

## 6. Adding a Shebang (Linux/macOS only)
At the top of your script, add:

```python
#!/usr/bin/env python3
```

Make the file executable:

```bash
chmod +x hello.py
```

Now you can run it directly:

```bash
./hello.py
```

---

## 7. Passing Arguments to a Script
You can pass values to your script:

```bash
python3 hello.py world
```

In your script:

```python
import sys
print("Hello,", sys.argv[1])
```

Output:

```
Hello, world
```

---

## 8. Troubleshooting
- **‘python’ not recognized (Windows)** → Use `py` or check that Python was added to PATH during installation.  
- **Permission denied (Linux/macOS)** → Use `chmod +x filename.py` to make it executable.  
- **Wrong version running** → Specify `python3` instead of `python`.  

---

## 9. Why Run Scripts from the Command Line?
- Reproducible: you can save and run the same script multiple times.  
- Shareable: scripts can be distributed to others.  
- Practical: most real-world Python projects are run as scripts or applications.  

---

## 10. Next Steps
✅ You now know how to run Python scripts from the command line.  
In the next chapter, we will explore how to **use Python with different text editors**.