import tkinter as tk
from tkinter import ttk

def on_combobox_selected(event):
    selected_value = combobox.get()
    result_label.config(text=f"Selected value: {selected_value}")

root = tk.Tk()
root.title("Combobox Example")

combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

result_label = tk.Label(root, text="")
result_label.pack()

combobox.bind("<<ComboboxSelected>>", on_combobox_selected)

root.mainloop()
