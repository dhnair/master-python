# Volume 1: Foundations
## Chapter 4: Setting up IDLE

### 1. Introduction
IDLE (Integrated Development and Learning Environment) is Python’s simple built-in editor.  
It is included with most Python installations and is a great starting point for beginners.  

---

### 2. Checking if IDLE is Installed
Open a terminal (macOS/Linux) or Command Prompt (Windows) and type:

```bash
idle3
```

- If IDLE opens, you are ready to use it.  
- If the command is not found, install it using your package manager.  

---

### 3. Installing IDLE on Windows
- IDLE is automatically installed when you install Python from [python.org](https://www.python.org).  
- If you unchecked IDLE during installation, run the installer again and enable the **tcl/tk and IDLE** option.  

---

### 4. Installing IDLE on macOS
- If you installed Python using the **official .pkg installer**, IDLE is already included.  
- If using **Homebrew**, install IDLE with:  

```bash
brew install python-tk
```

---

### 5. Installing IDLE on Linux
For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install idle3 -y
```

For Fedora:

```bash
sudo dnf install python3-tools -y
```

For Arch:

```bash
sudo pacman -S tk
```

---

### 6. Starting IDLE
- On Windows: search for **IDLE** in the Start Menu.  
- On macOS/Linux: run `idle3` from Terminal.  

When IDLE opens, you will see the **Python Shell** (interactive REPL).  

---

### 7. Running Your First Program
1. In IDLE, go to **File → New File**.  
2. Type this program:

```python
print("Hello, Python from IDLE!")
```

3. Save the file as `hello.py`.  
4. Press **F5** or choose **Run → Run Module**.  
5. You should see the output in the Python Shell window:

```
Hello, Python from IDLE!
```

---

### 8. Customizing IDLE
- **Fonts and Colors**: Go to **Options → Configure IDLE**.  
- **Themes**: Switch to dark mode or change syntax colors.  
- **Indentation**: Adjust spaces per tab for coding style.  

---

### 9. Troubleshooting
- **IDLE not opening**: Ensure `tkinter` is installed.  
  On Ubuntu/Debian:

  ```bash
  sudo apt install python3-tk -y
  ```

- **Multiple Python versions**: If IDLE opens the wrong version, check the shebang in the IDLE launcher or use the full command:  

```bash
idle3.12
```

---

### 10. Next Steps
✅ You now have IDLE set up and running.  
In the next chapter, we will set up **VS Code**, a more powerful editor for Python development.