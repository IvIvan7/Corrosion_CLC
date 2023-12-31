import tkinter as tk
import tkinter.ttk as ttk
import re
from tkinter import messagebox
import os
import subprocess
from tkinter import filedialog
from datetime import date

#Функция завершающая программу
def quit_mainloop():
    root.quit()

#Функция запрета ввода слов в поля
def on_validate_input(P):
    return re.match(r'^\d*\.?\d*$', P) is not None

#Функция очистки рабочего пространства
def clear_entries(entries, labeles, comboboxes, conds):
    for entry in entries:
        entry.delete(0, tk.END)
    for labele in labeles:
        labele.config(text="")
    for combobox in comboboxes:
        combobox.set('')
    for cond in conds:
        cond.config(state='disabled')
    age_entry.focus()
def clear_post(labels):
    for label in labels:
        label.config(text="")

#Функция ошибки пустых полей
def check_entries_filled(ini_entries):
    for ini_entry in ini_entries:
        if len(ini_entry.get()) == 0:
            messagebox.showerror("Ошибка", "Заполните все поля")
            return False
    return True

def save_file():
    wr_result = clc_new_geom(0)
    filepath = filedialog.asksaveasfilename()
    filep = filepath + '.txt'
    if filepath != "":
        with open(filep, "w") as file:
            file.write(wr_result)
            subprocess.Popen(['notepad.exe', filep])

#Функция сохраниения и открытия прогресса
def save_data():
    data = [age_entry.get(), cond_outs_ent.get(), cond_ins_ent.get(), H_ent.get(), B_ent.get(), s_ent.get(), t_ent.get(), Jx_ent.get(), Wminx_ent.get(), Wmaxx_ent.get(), Fx_ent.get()]
    selected_option1 = outside_combox.get()
    selected_option2 = inside_combox.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".clc", filetypes=[("CLC Files", "*.clc")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(f"Option 1: {selected_option1}\n")
            file.write(f"Option 2: {selected_option2}\n")
            for item in data:
                file.write(item + '\n')


def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CLC Files", "*.clc")])
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read().splitlines()

            outside_combox.set(data[0].split(": ")[1] if len(data) > 0 else '')
            inside_combox.set(data[1].split(": ")[1] if len(data) > 1 else '')

            for i, entry in enumerate([age_entry, cond_outs_ent, cond_ins_ent, H_ent, B_ent, s_ent, t_ent, Jx_ent,  Wminx_ent, Wmaxx_ent, Fx_ent], start=2):
                entry.delete(0, tk.END)
                entry.insert(0, data[i] if i < len(data) else '')

def open_table():
    table_path = os.path.join(current_dir, "Table.png")
    subprocess.Popen(["start",'Photo Viewer.exe', table_path], shell=True)

def new_proj():
    table_path = os.path.join(current_dir, "Corrosion_Clc_V_2.0.exe")
    subprocess.Popen(["start", '', table_path], shell=True)

#Создание рабочего окна приложения

root = tk.Tk()
root['bg'] = '#fafafa'
root.title('Расчет геометрических параметров тюбингов с коррозией')
root.geometry('840x500+400+200')
root.iconbitmap(default='Ico.ico')
root.resizable(False, False)
validate_input = root.register(on_validate_input)
root.option_add("*tearOff", False)

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Инструкция.pdf")

def Help():
    subprocess.Popen(["start", '', file_path], shell=True)


main_menu = tk.Menu()
root.config(menu=main_menu)
file_menu = tk.Menu()
help_menu = tk.Menu()
file_menu.add_command(label="Создать", command=new_proj)
file_menu.add_command(label="Сохранить", command=save_data)
file_menu.add_command(label="Открыть", command=load_data)
file_menu.add_command(label="Выйти", command=quit_mainloop)
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Помощь", menu=help_menu)
help_menu.add_command(label="Инструкция", command=Help)
help_menu.add_command(label="Таблица из справочника", command=open_table)


#Рамки с исходными данными и результатами

ini_frame = tk.LabelFrame(master=root, relief='ridge',bd=2, pady=10, padx=3, text='Исходные данные')
ini_frame.place(width=400, height=500, x=0, y=0)
post_frame = tk.LabelFrame(master=root, relief='ridge', bd=2, pady=10, padx=3, text='Результаты расчета')
post_frame.place(width=440, height=500, x=400, y=0)
separator = ttk.Separator(post_frame, orient="horizontal")
separator.grid(row = 13, column = 0, sticky="ew", pady = 5)

#Функция расчета возраста тоннеля

def calc_age(event):
    bld_year = int(float(age_entry.get()))
    today = date.today()
    now_year = today.year
    age = now_year - bld_year
    d = age % 10
    e = age % 100
    if e >= 11 and e <= 20:
        k = ' лет'
    elif d >= 2 and d <= 4:
        k =  ' года'
    elif  d <= 1:
        k = ' год'
    else:
        k =  ' лет'
    if age < 0 and bld_year > now_year:
        messagebox.showerror("Ошибка", "Проверьте возраст тоннеля")
        age_entry.delete(0, tk.END)
        pass
    else:
        age_res_lbl.config(text=f'Возраст тоннеля: {age} {k}')

    return age, now_year, k

#Интерфейс расчета возраста тоннеля

age_lbl = tk.Label(ini_frame, text='Введите год постройки тоннеля:')
age_lbl.grid(row = 0, column = 0, sticky='w')
age_entry = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
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
        'Почва (p=200…1000 Ом*см)': 0.06,
        'Почва (p=1000…2000 Ом*см)': 0.03
    }

