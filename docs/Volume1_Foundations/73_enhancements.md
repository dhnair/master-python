# Capstone Project: File Manager CLI
## Chapter 73: Enhancements

### 1. Introduction
Once the core features work, we can add **enhancements** to improve usability.

---

### 2. Adding Logging
```python
import logging

logging.basicConfig(filename="file_manager.log", level=logging.INFO)

def log_action(action, path):
    logging.info("%s: %s", action, path)
```

---

### 3. Adding Colors (optional)
```python
def print_success(msg):
    print(f"\033[92m{msg}\033[0m")  # green

def print_error(msg):
    print(f"\033[91m{msg}\033[0m")  # red
```

---

### 4. Configuration File
Allow default directory or settings from `config.json`.

```python
import json

with open("config.json") as f:
    config = json.load(f)
print("Default dir:", config["default_dir"])
```

---

### 5. Aliases for Commands
Instead of typing `list`, allow `ls`.  
This can be handled by mapping aliases.

```python
aliases = {"ls": "list", "rm": "delete"}
command = aliases.get(args.command, args.command)
```

---

### 6. Next Steps
✅ We added enhancements like logging, colors, and aliases.  
Next: **Testing and debugging**.
