import tkinter as tk

def on_validate_input(P):
    if P == "" or P.isdigit():
        return True
    else:
        return False

root = tk.Tk()
root.title("Only Digits Entry")

validate_input = root.register(on_validate_input)

entry = tk.Entry(root, validate="key", validatecommand=(validate_input, "%P"))
entry.pack(padx=20, pady=20)

root.mainloop()
