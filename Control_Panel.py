import tkinter as tk

def open_panel(root):
    panel = tk.Toplevel(root)
    panel.title("Control Panel -- Configure your NotePad-- !")
    panel.geometry("300x200")
    label = tk.Label(panel, text="Nothing to configure yet !")
    label.pack(pady=20)

    panel.transient(root)
    panel.grab_set()