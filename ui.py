import tkinter as tk
from tkinter import filedialog
import os

# --- Initial essentials variable and window ---

# Simple in-memory cache to store important values
cache = {"current_file": None,}

# Define a placeholder text for new files
Placeholder = "This is a new blank file."

# Create a new Tkinter window
root = tk.Tk()
root.title("NotePad--")
root.geometry("600x400")

# Disable resizing of the window
root.resizable(False, False)

# Define action menu functions

# Function to open the Control Panel
def open_control_panel():
    from Control_Panel import open_panel
    open_panel(root)

# Function to create a new file
def new_file():
    # Define essentials variables
    base_name = "New_File"
    ext = ".txt"
    i = 0
    placeholder = "This is a new blank file."
    filename = f"{base_name}{ext}"

    # Check for existing files and create a unique filename
    while os.path.exists(filename):
        i += 1
        filename = f"{base_name}_{i}{ext}"
        
    # Create the new file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(placeholder)

    # Update the window with the new file
    text_box.delete('1.0', "end")
    text_box.insert('1.0', placeholder)

# Function to open an existing file
def open_file():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        # Read the content of the selected file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Update the text box with the content of the file
        text_box.delete('1.0', "end")
        text_box.insert('1.0', content)

# Function to save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")], title="Save As...")

    if file_path:
        content = text_box.get('1.0', tk.END+"-1c")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        global current_file
        cache["current_file"] = file_path

# --- Setting up the menu bar ---

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a Control Panel menu
control_panel_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Control Panel", menu=control_panel_menu)

# Create an Exit menu

exit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Exit", menu=exit_menu)

# Adding commands to the File menu
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File As...", command=save_file)

# Adding commands to the Control Panel menu
control_panel_menu.add_command(label="Open Control Panel", command=open_control_panel)

# Adding commands to the Exit menu
exit_menu.add_command(label="Exit Application", command=root.quit)

# --- Doing some verification and setups ---

# Check if there's a current file in the cache
if not cache["current_file"]:
    # Name the new file and set it in the cache
    cache["current_file"] = "New_File.txt"
    # Check if the file don't exists
    if not os.path.exists(cache["current_file"]):
        # Create the new file
        with open(cache["current_file"], "w", encoding="utf-8") as f:
            # Write the placeholder text into the new file
            f.write(Placeholder)

# Check if a file is set in the cache
if cache["current_file"]:
    # Open the current file with read
    with open(cache["current_file"], "r") as f:
        # Read the content of the file and store it in a variable  
        content = f.read()

# --- Setting up the Text widget ---

# Create a text box
text_box = tk.Text(root, wrap='word')

# Insert the content of the file into the text box
text_box.insert('1.0', content)

# Add a scrollbar to the text box
scroll = tk.Scrollbar(root, command=text_box.yview, width=10)
text_box.configure(yscrollcommand=scroll.set)

# Pack everything
scroll.pack(side='right', fill='y', expand=True)
text_box.pack(side="left", expand=True, fill='both')

# Run everything
root.mainloop()