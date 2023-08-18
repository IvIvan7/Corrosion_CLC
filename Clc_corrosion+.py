# Создание окна
import tkinter as tk
import tkinter.filedialog as fd
window = tk.Tk()
window['bg'] = '#fafafa'
window.title('Расчет геометрических параметров тюбингов с коррозией')
window.geometry('1070x650')
window.resizable(False, False)

#Рамки расоложения виджетов
frm_form = tk.Frame()
frm_form.pack(fill=tk.BOTH, expand=True)
frm_form1 = tk.Frame(master=frm_form)
frm_form1.grid(row=0, column=0, sticky='w', padx= 10)
frm_form2 = tk.Frame(master=frm_form)
frm_form2.grid(row=1, column=0, sticky='w', padx= 10)
frm_form3 = tk.Frame(master=frm_form)
frm_form3.grid(row=2, column=0, sticky='w', padx= 10)
frm_form4 = tk.Frame(master=frm_form)
frm_form4.grid(row=0, column=1, sticky='w', padx=30)
frm_form5 = tk.Frame(master=frm_form)
frm_form5.grid(row=1, column=1, sticky='w', padx=30)
frm_form6 = tk.Frame(master=frm_form)
frm_form6.grid(row=2, column=1, sticky='w', padx=30)

# Расчет возраста тоннеля

#Функция расчета
def calc_age ():
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
    age_res_val['text'] = str(age) + k
    return age

#Взаимодействие с пользователем
age_lbl = tk.Label(master=frm_form1, text='Введите год постройки тоннеля:')
age_lbl.grid(row=0, column=0, pady=10, padx=1, sticky="w")
age_entry = tk.Entry(master=frm_form1, width=10, bg="yellow")
age_entry.grid(row=0, column=1, pady=10, padx=1, sticky="w")
age_entry.focus()
age_res_lbl = tk.Label(master=frm_form1, text='Возраст тоннеля:')
age_res_lbl.grid(row=0, column=4, pady=10, padx=1)
age_res_val = tk.Label(master=frm_form1, text='0', relief=tk.GROOVE, borderwidth=2)
age_res_val.grid(row=0, column=5, pady=10, padx=1)
btn_convert1 = tk.Button(
master=frm_form1,
text="\N{RIGHTWARDS BLACK ARROW}",
command= calc_age)
btn_convert1.grid(row=0, column=3, pady=1)

# Расчет потерь металла по внешней стороне

#Функция расчета потерь вне
def gr1():
    conductivity = float(cond1_entry.get())
    if conductivity > 0:
        m = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (conductivity - 1000)
    else:
        m = 0.06
    val_out_res_val['text'] = f"{round(m, 3)}"
    return m


def gr2():
    conductivity = float(cond2_entry.get())
    if conductivity > 0:
        if conductivity > 0:
            n = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (conductivity - 2000)
        else:
            n = 0.03
    val_out_res_val['text'] = f"{round(n, 3)}"
    return n

def outside():
    i = str(var1.get())
    m = gr1()
    n = gr2()

    btn_convert3 = tk.Button(
        master=frm_form2,
        text="\N{Plus Sign}",
        command=gr1)
    btn_convert3.grid(row=6, column=3, pady=1)



    btn_convert4 = tk.Button(
        master=frm_form2,
        text="\N{Plus Sign}",
        command=gr2)
    btn_convert4.grid(row=7, column=3, pady=1)



    outside_the_lining = {
        'Атмосфера чистая': 0.025,
        'Атмосфера загрязненная (городская)': 0.125,
        'Атмосфера, обогащенная SO2': 0.79,
        'Вода морская, спокойная': 0.125,
        'Вода морская (скорость течения 6-10 м/с)': 1.25,
        'Почва (ρ=200…1000 Ом*см)': m,
        'Почва (ρ=1000…2000 Ом*см)': n
    }
    value1 = outside_the_lining[i]
    val_out_res_val['text'] = value1
    return value1

Outs_list = [
    'Атмосфера чистая',
    'Атмосфера загрязненная (городская)',
    'Атмосфера, обогащенная SO2',
    'Вода морская, спокойная',
    'Вода морская (скорость течения 6-10 м/с)',
    'Почва (ρ=200…1000 Ом*см)',
    'Почва (ρ=1000…2000 Ом*см)'
    ]
