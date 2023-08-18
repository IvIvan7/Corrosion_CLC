import tkinter as tk
import tkinter.ttk as ttk

#Создание рабочего окна приложения

root = tk.Tk()
root['bg'] = '#fafafa'
root.title('Расчет геометрических параметров тюбингов с коррозией')
root.geometry('600x400')
root.resizable(False, False)

#Рамки с исходными данными и результатами

ini_frame = tk.Frame(master=root, relief='ridge',bd=2)
ini_frame.pack(fill='y', side='left')
post_frame = tk.Frame(master=root, relief='ridge', bd=2)
post_frame.pack(fill='y', side='right')



#Интерфейс расчета возраста тоннеля

age_lbl = tk.Label(master=ini_frame, text='Введите год постройки тоннеля:')
age_lbl.pack()
age_lbl1 = tk.Label(master=ini_frame, text='Введите год постройки тоннеля:')
age_lbl1.pack()
age_lbl2 = tk.Label(master=post_frame, text='Введите год постройки тоннеля:')
age_lbl2.pack()
age_lbl3 = tk.Label(master=post_frame, text='Введите год постройки тоннеля:')
age_lbl3.pack()

root.mainloop()