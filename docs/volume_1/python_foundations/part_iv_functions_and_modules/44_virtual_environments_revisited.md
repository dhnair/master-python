# Chapter 44: Virtual Environments Revisited

## 1. Introduction
We first saw virtual environments in Chapter 16.  
Here, we’ll reinforce their importance in real-world projects.

---

## 2. Why Use Virtual Environments?
- Isolate dependencies for each project.  
- Prevent version conflicts.  
- Keep global Python clean.  

---

## 3. Creating a Virtual Environment
```bash
python3 -m venv venv
```

---

## 4. Activating the Environment
- Windows (cmd): `venv\Scripts\activate`  
- PowerShell: `venv\Scripts\Activate.ps1`  
- Linux/macOS: `source venv/bin/activate`  

---

## 5. Installing Packages in Virtual Environments
```bash
pip install requests
```

Packages stay isolated inside `venv/lib/`.  

---

## 6. Freezing Dependencies
```bash
pip freeze > requirements.txt
```

Recreate environment:
```bash
pip install -r requirements.txt
```

---

## 7. Deactivating and Removing
```bash
deactivate
rm -rf venv
```

---

## 8. Next Steps
✅ You now understand how to use virtual environments effectively.  
In the next chapter, we’ll revisit **installing packages with pip**.
