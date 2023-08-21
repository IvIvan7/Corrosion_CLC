import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
n=0
while n<=5:
    n=n+1
pb = ttk.Progressbar(root, length=100)
pb.pack()
pb.start(n)
root.mainloop()