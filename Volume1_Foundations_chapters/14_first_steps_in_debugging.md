# Volume 1: Foundations
## Chapter 14: First Steps in Debugging

### 1. Introduction
**Debugging** is the process of finding and fixing errors (bugs) in your code.  
Every programmer encounters bugs — they are a normal part of coding.  
In this chapter, we’ll learn some basic debugging techniques in Python.  

---

### 2. Types of Errors
1. **Syntax Errors** → Mistakes in code structure.  
   Example:

   ```python
   print("Hello"
   ```

   Output:

   ```
   SyntaxError: unexpected EOF while parsing
   ```

2. **Runtime Errors** → Errors that occur while the program is running.  
   Example:

   ```python
   x = 10 / 0
   ```

   Output:

   ```
   ZeroDivisionError: division by zero
   ```

3. **Logic Errors** → Code runs but produces the wrong result.  
   Example:

   ```python
   def add(a, b):
       return a - b   # Bug: should be +
   ```

---

### 3. Using Print Statements
The simplest debugging method: insert `print()` statements.  

Example:

```python
x = 5
y = 0
print("Before division:", x, y)
z = x / y
```

Output shows the values before the crash.  

---

### 4. Using the Built-in `pdb` Debugger
Python includes a command-line debugger called **pdb**.  

Run your script with:

```bash
python3 -m pdb script.py
```

Commands inside pdb:  
- `n` → next line  
- `s` → step into function  
- `c` → continue execution  
- `p variable` → print variable value  
- `q` → quit debugger  

---

### 5. Debugging in IDLE
- Open your script in **IDLE**.  
- Go to **Debug → Debugger**.  
- This opens a panel where you can step through code and inspect variables.  

---

### 6. Debugging in VS Code
1. Open your script in VS Code.  
2. Click in the margin next to a line to add a **breakpoint**.  
3. Press **F5** or go to **Run → Start Debugging**.  
4. The program will pause at the breakpoint.  
5. Inspect variable values in the Debug Console.  

---

### 7. Debugging in PyCharm
1. Open your script in PyCharm.  
2. Right-click and choose **Debug** instead of Run.  
3. Use breakpoints (red dots) to pause execution.  
4. Step through code with the toolbar (Step Over, Step Into).  

---

### 8. Common Debugging Tips
- Read error messages carefully — they tell you the file, line, and type of error.  
- Start by fixing the **first error** in the traceback.  
- Use small test cases to isolate problems.  
- Don’t be afraid of bugs — they are opportunities to learn.  

---

### 9. Next Steps
✅ You now know the basics of debugging in Python.  
In the next chapter, we’ll learn about **pip**, Python’s package manager, which lets you install and use external libraries.