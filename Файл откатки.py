import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)  # Очищаем текущий текст в поле
            text.insert("1.0", content)  # Вставляем содержимое файла в поле

root = tk.Tk()
root.title("Открыть текстовый файл")

text = tk.Text(root)
text.pack()

open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.pack()

root.mainloop()