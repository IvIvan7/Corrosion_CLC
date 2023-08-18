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
        'Почва (ρ=200…1000 Ом*см)': 0.06,
        'Почва (ρ=1000…2000 Ом*см)': 0.03
    }

outside_keys_list = list(outside_the_lining.keys())

#Внешняя среда

def proc_out(event):
    selected_value_outs = outside_combox.get()
    cond_outs = int(float(cond_outs_ent.get()))
    if selected_value_outs == 'Почва (ρ=200…1000 Ом*см)':
        m = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (cond_outs - 1000)
        outside_the_lining[selected_value_outs] = m
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')
    else:
        n = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (cond_outs - 2000)
        outside_the_lining[selected_value_outs] = n
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')

def on_outcomb_selected(event):
    selected_value_outs = outside_combox.get()
    if selected_value_outs == 'Почва (ρ=200…1000 Ом*см)':
        cond_outs_ent.config(state='normal')
        cond_outs_ent.focus()
        cond_outs_ent.delete(0, tk.END)
    elif selected_value_outs == 'Почва (ρ=1000…2000 Ом*см)':
        cond_outs_ent.config(state='normal')
        cond_outs_ent.focus()
        cond_outs_ent.delete(0, tk.END)
    result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')

#Интерфейс выпадающего списка внешней среды
outside_combox_lbl = tk.Label(ini_frame, text='Определите внешнюю среду:')
outside_combox_lbl.grid(row = 1, column = 0, sticky='w')
outside_combox=ttk.Combobox(ini_frame, values=outside_keys_list, width=30)
outside_combox.grid(row = 1, column = 1, sticky='w')
result_label_outs = tk.Label(post_frame, text='')
result_label_outs.grid(row = 1, column = 0, sticky='w')
cond_outs_lbl = tk.Label(ini_frame, text='Введите значение \n электропроводности:')
cond_outs_lbl.grid(row = 2, column = 0, sticky='w')
cond_outs_ent = tk.Entry(ini_frame, width=10, bg="white", state='disabled')
cond_outs_ent.grid(row = 2, column = 1, sticky='w')
cond_outs_ent.bind('<Return>', proc_out)
cond_outs_ent.bind('<FocusOut>', proc_out)
outside_combox.bind('<<ComboboxSelected>>', on_outcomb_selected)


# Внутренняя

#Перечень исходных параметров из таблиц для расчёта
inside_the_lining = {
        'Атмосфера чистая': 0.025,
        'Атмосфера загрязненная (городская)': 0.125,
        'Атмосфера, обогащенная SO2': 0.79,
        'Вода морская, спокойная': 0.125,
        'Вода морская (скорость течения 6-10 м/с)': 1.25,
        'Почва (ρ=200…1000 Ом*см)': 0.06,
        'Почва (ρ=1000…2000 Ом*см)': 0.03
    }

inside_keys_list = list(inside_the_lining.keys())

def proc_ins(event):
    selected_value_ins = inside_combox.get()
    cond_ins = int(float(cond_ins_ent.get()))
    if selected_value_ins == 'Почва (ρ=200…1000 Ом*см)':
        x = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (cond_ins - 1000)
        inside_the_lining[selected_value_ins] = x
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {inside_the_lining[selected_value_ins]} мм/год')
    else:
        y = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (cond_ins - 2000)
        inside_the_lining[selected_value_ins] = y
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {inside_the_lining[selected_value_ins]} мм/год')


def on_inscomb_selected(event):
    selected_value_ins = inside_combox.get()
    if selected_value_ins == 'Почва (ρ=200…1000 Ом*см)':
        cond_ins_ent.config(state='normal')
        cond_ins_ent.focus()
        cond_ins_ent.delete(0, tk.END)
    elif selected_value_ins == 'Почва (ρ=1000…2000 Ом*см)':
        cond_ins_ent.config(state='normal')
        cond_ins_ent.focus()
        cond_ins_ent.delete(0, tk.END)
    result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {outside_the_lining[selected_value_ins]} мм/год')


# Интерфейс выпадающего списка внешней среды
inside_combox_lbl = tk.Label(ini_frame, text='Определите внутреннюю среду:')
inside_combox_lbl.grid(row=3, column=0, sticky='w')
inside_combox = ttk.Combobox(ini_frame, values=outside_keys_list, width=30)
inside_combox.grid(row=3, column=1, sticky='w')
result_label_ins = tk.Label(post_frame, text='')
result_label_ins.grid(row=3, column=0, sticky='w')
cond_ins_lbl = tk.Label(ini_frame, text='Введите значение \n электропроводности:')
cond_ins_lbl.grid(row=4, column=0, sticky='w')
cond_ins_ent = tk.Entry(ini_frame, width=10, bg="white", state='disabled')
cond_ins_ent.grid(row=4, column=1, sticky='w')
cond_ins_ent.bind('<Return>', proc_ins)
cond_ins_ent.bind('<FocusOut>', proc_ins)
inside_combox.bind('<<ComboboxSelected>>', on_inscomb_selected)





root.mainloop()
