# Chapter 57: Environment Variables

## 1. Introduction
Environment variables are dynamic values set outside Python. They are often used for configuration and secrets.

---

## 2. Accessing Environment Variables
```python
import os
print(os.getenv("HOME"))
```

---

## 3. Setting Environment Variables
Linux/macOS:
```bash
export API_KEY=12345
```
Windows (cmd):
```cmd
set API_KEY=12345
```

---

## 4. Using in Python
```python
api_key = os.getenv("API_KEY", "default_value")
print(api_key)
```

---

## 5. Modifying in Python
```python
os.environ["DEBUG"] = "true"
print(os.environ["DEBUG"])
```

---

## 6. Best Practices
- Use env vars for secrets (API keys, passwords).  
- Don’t hardcode sensitive values in code.  
- Consider libraries like `python-dotenv` for `.env` files.  

---

## 7. Next Steps
✅ You now know environment variables.  
Next: **Introduction to Object-Oriented Programming (OOP)**.
