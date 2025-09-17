# Volume 1: Foundations
## Chapter 2: Installing Python on macOS

### 1. Introduction
macOS includes a system version of Python, but it is often outdated and should not be used for development.  
It is recommended to install the latest stable Python release separately.  

---

### 2. Checking the Current Python Version
Open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter) and run:  

```bash
python3 --version
```

If the version is older than 3.10 or missing, install the latest release.  
You can also check if pip is available:  

```bash
pip3 --version
```

---

### 3. Downloading the Official Installer
1. Open a web browser.  
2. Visit the official download page: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)  
3. The site will suggest the latest stable version (e.g., Python 3.12.x).  
4. Download the **macOS 64-bit universal installer (.pkg file)**.  

---

### 4. Installing with the .pkg Installer
1. Locate the downloaded file in **Downloads** (example: `python-3.12.x-macosx10.9.pkg`).  
2. Double-click the `.pkg` file.  
3. Follow the prompts:  
   - Continue → Agree to license → Select install location.  
   - Enter your administrator password when asked.  
4. After installation, Python is usually placed in `/usr/local/bin/python3`.  

---

### 5. Alternative: Installing with Homebrew
If you prefer the Homebrew package manager:  

1. Install Homebrew (if not already installed):  

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python:  

```bash
brew install python
```

3. Verify installation:  

```bash
python3 --version
pip3 --version
```

---

### 6. Verifying Installation
Check that Python and pip are working:  

```bash
python3 --version
pip3 --version
```

Expected output:  

```
Python 3.12.2
pip 23.x.x
```

---

### 7. Troubleshooting
- **Command not found**: Restart Terminal or confirm the path with:  

```bash
which python3
```

- **Multiple versions of Python**:  
  - macOS may have an old system Python.  
  - Always use `python3` instead of `python`.  

- **pip missing**: Install separately with:  

```bash
sudo apt install python3-pip   # if on Linux subsystem
brew reinstall python          # if using Homebrew
```

- **PATH issues**: Add `/usr/local/bin` to your PATH if needed by editing `~/.zshrc` or `~/.bashrc`.  

---

### 8. Uninstalling Python
- If installed via the `.pkg` file, manually remove from `/Library/Frameworks/Python.framework/Versions/`.  
- If installed with Homebrew, run:  

```bash
brew uninstall python
```

---

### 9. Next Steps
✅ Python is now installed on macOS.  
In the next chapter, we will install Python on **Linux distributions**.