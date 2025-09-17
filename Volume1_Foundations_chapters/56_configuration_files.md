# Volume 1: Foundations
## Chapter 56: Configuration Files

### 1. Introduction
Configuration files store program settings. Python supports multiple formats like `.ini`, `.yaml`, `.json`, and environment variables.

---

### 2. Using INI Files with configparser
```python
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

print(config["DEFAULT"]["username"])
```

Example `settings.ini`:
```ini
[DEFAULT]
username = admin
password = secret
```

---

### 3. Writing INI Files
```python
config["NEW"] = {"key": "value"}
with open("settings.ini", "w") as f:
    config.write(f)
```

---

### 4. JSON Config Files
```python
import json
with open("config.json") as f:
    cfg = json.load(f)
print(cfg)
```

---

### 5. YAML Config Files (via PyYAML)
```python
import yaml
with open("config.yaml") as f:
    cfg = yaml.safe_load(f)
print(cfg)
```

---

### 6. Best Practices
- Keep secrets (like passwords) out of config files.  
- Use environment variables for sensitive info.  
- Document your config structure.  

---

### 7. Next Steps
✅ You now know how to use configuration files.  
Next: **Environment variables**.
