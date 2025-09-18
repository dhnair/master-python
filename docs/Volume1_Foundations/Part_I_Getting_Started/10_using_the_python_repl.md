# Chapter 10: Using the Python REPL

## 1. Introduction
The **Python REPL (Read-Eval-Print Loop)** is an interactive shell where you can type Python commands and see results immediately.  
It is one of the fastest ways to experiment, test small pieces of code, and learn Python.  

---

## 2. Starting the REPL
Open a terminal (Linux/macOS) or Command Prompt (Windows) and type:

```bash
python
```

or, if multiple versions are installed:

```bash
python3
```

You should see something like:

```
Python 3.12.2 (tags/v3.12.2:...) 
>>> 
```

The `>>>` prompt means Python is ready for input.

---

## 3. Running Basic Commands
Try typing:

```python
2 + 3
```

Output:

```
5
```

Try another:

```python
print("Hello, Python!")
```

Output:

```
Hello, Python!
```

---

## 4. Using Variables
You can create variables and use them immediately:

```python
x = 10
y = 5
x + y
```

Output:

```
15
```

---

## 5. Using Built-in Functions
The REPL supports all Python functions:

```python
len("Python")
```

Output:

```
6
```

---

## 6. Getting Help
Inside the REPL, type:

```python
help()
```

This opens an interactive help system.  
Type `quit` to exit help.

You can also get help on a specific function:

```python
help(len)
```

---

## 7. Exiting the REPL
To exit, type:

```python
exit()
```

or press:

- `Ctrl + Z` then Enter (Windows)  
- `Ctrl + D` (Linux/macOS)  

---

## 8. Useful Tips
- Use the **arrow keys** to scroll through command history.  
- Press **Tab** to autocomplete variable names and functions.  
- Use **Ctrl + L** (Linux/macOS) or **cls** command on Windows to clear the screen.  

---

## 9. Why Use the REPL?
- Great for learning Python.  
- Quick way to test ideas.  
- Lightweight compared to opening an IDE.  

---

## 10. Next Steps
✅ You now know how to use the Python REPL to run code interactively.  
In the next chapter, we’ll learn how to **run Python scripts from the command line**.