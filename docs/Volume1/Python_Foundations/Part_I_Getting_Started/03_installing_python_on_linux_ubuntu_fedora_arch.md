# Chapter 3: Installing Python on Linux (Ubuntu, Fedora, Arch)

## 1. Introduction
Most Linux distributions come with Python preinstalled, but the system version is often outdated.  
For development work, it is recommended to install the latest stable Python release using your distribution’s package manager.  

---

## 2. Checking the Current Python Version
Before installing, check what version of Python is already on your system:  

```bash
python3 --version
```

If you see Python 3.10 or newer, you may already be fine.  
If the command fails or the version is older, follow the steps below.  

You can also check `pip` (Python’s package manager):  

```bash
pip3 --version
```

If pip is missing, it will need to be installed.  

---

## 3. Installing on Ubuntu and Debian
Update package lists:  

```bash
sudo apt update
```

Install Python 3 and pip:  

```bash
sudo apt install python3 python3-pip -y
```

Verify installation:  

```bash
python3 --version
pip3 --version
```

To uninstall (if you need to remove a broken version):  

```bash
sudo apt remove python3 python3-pip
```

---

## 4. Installing on Fedora
Update packages:  

```bash
sudo dnf update -y
```

Install Python 3 and pip:  

```bash
sudo dnf install python3 python3-pip -y
```

Verify installation:  

```bash
python3 --version
pip3 --version
```

Uninstall if needed:  

```bash
sudo dnf remove python3 python3-pip
```

---

## 5. Installing on Arch Linux
Update the system:  

```bash
sudo pacman -Syu
```

Install Python and pip:  

```bash
sudo pacman -S python python-pip
```

Verify installation:  

```bash
python --version
pip --version
```

Uninstall if needed:  

```bash
sudo pacman -R python python-pip
```

---

## 6. Building from Source (Advanced Users)
If you want the very latest Python release:  

1. Download the source from [https://www.python.org/ftp/python/](https://www.python.org/ftp/python/).  
2. Extract and compile:  

```bash
tar -xf Python-3.x.x.tgz
cd Python-3.x.x
./configure --enable-optimizations
make
sudo make install
```

3. Verify installation:  

```bash
python3 --version
```

---

## 7. Troubleshooting
- **Command not found**: Try `python3` instead of `python`, or check your PATH with:  

```bash
which python3
```

- **pip missing**: Install separately if not included:  

```bash
sudo apt install python3-pip -y     # Ubuntu/Debian
sudo dnf install python3-pip -y     # Fedora
sudo pacman -S python-pip           # Arch
```

- **Multiple versions installed**: Use `update-alternatives` (Debian/Ubuntu) to switch default versions.  

---

## 8. Next Steps
✅ Python is now installed and ready on your Linux system.  
In the next chapter, we will set up **IDLE**, Python’s built-in editor, to start writing your first programs.