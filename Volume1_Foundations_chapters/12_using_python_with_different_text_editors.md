# Volume 1: Foundations
## Chapter 12: Using Python with Different Text Editors

### 1. Introduction
Python code can be written in any plain text editor.  
While IDEs like VS Code and PyCharm are powerful, sometimes a simple text editor is faster and more lightweight.  
In this chapter, we’ll explore using Python with several popular text editors.  

---

### 2. Notepad (Windows)
- The simplest editor available on Windows.  
- Steps:  
  1. Open **Notepad**.  
  2. Write a Python program, for example:  

     ```python
     print("Hello from Notepad!")
     ```  
  3. Save the file with the `.py` extension (e.g., `hello.py`).  
     - Select **Save as type → All Files**.  
     - Encoding: **UTF-8**.  
  4. Run the file from Command Prompt with:  

     ```bash
     python hello.py
     ```

---

### 3. TextEdit (macOS)
- The built-in text editor for macOS.  
- Steps:  
  1. Open **TextEdit**.  
  2. Go to **Format → Make Plain Text**.  
  3. Write Python code and save it with `.py` extension (e.g., `hello.py`).  
  4. Run from Terminal with:  

     ```bash
     python3 hello.py
     ```

---

### 4. Nano (Linux/macOS Terminal Editor)
- A simple terminal-based text editor.  
- Steps:  
  1. Open Terminal.  
  2. Create a new file with:  

     ```bash
     nano hello.py
     ```  
  3. Write Python code inside.  
  4. Save with **Ctrl + O**, exit with **Ctrl + X**.  
  5. Run with:  

     ```bash
     python3 hello.py
     ```

---

### 5. Vim and Neovim
- Powerful modal text editors for advanced users.  
- Steps:  
  1. Install Vim:  

     ```bash
     sudo apt install vim        # Ubuntu/Debian
     sudo pacman -S vim          # Arch
     brew install vim            # macOS
     ```  

  2. Create a Python file:  

     ```bash
     vim hello.py
     ```  

  3. Press **i** to enter insert mode, write Python code.  
  4. Save and quit: **Esc → :wq**.  
  5. Run as usual:  

     ```bash
     python3 hello.py
     ```

---

### 6. Sublime Text
- A fast, extensible editor with Python plugins.  
- Installation: [https://www.sublimetext.com/](https://www.sublimetext.com/)  
- Steps:  
  1. Open Sublime Text.  
  2. Write Python code.  
  3. Save with `.py` extension.  
  4. Install the **SublimeREPL** plugin for running Python inside Sublime.  

---

### 7. Atom (Discontinued, still usable via forks)
- Atom was discontinued, but forks like **Pulsar** exist.  
- Features include extensions and integrated terminals.  

---

### 8. Why Use Text Editors?
- **Lightweight** compared to IDEs.  
- **Universal** — works on any OS.  
- **Customizable** — plugins, syntax highlighting, linting.  

---

### 9. Next Steps
✅ You now know how to write Python code in various text editors.  
In the next chapter, we’ll look at the difference between **Python scripts and modules**.