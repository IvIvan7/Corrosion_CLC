import tkinter as tk
from tkinter import messagebox

def check_entries_filled(entries):
    for entry in entries:
        if len(entry.get()) == 0:
            messagebox.showerror("Ошибка", "Заполните все поля Entry")
            return False
    return True

def submit_form():
    if check_entries_filled(entry_list):
        # Делайте здесь что-то, когда все поля заполнены
        pass

# Создание окна
root = tk.Tk()
root.title("Проверка полей Entry")

# Создание Entry
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

entry_list = [entry1, entry2, entry3]

# Создание кнопки
submit_button = tk.Button(root, text="Отправить", command=submit_form)

# Размещение элементов в окне
entry1.pack()
entry2.pack()
entry3.pack()
submit_button.pack()

# Запуск главного цикла
root.mainloop()
