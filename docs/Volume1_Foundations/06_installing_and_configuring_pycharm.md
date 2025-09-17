# Volume 1: Foundations
## Chapter 6: Installing and Configuring PyCharm

### 1. Introduction
PyCharm is a popular Integrated Development Environment (IDE) created by JetBrains.  
It comes in two editions:  
- **Community Edition (free, open-source)** → ideal for beginners.  
- **Professional Edition (paid)** → adds advanced features such as web development and database tools.  

For most learners, the Community Edition is sufficient.  

---

### 2. Downloading PyCharm
1. Open your web browser.  
2. Go to the official PyCharm download page:  
   [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)  
3. Choose your operating system (Windows, macOS, Linux).  
4. Download the **Community Edition** installer.  

---

### 3. Installing on Windows
1. Run the `.exe` installer.  
2. Follow the setup wizard:  
   - Choose installation location.  
   - (Optional) Create a desktop shortcut.  
   - ✅ Check **Add "Open Folder as Project"** option.  
   - ✅ Add to PATH (recommended).  
3. Click **Install** and wait for the installation to finish.  
4. Launch PyCharm from the Start Menu.  

---

### 4. Installing on macOS
1. Open the `.dmg` file you downloaded.  
2. Drag **PyCharm CE.app** into the **Applications** folder.  
3. Open it via Spotlight or Launchpad.  
4. (Optional) Add `charm` command to PATH for opening projects from Terminal:  
   - Open PyCharm.  
   - Go to **Tools → Create Command-line Launcher**.  
   - Accept default settings.  

---

### 5. Installing on Linux
For Ubuntu/Debian:  

```bash
sudo snap install pycharm-community --classic
```

For Fedora/RHEL (if Snap not available, use tarball):  

```bash
sudo tar -xzf pycharm-community-*.tar.gz -C /opt/
cd /opt/pycharm-community-*/
bin/pycharm.sh
```

For Arch:  

```bash
yay -S pycharm-community-edition
```

---

### 6. Initial Setup
1. Start PyCharm for the first time.  
2. Choose a theme (Light or Dark).  
3. (Optional) Import settings if you used PyCharm before.  
4. Configure font size and keymap if desired.  

---

### 7. Configuring Python Interpreter
1. Create a new project or open an existing folder.  
2. PyCharm will prompt you to set a Python interpreter.  
3. Choose one of the following:  
   - **Existing interpreter** → Use the system Python you installed earlier.  
   - **Virtual environment** → PyCharm can create one for your project.  
4. Confirm the interpreter path (e.g., `python3.12`).  

---

### 8. Creating Your First Project
1. From the welcome screen, click **New Project**.  
2. Enter a project name (e.g., `HelloPython`).  
3. Choose the interpreter.  
4. Click **Create**.  
5. Inside the project, create a new Python file:  
   - Right-click project folder → **New → Python File**.  
   - Name it `hello.py`.  
6. Type:  

```python
print("Hello from PyCharm!")
```

7. Right-click the file and choose **Run 'hello'**.  
8. The output will appear in the Run window:  

```
Hello from PyCharm!
```

---

### 9. Customizing PyCharm
- **Themes and Fonts**: Settings → Appearance & Behavior → Appearance.  
- **Keymaps**: Choose from IntelliJ, VS Code, or custom keybindings.  
- **Plugins**: Explore useful plugins (e.g., Markdown support, Git tools, database tools).  

---

### 10. Troubleshooting
- **Interpreter not found**: Double-check Python is installed and added to PATH.  
- **PyCharm feels slow**: Increase memory in `Help → Change Memory Settings`.  
- **Projects not opening**: Try deleting `.idea` folder in project directory and reopen.  

---

### 11. Next Steps
✅ You now have PyCharm installed and configured.  
In the next chapter, we will set up **Jupyter Notebook**, an interactive environment widely used in data science.