outside_keys_list = list(outside_the_lining.keys())

#Внешняя среда

def proc_out(event):
    selected_value_outs = outside_combox.get()
    cond_outs = int(float(cond_outs_ent.get()))
    if selected_value_outs == 'Почва (ρ=200…1000 Ом*см)':
        m = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (cond_outs - 1000)
        outside_the_lining[selected_value_outs] = round(m ,4)
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')
    else:
        n = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (cond_outs - 2000)
        outside_the_lining[selected_value_outs] = round(n ,4)
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')

def on_outcomb_selected(event):
    selected_value_outs = outside_combox.get()
    if selected_value_outs == 'Почва (p=200…1000 Ом*см)':
        outside_the_lining[selected_value_outs] = 0.06
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')
        cond_outs_ent.config(state='normal')
        cond_outs_ent.focus()
        cond_outs_ent.delete(0, tk.END)
    elif selected_value_outs == 'Почва (p=1000…2000 Ом*см)':
        outside_the_lining[selected_value_outs] = 0.03
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')
        cond_outs_ent.config(state='normal')
        cond_outs_ent.focus()
        cond_outs_ent.delete(0, tk.END)
    else:
        cond_outs_ent.delete(0, tk.END)
        cond_outs_ent.config(state='disabled')
        result_label_outs.config(text=f'Внешняя среда: {selected_value_outs} | {outside_the_lining[selected_value_outs]} мм/год')


#Интерфейс выпадающего списка внешней среды
outside_combox_lbl = tk.Label(ini_frame, text='Определите внешнюю среду:')
outside_combox_lbl.grid(row = 1, column = 0, sticky='w')
outside_combox=ttk.Combobox(ini_frame, values=outside_keys_list, width=25, state='readonly')
outside_combox.grid(row = 1, column = 1, sticky='w')
result_label_outs = tk.Label(post_frame, text='')
result_label_outs.grid(row = 1, column = 0, sticky='w')
cond_outs_lbl = tk.Label(ini_frame, text='Введите значение \n электропроводности:')
cond_outs_lbl.grid(row = 2, column = 0, sticky='w')
cond_outs_ent = tk.Entry(ini_frame, width=10, bg="white", state='disabled', validate="key", validatecommand=(validate_input, "%P"))
cond_outs_ent.grid(row = 2, column = 1, sticky='w')
cond_outs_ent.bind('<Return>', proc_out)
cond_outs_ent.bind('<FocusOut>', proc_out)
outside_combox.bind('<<ComboboxSelected>>', on_outcomb_selected)



# Внутренняя среда

