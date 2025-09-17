# Volume 1: Foundations
## Chapter 1: Installing Python on Windows

### 1. Introduction
Windows does not come with Python preinstalled.  
To start programming, we must download, install, and configure the latest version of Python.  

---

### 2. Downloading Python
1. Open a web browser.  
2. Go to the official Python download page:  
   [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)  
3. The site will automatically suggest the latest stable version (for example: Python 3.12.x).  
4. Click the **Download Python 3.x.x** button.  

---

### 3. Running the Installer
1. Locate the downloaded file in your **Downloads** folder (example: `python-3.12.x-amd64.exe`).  
2. Double-click the installer to run it.  
3. On the first screen:  
   - ✅ Check the box **“Add Python to PATH”** (very important).  
   - Click **Install Now**.  
4. Wait for the installation to complete.  

---

### 4. Custom Installation (Optional)
If you want more control:  
- Choose **Customize installation**.  
- Options you may enable:  
  - Documentation  
  - pip (package manager)  
  - Add Python to environment variables  
- This is useful if you want multiple versions of Python installed.  

---

### 5. Verifying Installation
1. Open the Command Prompt (press `Win + R`, type `cmd`, press Enter).  
2. Type:  

```bash
python --version
```

or  

```bash
py --version
```

You should see something like:  

```
Python 3.12.2
```

3. Verify pip:  

```bash
pip --version
```

---

### 6. First Run of Python
In Command Prompt, type:  

```bash
python
```

This opens the Python REPL (interactive shell).  
Type `exit()` or press `Ctrl + Z` then Enter to quit.  

---

### 7. Troubleshooting
- **‘python’ not recognized**:  
  - Try `py` instead.  
  - If that works, it means Python is installed but not added to PATH.  
  - Reinstall and check the **“Add to PATH”** option.  

- **Multiple versions of Python**:  
  - Use `py -0` to list installed versions.  
  - Run a specific version with `py -3.12` or `py -3.11`.  

- **Pip missing**:  
  - Run the installer again and check **pip** option.  

---

### 8. Uninstalling Python
1. Open **Control Panel → Programs → Programs and Features**.  
2. Find Python in the list.  
3. Select it and click **Uninstall**.  

---

### 9. Next Steps
✅ Python is now installed on Windows.  
In the next chapter, we will learn how to install Python on macOS.