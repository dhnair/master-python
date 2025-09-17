# Volume 1: Foundations
## Chapter 16: Introduction to Virtual Environments

### 1. Introduction
A **virtual environment** is an isolated Python workspace.  
It lets you install packages for one project without affecting other projects or the system Python installation.  

This is especially useful when:  
- Different projects require different package versions.  
- You want to avoid breaking system-installed Python packages.  

---

### 2. Checking if venv is Installed
Python 3.3+ includes the `venv` module by default.  
Check by running:

```bash
python3 -m venv --help
```

If you see usage instructions, it’s available.  

---

### 3. Creating a Virtual Environment
Navigate to your project folder and run:

```bash
python3 -m venv myenv
```

This creates a folder called `myenv` that contains a local Python installation.  

---

### 4. Activating the Virtual Environment
- On **Windows** (Command Prompt):

```bash
myenv\Scripts\activate
```

- On **PowerShell**:

```bash
.\myenv\Scripts\Activate.ps1
```

- On **Linux/macOS**:

```bash
source myenv/bin/activate
```

When active, your shell prompt will show `(myenv)`.

---

### 5. Installing Packages Inside the Virtual Environment
Once activated, any pip commands only affect the environment:

```bash
pip install requests
```

Check installed packages:

```bash
pip list
```

---

### 6. Deactivating the Environment
To leave the virtual environment, simply run:

```bash
deactivate
```

---

### 7. Removing a Virtual Environment
Since it’s just a folder, you can delete it safely:

```bash
rm -rf myenv   # Linux/macOS
rmdir /S myenv # Windows
```

---

### 8. Why Use Virtual Environments?
- Prevents dependency conflicts between projects.  
- Keeps your global Python installation clean.  
- Required in most professional Python projects.  

---

### 9. Alternatives
- **virtualenv**: An older tool with extra features.  
- **conda environments**: Used with Anaconda for data science projects.  
- **pipenv** or **poetry**: Modern tools that combine dependency and environment management.  

---

### 10. Next Steps
✅ You now know how to create and use virtual environments.  
In the next chapter, we’ll start exploring **Python’s core language basics**, beginning with variables and assignment rules.