#Перечень исходных параметров из таблиц для расчёта
inside_the_lining = {
        'Атмосфера чистая': 0.025,
        'Атмосфера загрязненная (городская)': 0.125,
        'Атмосфера, обогащенная SO2': 0.79,
        'Вода морская, спокойная': 0.125,
        'Вода морская (скорость течения 6-10 м/с)': 1.25,
        'Почва (p=200…1000 Ом*см)': 0.06,
        'Почва (p=1000…2000 Ом*см)': 0.03
    }

inside_keys_list = list(inside_the_lining.keys())

def proc_ins(event):
    selected_value_ins = inside_combox.get()
    cond_ins = int(float(cond_ins_ent.get()))
    if selected_value_ins == 'Почва (p=200…1000 Ом*см)':
        x = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (cond_ins - 1000)
        inside_the_lining[selected_value_ins] = round(x ,4)
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {inside_the_lining[selected_value_ins]} мм/год')
    else:
        y = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (cond_ins - 2000)
        inside_the_lining[selected_value_ins] = round(y ,4)
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {inside_the_lining[selected_value_ins]} мм/год')


def on_inscomb_selected(event):
    selected_value_ins = inside_combox.get()
    if selected_value_ins == 'Почва (p=200…1000 Ом*см)':
        inside_the_lining[selected_value_ins] = 0.06
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {outside_the_lining[selected_value_ins]} мм/год')
        cond_ins_ent.config(state='normal')
        cond_ins_ent.focus()
        cond_ins_ent.delete(0, tk.END)
    elif selected_value_ins == 'Почва (p=1000…2000 Ом*см)':
        inside_the_lining[selected_value_ins] = 0.03
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {outside_the_lining[selected_value_ins]} мм/год')
        cond_ins_ent.config(state='normal')
        cond_ins_ent.focus()
        cond_ins_ent.delete(0, tk.END)
    else:
        result_label_ins.config(text=f'Внутренняя среда: {selected_value_ins} | {outside_the_lining[selected_value_ins]} мм/год')
        cond_ins_ent.delete(0, tk.END)
        cond_ins_ent.config(state='disabled')



# Интерфейс выпадающего списка внешней среды
inside_combox_lbl = tk.Label(ini_frame, text='Определите внутреннюю среду:')
inside_combox_lbl.grid(row=3, column=0, sticky='w')
inside_combox = ttk.Combobox(ini_frame, values=outside_keys_list, width=25, state='readonly')
inside_combox.grid(row=3, column=1, sticky='w')
result_label_ins = tk.Label(post_frame, text='')
result_label_ins.grid(row=3, column=0, sticky='w')
cond_ins_lbl = tk.Label(ini_frame, text='Введите значение \n электропроводности:')
cond_ins_lbl.grid(row=4, column=0, sticky='w')
cond_ins_ent = tk.Entry(ini_frame, width=10, bg="white", state='disabled', validate="key", validatecommand=(validate_input, "%P"))
cond_ins_ent.grid(row=4, column=1, sticky='w')
cond_ins_ent.bind('<Return>', proc_ins)
cond_ins_ent.bind('<FocusOut>', proc_ins)
inside_combox.bind('<<ComboboxSelected>>', on_inscomb_selected)

# Расчет геометрических параметров

