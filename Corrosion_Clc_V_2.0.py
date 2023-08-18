import tkinter as tk
import tkinter.ttk as ttk

#Создание рабочего окна приложения

root = tk.Tk()
root['bg'] = '#fafafa'
root.title('Расчет геометрических параметров тюбингов с коррозией')
root.geometry('800x400+400+200')
root.iconbitmap(default='Ico_2.ico')
root.resizable(False, False)

#Рамки с исходными данными и результатами

ini_frame = tk.LabelFrame(master=root, relief='ridge',bd=2, pady=10, padx=3, text='Исходные данные')
ini_frame.place(width=400, height=400, x=0, y=0)
post_frame = tk.LabelFrame(master=root, relief='ridge', bd=2, pady=10, padx=3, text='Результаты расчета')
post_frame.place(width=400, height=400, x=400, y=0)

#Функция расчета возраста тоннеля

def calc_age (event):
    bld_year = int(float(age_entry.get()))
    from datetime import date
    today = date.today()
    now_year = today.year
    age = now_year - bld_year
    d = age % 10
    if d == 1 and age != 11:
        k =  ' год'
    elif age >= 5 and age <= 20:
        k =  ' лет'
    else:
        k =  ' года'
    age_res_lbl.config(text=f'Возраст тоннеля: {age} {k}')
    return age

#Интерфейс расчета возраста тоннеля

age_lbl = tk.Label(ini_frame, text='Введите год постройки тоннеля:')
age_lbl.grid(row = 0, column = 0, sticky='w')
age_entry = tk.Entry(ini_frame, width=10, bg="white")
age_entry.grid(row = 0, column = 1, sticky='w', pady=5)
age_entry.focus()
age_entry.bind('<FocusOut>', calc_age)
age_entry.bind('<Return>', calc_age)
age_res_lbl = tk.Label(post_frame, text='Возраст тоннеля:')
age_res_lbl.grid(row = 0, column = 0, sticky='w')


#Ввод данных о среде расположения тоннеля

#Перечень исходных параметров из таблиц для расчёта
outside_the_lining = {
        'Атмосфера чистая': 0.025,
        'Атмосфера загрязненная (городская)': 0.125,
        'Атмосфера, обогащенная SO2': 0.79,
        'Вода морская, спокойная': 0.125,
        'Вода морская (скорость течения 6-10 м/с)': 1.25,
        'Почва (ρ=200…1000 Ом*см)': 1,
        'Почва (ρ=1000…2000 Ом*см)': 1
    }

outside_keys_list = list(outside_the_lining.keys())


def on_outcomb_selected(event):
    selected_value = outside_combox.get()
    result_label_outs.config(text=f'Внешняя среда: {selected_value} | {outside_the_lining[selected_value]} мм/год')
    #if selected_value in outside_the_lining:
       # outside_the_lining[selected_value] = value
        #print(value)
   # else: print(3)

#Интерфейс выпадающего списка внешней среды
outside_combox_lbl = tk.Label(ini_frame, text='Определите внешнюю среду:')
outside_combox_lbl.grid(row = 1, column = 0, sticky='w')
outside_combox=ttk.Combobox(ini_frame, values=outside_keys_list, width=30)
outside_combox.grid(row = 1, column = 1, sticky='w')

result_label_outs = tk.Label(post_frame, text='')
result_label_outs.grid(row = 1, column = 0, sticky='w')

outside_combox.bind('<<ComboboxSelected>>', on_outcomb_selected)







root.mainloop()
