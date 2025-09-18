# Chapter 7: Installing and Configuring Jupyter Notebook

## 1. Introduction
Jupyter Notebook is an interactive coding environment widely used in data science, machine learning, and education.  
It allows you to write and run Python code in small cells, mix code with text, and create rich documents with charts and equations.  

---

## 2. Installing Jupyter with pip
If you already have Python and pip installed, you can install Jupyter directly:

```bash
pip install notebook
```

Verify installation:

```bash
jupyter --version
```

---

## 3. Installing Jupyter with Anaconda
If you installed Anaconda (Chapter 8), Jupyter comes preinstalled.  
You can update it with:

```bash
conda install jupyter
```

---

## 4. Starting Jupyter Notebook
1. Open a terminal (Linux/macOS) or Command Prompt (Windows).  
2. Type:

```bash
jupyter notebook
```

3. This will start a local server and open your default browser.  
   The default address is: [http://localhost:8888](http://localhost:8888)  

---

## 5. Creating Your First Notebook
1. In the browser interface, click **New → Python 3 (ipykernel)**.  
2. A blank notebook will open.  
3. In the first cell, type:

```python
print("Hello, Jupyter!")
```

4. Press **Shift + Enter** to run the cell.  
5. You should see the output below the cell:

```
Hello, Jupyter!
```

---

## 6. Using Markdown in Jupyter
You can add formatted text to your notebooks:  
1. Change a cell type to **Markdown**.  
2. Enter text like:

```markdown
# This is a heading
- Bullet point
- **Bold text**
```

3. Run the cell with **Shift + Enter**.  

---

## 7. Useful Keyboard Shortcuts
- **Shift + Enter** → Run current cell.  
- **A** → Insert cell above.  
- **B** → Insert cell below.  
- **M** → Change cell to Markdown.  
- **Y** → Change cell to Code.  
- **Ctrl + S** → Save notebook.  

---

## 8. Customizing Jupyter Notebook
- Change the working directory by launching Jupyter from the desired folder.  
- Install themes with `pip install jupyterthemes`.  
- Example:

```bash
jt -t monokai
```

---

## 9. Troubleshooting
- **Jupyter not found**: Make sure Python Scripts folder is in PATH (`~/.local/bin` on Linux/macOS, `C:\Users\<name>\AppData\Roaming\Python\Python312\Scripts` on Windows).  
- **Port already in use**: Start with a different port:

```bash
jupyter notebook --port 8889
```

- **Browser not opening**: Copy the URL with token from the terminal and paste it manually into a browser.  

---

## 10. Next Steps
✅ Jupyter Notebook is now installed and running.  
In the next chapter, we will install and configure **Anaconda**, which includes Jupyter and many other useful data science tools.