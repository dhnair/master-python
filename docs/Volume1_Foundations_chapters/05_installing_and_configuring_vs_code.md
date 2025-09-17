# Volume 1: Foundations
## Chapter 5: Installing and Configuring VS Code

### 1. Introduction
Visual Studio Code (VS Code) is a lightweight but powerful code editor from Microsoft.  
It is widely used for Python development because of its excellent extensions, debugging tools, and integrated terminal.  

---

### 2. Downloading VS Code
1. Open your web browser.  
2. Go to the official download page: [https://code.visualstudio.com/](https://code.visualstudio.com/)  
3. Choose your operating system (Windows, macOS, or Linux).  
4. Download the installer (`.exe`, `.dmg`, or `.deb/.rpm`).  

---

### 3. Installing on Windows
1. Run the downloaded `.exe` installer.  
2. Accept the license agreement.  
3. Choose installation location (default is fine).  
4. On the "Select Additional Tasks" screen, check:  
   - ✅ **Add to PATH**  
   - ✅ **Register as default editor for supported file types**  
   - ✅ **Add "Open with Code" to context menu**  
5. Click **Install**.  

---

### 4. Installing on macOS
1. Open the downloaded `.dmg` file.  
2. Drag **Visual Studio Code.app** into the **Applications** folder.  
3. Open VS Code from **Launchpad** or Spotlight.  
4. (Optional) Add `code` command to PATH:  
   - Open VS Code.  
   - Press `Cmd + Shift + P`, type **Shell Command: Install 'code' command in PATH**, and press Enter.  

---

### 5. Installing on Linux
For Ubuntu/Debian:  

```bash
sudo apt update
sudo apt install ./code_*_amd64.deb
```

For Fedora/RHEL:  

```bash
sudo dnf install ./code-*.rpm
```

For Arch (via AUR):  

```bash
yay -S visual-studio-code-bin
```

---

### 6. Installing the Python Extension
1. Open VS Code.  
2. Go to the **Extensions** view (`Ctrl + Shift + X` or `Cmd + Shift + X` on macOS).  
3. Search for **Python**.  
4. Install the official Microsoft Python extension.  

---

### 7. Configuring Python in VS Code
1. Open any `.py` file or create a new one.  
2. If prompted, select your Python interpreter.  
3. You can also manually set it:  
   - Open the Command Palette (`Ctrl + Shift + P`).  
   - Type **Python: Select Interpreter**.  
   - Choose the version you installed earlier.  

---

### 8. Running Your First Program
1. Create a new file `hello.py`.  
2. Type:  

```python
print("Hello from VS Code!")
```

3. Save the file.  
4. Right-click inside the editor and select **Run Python File in Terminal**.  
5. You should see the output in the integrated terminal:

```
Hello from VS Code!
```

---

### 9. Customizing VS Code
- **Themes**: Install new themes from Extensions marketplace.  
- **Fonts**: Go to **Settings → Font Family**.  
- **Keybindings**: Customize shortcuts via **Keyboard Shortcuts** (`Ctrl + K Ctrl + S`).  
- **Extensions**: Explore other useful extensions (Pylance, Jupyter, GitLens).  

---

### 10. Troubleshooting
- **Python not detected**: Check that Python is installed and added to PATH.  
- **Multiple Python versions**: Ensure the correct interpreter is selected via **Python: Select Interpreter**.  
- **Code command not found (macOS/Linux)**: Reinstall the `code` shell command from Command Palette.  

---

### 11. Next Steps
✅ You now have VS Code installed and configured with Python.  
In the next chapter, we will set up **PyCharm**, another popular IDE for Python.