def Clc_t_and_s_value(event):
    H = float(H_ent.get())
    result_H_lbl.config(text=f'Высота блока H: {round(H ,2)} мм')
    B = float(B_ent.get())
    result_B_lbl.config(text=f'Ширина блока B: {round(B ,2)} мм')
    t = float(t_ent.get())
    s = float(s_ent.get())
    Jx_ult = float(Jx_ent.get())
    Wmin, Wmax, Fx = [Wminx_ent.get(), Wmaxx_ent.get(), Fx_ent.get()]
    x1 = ((2 * t * H ** 2) + ((B - 2 * t) * s ** 2)) / (2 * ((2 * t * H) + (B - 2 * t) * s))
    x2 = H - x1
    Jx = (((B * (x1 ** 3)) - ((B - 2 * t) * ((x1 - s) ** 3)) + (2 * t * (x2 ** 3))) / 3) / 10000
    # Проверка совпадения значений моментов инерции
    Chek = (Jx == Jx_ult)
    # Цикл подбора толщин по исходному моменту инерции
    n = 0

    while Chek == False:
        if n == 1000000000:
            clear_post([result_H_lbl, result_B_lbl, result_t_lbl, result_s_lbl, result_Jx_lbl, result_Jxn_lbl, result_Wminn_lbl, result_Wmaxn_lbl, result_Fnn_lbl])
            messagebox.showerror("Ошибка", "Проверьте правильность исходных данных")
            break
        else:
            if Jx < Jx_ult:
                t = t + 0.000001
                s = s + 0.000001
            else:
                t = t - 0.000001
                s = s - 0.000001
        x1 = ((2 * t * H ** 2) + ((B - 2 * t) * s ** 2)) / (2 * ((2 * t * H) + (B - 2 * t) * s))
        x2 = H - x1
        Jx = (((B * (x1 ** 3)) - ((B - 2 * t) * ((x1 - s) ** 3)) + (2 * t * (x2 ** 3))) / 3) / 10000
        n= n+1
        Chek = (round(Jx, 3) == Jx_ult)
    if n == 1000000000:
        clear_post(
            [result_H_lbl, result_B_lbl, result_t_lbl, result_s_lbl, result_Jx_lbl, result_Jxn_lbl, result_Wminn_lbl,
             result_Wmaxn_lbl, result_Fnn_lbl])
    else:
        result_t_lbl.config(text=f'Толщина ребра блока t: {round(t ,2)} мм')
        result_s_lbl.config(text=f'Толщина спинки блока s: {round(s ,2)} мм')
        result_Jx_lbl.config(text=f'Момент инерции блока Jx: {round(Jx, 2)} см⁴')
        result_Wmaxx_lbl.config(text=f'Максимальный момент сопротивления блока нетто: {Wmax} см³')
        result_Wminx_lbl.config(text=f'Минимальный момент сопротивления блока нетто: {Wmin} см³')
        result_Fx_lbl.config(text=f'Площадь поперечного сечения блока брутто: {Fx} см²')

        return s, t, Jx


