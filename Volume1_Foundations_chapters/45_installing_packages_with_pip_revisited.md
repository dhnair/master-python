# Volume 1: Foundations
## Chapter 45: Installing Packages with pip Revisited

### 1. Introduction
We learned about `pip` in Chapter 15.  
Now we’ll go deeper into best practices for package management in real projects.

---

### 2. Installing a Specific Version
```bash
pip install requests==2.31.0
```

---

### 3. Upgrading and Downgrading
```bash
pip install --upgrade requests
pip install requests==2.28.0
```

---

### 4. Uninstalling Packages
```bash
pip uninstall requests
```

---

### 5. Listing Installed Packages
```bash
pip list
```

---

### 6. Searching for Packages
```bash
pip search flask
```

---

### 7. Using requirements.txt
Create:
```bash
pip freeze > requirements.txt
```

Install from file:
```bash
pip install -r requirements.txt
```

---

### 8. Using pip in Virtual Environments
Always activate your environment before installing packages.  
This keeps dependencies isolated.  

---

### 9. Common Issues
- Permission errors → use `--user` or virtual environments.  
- Version conflicts → check `pipdeptree` or use virtual environments.  

---

### 10. Next Steps
✅ You now understand advanced `pip` usage.  
In the next chapter, we’ll learn about **reading text files**.
