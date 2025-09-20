# Chapter 15: Working with pip

## 1. Introduction
**pip** is Python’s default package manager.  
It allows you to install, update, and remove external libraries (packages) that extend Python’s functionality.  
Most Python projects use pip to manage dependencies.  

---

## 2. Checking if pip is Installed
Open a terminal or Command Prompt and run:

```bash
pip --version
```

or

```bash
pip3 --version
```

You should see something like:

```
pip 23.2.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

If you get an error, pip may not be installed.  

---

## 3. Installing pip (if missing)
- On **Windows**, reinstall Python with the **pip** option checked.  
- On **Linux/macOS**, install with:  

```bash
sudo apt install python3-pip        # Ubuntu/Debian
sudo dnf install python3-pip        # Fedora
brew install pipx && pipx ensurepath # macOS with Homebrew
```

---

## 4. Installing a Package
To install a package:

```bash
pip install requests
```

This installs the `requests` library for making HTTP requests.  

---

## 5. Using Installed Packages
After installation, you can import the package in Python:

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)
```

---

## 6. Listing Installed Packages
Check what’s installed:

```bash
pip list
```

Sample output:

```
numpy  1.26.0
pandas 2.1.1
requests 2.31.0
```

---

## 7. Upgrading Packages
Update a package to the latest version:

```bash
pip install --upgrade requests
```

Upgrade pip itself:

```bash
pip install --upgrade pip
```

---

## 8. Uninstalling Packages
Remove a package:

```bash
pip uninstall requests
```

---

## 9. Requirements Files
For larger projects, dependencies are stored in a file called `requirements.txt`.

- Create one:

```bash
pip freeze > requirements.txt
```

- Install all packages from it:

```bash
pip install -r requirements.txt
```

---

## 10. Troubleshooting
- **Permission denied (Linux/macOS)** → Use `pip install --user <package>`.  
- **pip installs wrong version** → Make sure you use `pip3` with Python 3.  
- **PATH issues** → Add the Python `Scripts/` folder to PATH.  

---

## 11. Next Steps
✅ You now know how to install and manage packages with pip.  
In the next chapter, we’ll explore **virtual environments**, which let you manage project-specific dependencies.