def clc_new_geom(event):
    H = float(H_ent.get())
    B = float(B_ent.get())
    Wmin, Wmax, Fx = [Wminx_ent.get(), Wmaxx_ent.get(), Fx_ent.get()]
    s, t, Jx = Clc_t_and_s_value(event)
    age, now_year, k = calc_age(event)
    value_outs = outside_the_lining[outside_combox.get()]
    losses_outside = age * value_outs
    value_ins = inside_the_lining[inside_combox.get()]
    losses_inside = age * value_ins
    Hn = H - losses_outside - losses_inside
    Bn = B
    tn = t - losses_inside
    sn = s - losses_inside
    # Расчет расстояний до центра тяжести от левого и правого края сечения
    x1n = ((2 * tn * Hn ** 2) + ((Bn - 2 * tn) * sn ** 2)) / (2 * ((2 * tn * Hn) + (Bn - 2 * tn) * sn))
    x2n = Hn - x1n
    # Расчет нового момента инерции
    Jxn = (((Bn * (x1n ** 3)) - ((Bn - 2 * tn) * ((x1n - sn) ** 3)) + (2 * tn * (x2n ** 3))) / 3) / 10000
    result_Jxn_lbl.config(text=f'Момент инерции ржавого блока: {round(Jxn, 2)} см⁴')
    # Расчет моментов сопротивления
    Wminn = Jxn / (x2n / 10)
    Wmaxn = Jxn / (x1n / 10)
    result_Wminn_lbl.config(text=f'Минимальный момент сопротивления ржавого блока: {round(Wminn, 2)} см³')
    result_Wmaxn_lbl.config(text=f'Максимальный момент сопротивления ржавого блока: {round(Wmaxn, 2)} см³')
    Ftest = (2 * H * t) + ((B - 2 * t) * s)
    Fntest = (2 * Hn * tn) + ((Bn - 2 * tn) * sn)
    delta = Fntest/Ftest
    Fnn = float(Fx)*delta
    result_Fnn_lbl.config(text=f'Площадь поперечного сечения ржавого блока: {round(Fnn, 2)} см²')
    doc_but.config(state='normal')
    wr_result = f'''    Особенностью, принятой в расчете, для материала чугуна является учет коррозии. Толщина слоя, подвергнувшаяся коррозионному воздействию, рассчитывалась согласно требованиям СП 28.13330.2017 «СНиП 2.03.11-85 Защита строительных конструкций от коррозии» и таблицы справочника по чугунному литью [1], представленной на Рис.
    Исходные данные для расчета:
Высота блока H: {round(H ,2)} мм;
Ширина блока B: {round(B ,2)} мм;
Толщина ребра блока t: {round(t ,2)} мм;
Толщина спинки блока s: {round(s ,2)} мм;
Момент инерции блока нетто Jx: {round(Jx, 2)} см^4
Минимальный момент сопротивления блока нетто Wmin: {Wmin} см^3
Максимальный момент сопротивления блока нетто Wmax: {Wmax} см^3
Площадь поперечного сечения блока брутто Fx: {Fx} см^2
    Порядок расчета:
1. Вычисление возраста тоннеля: 
Текущий год – Год строительства = {now_year} - {age_entry.get()} = {age} {k}
2. Вычисление величины коррозионного слоя на внутренней части тюбинга:
Потери металла * Возраст тоннеля = {value_ins} * {age} = {round(losses_inside,3)} мм
3. Вычисление величины коррозионного слоя на внешней части тюбинга:
Потери металла * Возраст = {value_outs} * {age} = {round(losses_outside,3)} мм
Геометрические характеристики чугунных тюбингов с учетом коррозионного воздействия:
Момент инерции ржавого блока: {round(Jxn, 2)} см^4
Минимальный момент сопротивления ржавого блока: {round(Wminn, 2)} см^3
Максимальный момент сопротивления ржавого блока: {round(Wmaxn, 2)} см^3
Площадь поперечного сечения ржавого блока: {round(Fnn, 2)} см^2

    Библиографический список:
1. Гиршович, Н. Г. Справочник по чугунному литью / Н. Г. Гиршович. – Издание 3-е, переработанное и дополненное. – Ленинград : "Машиностроение", 1978. – 758 с.'''
    return wr_result


def submit_form():
    entry_list = [age_entry, H_ent, B_ent, s_ent, t_ent, Jx_ent, inside_combox, outside_combox, Wminx_ent, Wmaxx_ent, Fx_ent]
    if check_entries_filled(entry_list):
        clc_new_geom(0)
        pass