var1=tk.StringVar(value='0')
env_out_lbl = tk.Label(master=frm_form2, text='Выберите внешнюю среду:')
env_out_lbl.grid(row=0, column=0, sticky="w")
for env in Outs_list:
    env_btn1 = tk.Radiobutton(master=frm_form2, text=env, value=env, variable=var1, command=outside)
    env_btn1.grid(column=0, sticky="w")
cond_lbl1 = tk.Label(master=frm_form2, relief=tk.GROOVE, borderwidth=2, text='Введите величину электропроводности:')
cond_lbl1.grid(row=6, column=1, sticky="w")
entry1_def = tk.StringVar()
entry1_def.set('1000')
cond1_entry = tk.Entry(master=frm_form2, width=10, bg="yellow", textvariable= entry1_def)
cond1_entry.grid(row=6, column=2, pady=10, padx=1, sticky="w")
cond_lbl2 = tk.Label(master=frm_form2, relief=tk.GROOVE, borderwidth=2, text='Введите величину электропроводности:')
cond_lbl2.grid(row=7, column=1, sticky="w")
entry2_def = tk.StringVar()
entry2_def.set('1000')
cond2_entry = tk.Entry(master=frm_form2, width=10, bg="yellow", textvariable= entry2_def)
cond2_entry.grid(row=7, column=2, pady=10, padx=1, sticky="w")
val_out_lbl = tk.Label(master=frm_form2, text='Потери металла на внешней поверхности:')
val_out_lbl.grid(row=0, column=1, sticky="w")
val_out_res_val = tk.Label(master=frm_form2, relief=tk.GROOVE, text='0')
val_out_res_val.grid(row=0, column=2, pady=10, padx=1)
val_out_lbl = tk.Label(master=frm_form2, text='(мм/год)')
val_out_lbl.grid(row=0, column=3, sticky="w")

#Функция расчета потерь внутри
def gr3():
    conductivity = float(cond3_entry.get())
    if conductivity > 0:
        m = 0.13 + ((0.06 - 0.13) / (200 - 1000)) * (conductivity - 1000)
    else:
        m = 0.06
    val_in_res_val['text'] = f"{round(m, 3)}"
    return m

def gr4 ():
    conductivity = float(cond4_entry.get())
    if conductivity > 0:
        n = 0.13 + ((0.06 - 0.03) / (1000 - 2000)) * (conductivity - 2000)
    else:
        n = 0.03
    val_in_res_val['text'] = f"{round(n, 3)}"
    return n

def inside():
    i = str(var2.get())
    m = gr3()
    n = gr4()


    inside_the_lining = {
        'Атмосфера чистая': 0.025,
        'Атмосфера загрязненная (городская)': 0.125,
        'Атмосфера, обогащенная SO2': 0.79,
        'Вода морская, спокойная': 0.125,
        'Вода морская (скорость течения 6-10 м/с)': 1.25,
        'Почва (ρ=200…1000 Ом*см)': m,
        'Почва (ρ=1000…2000 Ом*см)': n
    }
    value2 = inside_the_lining[i]
    val_in_res_val['text'] = value2
    return value2
Ins_list = [
    'Атмосфера чистая',
    'Атмосфера загрязненная (городская)',
    'Атмосфера, обогащенная SO2',
    'Вода морская, спокойная',
    'Вода морская (скорость течения 6-10 м/с)',
    'Почва (ρ=200…1000 Ом*см)',
    'Почва (ρ=1000…2000 Ом*см)'
    ]
var2=tk.StringVar(value='0')
env_in_lbl = tk.Label(master=frm_form3, text='Выберите внутреннюю среду:')
env_in_lbl.grid(row=0, column=0, sticky="w")
for env in Ins_list:
    env_btn2 = tk.Radiobutton(master=frm_form3, text=env, value=env, variable=var2, command=inside)
    env_btn2.grid(column=0, sticky="w")
