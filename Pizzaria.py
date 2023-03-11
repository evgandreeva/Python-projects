from tkinter import*
tk = Tk()
tk.geometry("650x300")

def s1_click(val):
    global y1
    k1 = int(val)
    x1 = float(p1.get())
    y1 = x1 * k1
    y1 = round(y1,2)
    var1.set(rez(y1))
    
def s2_click(val):
    global y2
    k2 = int(val)
    x2 = float(p2.get())
    y2 = x2 * k2
    y2 = round(y2,2)
    var2.set(rez(y2))

def s3_click(val):
    global y3
    k3 = int(val)
    x3 = float(p3.get())
    y3 = x3 * k3
    y3 = round(y3,2)
    var3.set(rez(y3))

def s4_click(val):
    global y4
    k4 = int(val)
    x4 = float(p4.get())
    y4 = x4 * k4
    y4 = round(y4,2)
    var4.set(rez(y4))

def btn_click():
    k = 0
    global y1, y2, y3 ,y4
    if var_ch1.get() == 1:
        k = k + 1
    if var_ch2.get() == 1:
        k = k + 1
    if var_ch3.get() == 1:
        k = k + 1
    if var_ch4.get() == 1:
        k = k + 1
    
    y = y1 + y2 + y3 + y4+k*3
    var5.set(rez(y))

def rez(y):
    if y == int(y):
        return(int(y))
    else:
        return(y)
    
lbl = Label(text = "Найменування", font = "Arial 11 bold")
lbl.place(x = 20, y = 20)

lbl1 = Label(text = "Ціна, грн", font = "Arial 11 bold")
lbl1.place(x = 150, y = 20)

lbl2 = Label(text = "Кількість", font = "Arial 11 bold")
lbl2.place(x = 230, y = 20)

lbl3 = Label(text = "Вартість, грн", font = "Arial 11 bold")
lbl3.place(x = 310, y = 20)

lbl4 = Label(text = "Піцца", font = "Arial 10")
lbl4.place(x = 20, y = 60)

lbl5 = Label(text = "Морозиво", font = "Arial 10")
lbl5.place(x = 20, y = 100)

lbl6 = Label(text = "Тістечко", font = "Arial 10")
lbl6.place(x = 20, y = 140)

lbl7 = Label(text = "Сік", font = "Arial 10")
lbl7.place(x = 20, y = 180)

lbl8 = Label(text = "Вартість замовлення", font = "Arial 11")
lbl8.place(x = 20, y = 220)

lbl9 = Label(text = "Добавки до піци, 3 грн", font = "Arial 11 bold")
lbl9.place(x = 440, y = 20)

# Ціна p1, p2, p3, p4

p1 = Entry(font = "Arial 12", bg = "sky blue", justify = "center")
p1.insert(END,"75")
p1.place(x = 150, y = 60, width = 60, height = 30)

p2 = Entry(font = "Arial 12", bg = "sky blue", justify = "center")
p2.insert(END,"12")
p2.place(x = 150, y = 100, width = 60, height = 30)

p3 = Entry(font = "Arial 12", bg = "sky blue", justify = "center")
p3.insert(END,"16")
p3.place(x = 150, y = 140, width = 60, height = 30)

p4 = Entry(font = "Arial 12", bg = "sky blue", justify = "center")
p4.insert(END,"8")
p4.place(x = 150, y = 180, width = 60, height = 30)

# Вартість c1, c2, c3, c4
var1 = StringVar()
c1 = Label(text = 0, font = "Arial 12", bg = "deep sky blue",textvariable = var1)
c1.place (x = 310, y = 60, width = 60, height = 30)

var2 = StringVar()
c2 = Label(text = 0, font = "Arial 12", bg = "deep sky blue",textvariable = var2)
c2.place (x = 310, y = 100, width = 60, height = 30)

var3 = StringVar()
c3 = Label(text = 0, font = "Arial 12", bg = "deep sky blue",textvariable = var3)
c3.place (x = 310, y = 140, width = 60, height = 30)

var4 = StringVar()
c4 = Label(text = 0, font = "Arial 12", bg = "deep sky blue",textvariable = var4)
c4.place (x = 310, y = 180, width = 60, height = 30)

y1 = 0
y2 = 0
y3 = 0
y4 = 0

var5 = StringVar()
c = Label(text = 0, font = "Arial 12", bg = "deep sky blue",textvariable = var5)
c.place (x = 200, y = 220, width = 60, height = 30)

valuta = Label(text = "грн", font = "Arial 11")
valuta.place (x = 260, y = 220, width = 30, height = 30)

knopka = Button(text = "Розрахувати", font = "Arial 11", command = btn_click)
knopka.place(x = 310, y = 220, width = 100 , height = 35)

# Шкали s1, s2, s3, s4
s1 = Scale(orient = HORIZONTAL, length = 50,from_ = 0,to = 10, command = s1_click)
s1.place(x = 230, y = 50)

s2 = Scale(orient = HORIZONTAL, length = 50,from_ = 0,to = 10, command = s2_click)
s2.place(x = 230, y = 90)

s3 = Scale(orient = HORIZONTAL, length = 50,from_ = 0,to = 10, command = s3_click)
s3.place(x = 230, y = 130)

s4 = Scale(orient = HORIZONTAL, length = 50,from_ = 0,to = 10, command = s4_click)
s4.place(x = 230, y = 170)

# Прапорці
var_ch1 = IntVar()
ch1 = Checkbutton(text = "Майонез", font = "Arial 12", variable = var_ch1)
ch1.place(x = 440, y = 60)

var_ch2 = IntVar()
ch2 = Checkbutton(text = "Кетчуп", font = "Arial 12", variable = var_ch2)
ch2.place(x = 440, y = 100)

var_ch3 = IntVar()
ch3 = Checkbutton(text = "Соус", font = "Arial 12", variable = var_ch3)
ch3.place(x = 440, y = 140)

var_ch4 = IntVar()
ch4 = Checkbutton(text = "Ананаси", font = "Arial 12", variable = var_ch4)
ch4.place(x = 440, y = 180)

tk.mainloop()