geom_title_lbl = tk.Label(ini_frame, text='Введите геометрические параметры блока:')
geom_title_lbl.grid(row=5, column=0, sticky='w', columnspan=2)
H_lbl = tk.Label(ini_frame, text='Высота блока H (мм):')
H_lbl.grid(row=6, column=0, sticky='w')
B_lbl = tk.Label(ini_frame, text='Ширина блока B (мм):')
B_lbl.grid(row=7, column=0, sticky='w')
t_lbl = tk.Label(ini_frame, text='Толщина ребра блока t (мм):')
t_lbl.grid(row=8, column=0, sticky='w')
s_lbl = tk.Label(ini_frame, text='Толщина спинки блока s (мм):')
s_lbl.grid(row=9, column=0, sticky='w')
Jx_lbl = tk.Label(ini_frame, text='Момент инерции блока нетто (см⁴):')
Jx_lbl.grid(row=10, column=0, sticky='w')
Wminx_lbl = tk.Label(ini_frame, text='Минимальный момент \n сопротивления блока нетто (см³):', justify="left")
Wminx_lbl.grid(row=11, column=0, sticky='w')
Wmaxx_lbl = tk.Label(ini_frame, text='Максимальный момент \n сопротивления блока нетто (см³):', justify="left")
Wmaxx_lbl.grid(row=12, column=0, sticky='w')
Fx_lbl = tk.Label(ini_frame, text='Площадь поперечного \n сечения блока брутто (см²):', justify="left")
Fx_lbl.grid(row=13, column=0, sticky='w')
H_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
H_ent.grid(row=6, column=1, sticky='w', pady = 8)
B_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
B_ent.grid(row=7, column=1, sticky='w')
t_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
t_ent.grid(row=8, column=1, sticky='w', pady = 8)
s_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
s_ent.grid(row=9, column=1, sticky='w')
Jx_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
Jx_ent.grid(row=10, column=1, sticky='w', pady = 8)
Wminx_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
Wminx_ent.grid(row=11, column=1, sticky='sw')
Wmaxx_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
Wmaxx_ent.grid(row=12, column=1, sticky='sw')
Fx_ent = tk.Entry(ini_frame, width=10, bg="white", validate="key", validatecommand=(validate_input, "%P"))
Fx_ent.grid(row=13, column=1, sticky='sw')
result_geom_lbl = tk.Label(post_frame, text='Геометрические параметры блока обделки:')
result_geom_lbl.grid(row=4, column=0, sticky='w', columnspan=2)
result_H_lbl = tk.Label(post_frame, text='')
result_H_lbl.grid(row=5, column=0, sticky='w')
result_B_lbl = tk.Label(post_frame, text='')
result_B_lbl.grid(row=6, column=0, sticky='w')
result_t_lbl = tk.Label(post_frame, text='')
result_t_lbl.grid(row=7, column=0, sticky='w')
result_s_lbl = tk.Label(post_frame, text='')
result_s_lbl.grid(row=8, column=0, sticky='w')
result_Jx_lbl = tk.Label(post_frame, text='')
result_Jx_lbl.grid(row=9, column=0, sticky='w')
result_Wminx_lbl = tk.Label(post_frame, text='')
result_Wminx_lbl.grid(row=10, column=0, sticky='w')
result_Wmaxx_lbl = tk.Label(post_frame, text='')
result_Wmaxx_lbl.grid(row=11, column=0, sticky='w')
result_Fx_lbl = tk.Label(post_frame, text='')
result_Fx_lbl.grid(row=12, column=0, sticky='w')

result_Jxn_lbl = tk.Label(post_frame, text='')
result_Jxn_lbl.grid(row=14, column=0, sticky='w')
result_Wmaxn_lbl = tk.Label(post_frame, text='')
result_Wmaxn_lbl.grid(row=15, column=0, sticky='w')
result_Wminn_lbl = tk.Label(post_frame, text='')
result_Wminn_lbl.grid(row=16, column=0, sticky='w')
result_Fnn_lbl = tk.Label(post_frame, text='')
result_Fnn_lbl.grid(row=17, column=0, sticky='nw')


#Кнопки
clc_but = tk.Button(ini_frame, text='Расчет', command=submit_form, bg= '#63B8FF')
clc_but.grid(row=14, column=0, sticky='w',pady=15, padx=5)
clear_button = tk.Button(ini_frame, text="Очистить поля", command=lambda: clear_entries([age_entry, H_ent, B_ent, s_ent, t_ent, Jx_ent, cond_ins_ent, cond_outs_ent, Wminx_ent, Wmaxx_ent, Fx_ent],
                                                                                        [age_res_lbl, result_H_lbl, result_B_lbl, result_t_lbl, result_s_lbl, result_Jx_lbl, result_Jxn_lbl, result_Wminn_lbl, result_Wmaxn_lbl, result_Fnn_lbl, result_label_outs, result_label_ins, result_Wminx_lbl, result_Wmaxx_lbl, result_Fx_lbl],
                                                                                        [outside_combox, inside_combox],
                                                                                        [cond_outs_ent, cond_ins_ent, doc_but]), bg= '#F08080')
clear_button.grid(row=14, column=0, sticky='w',pady=15, padx=60)
doc_but = tk.Button(post_frame, text='Сформировать отчет', command=save_file, bg= '#5CB274', state='disabled')
doc_but.grid(row=18, column=0, sticky='w',pady=35, padx=5)



root.mainloop()