cond_lbl3 = tk.Label(master=frm_form3, relief=tk.GROOVE, borderwidth=2, text='Введите величину электропроводности:')
cond_lbl3.grid(row=6, column=1, sticky="w")
entry3_def = tk.StringVar()
entry3_def.set('1000')
cond3_entry = tk.Entry(master=frm_form3, width=10, bg="yellow", textvariable= entry3_def)
cond3_entry.grid(row=6, column=2, pady=10, padx=1, sticky="w")
cond_lbl4 = tk.Label(master=frm_form3, relief=tk.GROOVE, borderwidth=2, text='Введите величину электропроводности:')
cond_lbl4.grid(row=7, column=1, sticky="w")
entry4_def = tk.StringVar()
entry4_def.set('1000')
cond4_entry = tk.Entry(master=frm_form3, width=10, bg="yellow", textvariable= entry3_def)
cond4_entry.grid(row=7, column=2, pady=10, padx=1, sticky="w")
val_in_lbl = tk.Label(master=frm_form3, text='Потери металла на внутренней поверхности:')
val_in_lbl.grid(row=0, column=1, sticky="w")
val_in_res_val = tk.Label(master=frm_form3, relief=tk.GROOVE, text='0')
val_in_res_val.grid(row=0, column=2)
val_in_lbl = tk.Label(master=frm_form3, text='(мм/год)')
val_in_lbl.grid(row=0, column=3, sticky="w")


#Расчет геометрических характеристик тюбинга по факту
def geom_calc ():
    # Ввод исходных данных
    H = float(entry1.get())
    B = float(entry2.get())
    t = float(entry3.get())
    s = float(entry4.get())
    Jx_ult = float(entry5.get())
    x1 = ((2*t * H**2)+((B-2*t)*s**2))/(2*((2*t*H)+(B-2*t)*s))
    x2 = H-x1
    print('Значение х1 =',x1)
    print('Значение х2 =',x2)
    #Расчет Момента инерции
    Jx = (((B*(x1**3))-((B-2*t)*((x1-s)**3))+(2*t*(x2**3)))/3)/10000
    print('Значение Jх (см4) =',Jx)
    #Проверка софпадения значений моментов инерции
    Chek = (Jx == Jx_ult)
    #Цикл подбора толщин по исхедному моменту инерции#
    while Chek == False:
        t = t + 0.001
        s = s + 0.001
        x1 = ((2 * t * H ** 2) + ((B - 2 * t) * s ** 2)) / (2 * ((2 * t * H) + (B - 2 * t) * s))
        x2 = H - x1
        Jx = (((B * (x1 ** 3)) - ((B - 2 * t) * ((x1 - s) ** 3)) + (2 * t * (x2 ** 3))) / 3) / 10000
        Chek = (Jx >= Jx_ult)
    res_H_lbl['text'] = H
    res_B_lbl['text'] = B
    res_s_lbl['text'] = f"{round(s, 2)}"
    res_t_lbl['text'] = f"{round(t, 2)}"
    print('Значение Jх (см4) =', int(Jx))
    print('Значение t (мм) =', (round(t ,2)))
    print('Значение s (мм) =', (round(s, 2)))
    # Расчет потерь
    losses_outside = calc_age() * outside()
    losses_inside = calc_age() * inside()
    res_outlos_lbl['text'] = f"{round(losses_outside, 2)}"
    res_inlos_lbl['text'] = f"{round(losses_inside, 2)}"
    # Расчет новых значений геометрических характеристик блока
    Hn = H - losses_outside - losses_inside
    Bn = B
    tn = t - losses_inside
    sn = s - losses_inside
    # Расчет расстояний до центра тяжести от левого и правого края сечения
    x1n = ((2 * tn * Hn ** 2) + ((Bn - 2 * tn) * sn ** 2)) / (2 * ((2 * tn * Hn) + (Bn - 2 * tn) * sn))
    x2n = Hn - x1n
    print('Значение х1n =', x1n)
    print('Значение х2n =', x2n)
    # Расчет нового момента инерции
    Jxn = (((Bn * (x1n ** 3)) - ((Bn - 2 * tn) * ((x1n - sn) ** 3)) + (2 * tn * (x2n ** 3))) / 3) / 10000
    res_Jx_lbl['text'] = f"{round(Jxn, 2)}"
    print('Значение Jхn (см4) =', round(Jxn, 2))
    # Расчет моментов сопротивления
    Wminn = Jxn / (x2n / 10)
    Wmaxn = Jxn / (x1n / 10)
    res_Wmin_lbl['text'] = f"{round(Wminn, 2)}"
    res_Wmax_lbl['text'] = f"{round(Wmaxn, 2)}"
    print('Значение Wminn (см3) =', round(Wminn, 2))
    print('Значение Wmaxn (см3) =', round(Wmaxn, 2))
    Fn = (Bn*sn+2*((Hn-sn)*tn))/100
    res_F_lbl['text'] = f"{round(Fn, 2)}"

