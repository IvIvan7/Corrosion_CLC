import tkinter as tk

# Функция для создания разделительной линии
def create_separator_line(parent):
    canvas = tk.Canvas(parent, height=2, highlightthickness=0)
    canvas.create_line(0, 1, parent.winfo_width(), 1, fill="black")
    return canvas

# Создаем главное окно
root = tk.Tk()
root.title("Разделительная линия")

# Создаем верхний и нижний фреймы
top_frame = tk.Frame(root)
top_frame.pack(fill="both", expand=True)

bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both", expand=True)

# Создаем разделительную линию
separator = create_separator_line(root)
separator.pack(fill="x")

# Размещаем элементы внутри фреймов
label1 = tk.Label(top_frame, text="Верхний фрейм")
label1.pack()

label2 = tk.Label(bottom_frame, text="Нижний фрейм")
label2.pack()

# Запускаем главный цикл событий
root.mainloop()