#Взаимодействие с пользователем по расчету
labels1 = [
    "Введите H : ",
    "Введите B : ",
    "Введите t : ",
    "Введите s : ",
    "Введите Jx : ",
]
labels2 = [
    " (мм)",
    " (мм)",
    " (мм)",
    " (мм)",
    " (см4)",
]

# Цикл для списка ярлыков полей ввода.
for idx1, text1 in enumerate(labels1):
    for idx2, text2 in enumerate(labels2):
        # Создает ярлык с текстом из списка ярлыков.
        label = tk.Label(master=frm_form4, text=text1)
        # Создает текстовое поле которая соответствует ярлыку.
        label2 = tk.Label(master=frm_form4, text=text2)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        label.grid(row=idx1, column=0, sticky="w")
        label2.grid(row=idx2, column=2, sticky="w")
entry1 = tk.Entry(master=frm_form4, width=10, bg="yellow")
entry1.grid(row=0, column=1)
entry2 = tk.Entry(master=frm_form4, width=10, bg="yellow")
entry2.grid(row=1, column=1)
entry3 = tk.Entry(master=frm_form4, width=10, bg="yellow")
entry3.grid(row=2, column=1)
entry4 = tk.Entry(master=frm_form4, width=10, bg="yellow")
entry4.grid(row=3, column=1)
entry5 = tk.Entry(master=frm_form4, width=10, bg="yellow")
entry5.grid(row=4, column=1)
#Поля вывода результатов
labels5 = [
    "Высота блока H' : ",
    "Ширина блока B' : ",
    "Толщина ребра блока t' : ",
    "Толщина спинки блока s' : ",
    "Потери металла на наружней стороне блока : ",
    "Потери металла на внутренней стороне блока : ",
    "Момент инерции Jx` : ",
    "Максимальный момент сопротивления W'max : ",
    "Минимальный момент сопротивления W'min : ",
    "Площадь поперечного сечения F' : ",
    ]

labels6 = [
    " (мм)",
    " (мм)",
    " (мм)",
    " (мм)",
    " (мм)",
    " (мм)",
    " (см4)",
    " (см3)",
    " (см3)",
    " (см2)",
    ]

# Цикл для списка ярлыков полей.
for idx3, text1 in enumerate(labels5):
    for idx4, text2 in enumerate(labels6):
        # Создает ярлык с текстом из списка ярлыков.
        label9 = tk.Label(master=frm_form5, text=text1)
        # Создает текстовое поле которая соответствует ярлыку.
        label10 = tk.Label(master=frm_form5, text=text2)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        label9.grid(row=idx3, column=0, sticky="w")
        label10.grid(row=idx4, column=2, sticky="w")
res_H_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_H_lbl.grid(row=0, column=1, sticky="w")
res_B_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_B_lbl.grid(row=1, column=1, sticky="w")
res_s_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_s_lbl.grid(row=2, column=1, sticky="w")
res_t_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_t_lbl.grid(row=3, column=1, sticky="w")
res_outlos_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_outlos_lbl.grid(row=4, column=1, sticky="w")
res_inlos_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_inlos_lbl.grid(row=5, column=1, sticky="w")
res_Jx_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_Jx_lbl.grid(row=6, column=1, sticky="w")
res_Wmax_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_Wmax_lbl.grid(row=7, column=1, sticky="w")
res_Wmin_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_Wmin_lbl.grid(row=8, column=1, sticky="w")
res_F_lbl = tk.Label(master=frm_form5, relief=tk.GROOVE, borderwidth=2, text='0')
res_F_lbl.grid(row=9, column=1, sticky="w")
#Кнопка расчета
btn_convert6 = tk.Button(
            master=frm_form4,
            text="Расчет",
            command=geom_calc,
            bg= 'PaleGreen')
btn_convert6.grid(row=5, column=1, pady=20)

#Картинка с сечением
#canvas = tk.Canvas(window, height=196, width=300)
#img = tk.PhotoImage(file = 'Сечение.png')
#image = canvas.create_image(0, 0, anchor='nw',image=img)
#canvas.place(x=700, y=430)

#Кнопка удаления введенных данных
def clear():
    age_entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
btn_clear = tk.Button(master=frm_form4, text="Очистить поля", command=clear, bg= 'Coral1')
btn_clear.grid(row=5, column=2, pady=20)

window.mainloop()