from tkinter import*
tk = Tk()
tk.geometry("390x570")

def BC_click():
    ent.delete(0, END)

def B1_click():
    ent.insert(END,"1")
    
def B2_click():
    ent.insert(END,"2")

def B3_click():
    ent.insert(END,"3")

def B4_click():
    ent.insert(END,"4")

def B5_click():
    ent.insert(END,"5")

def B6_click():
    ent.insert(END,"6")

def B7_click():
    ent.insert(END,"7")

def B8_click():
    ent.insert(END,"8")

def B9_click():
    ent.insert(END,"9")

def B0_click():
    ent.insert(END,"0")

def Point_click():
    ent.insert(END,".")

def Plus_click():
    global a, b
    a = float(ent.get())
    b = "+"
    ent.delete(0, END)

def Minus_click():
    global a, b
    a = float(ent.get())
    b = "-"
    ent.delete(0, END)

def Multiply_click():
    global a, b
    a = float(ent.get())
    b = "*"
    ent.delete(0, END)

def Divide_click():
    global a, b
    a = float(ent.get())
    b = "/"
    ent.delete(0, END)

def Equal_click():
    global a, b
    c = float(ent.get())
    ent.delete(0,END)
    if b == "+":
        ent.insert(END, a + c)
    elif b == "-":
        ent.insert(END, a - c)
    elif b == "*":
        ent.insert(END, a * c)
    elif b == "/":
        if (c != 0) and (a % c == 0) :
            ent.insert(END, int (a / c))
        elif c != 0:
            ent.insert(END, a / c)
        else:
            ent.insert(END,"ERROR")
    
ent = Entry(justify = "right", font = "Consolas 14 bold")
ent.place(x = 30, y = 30, width = 330, height = 60)

BC = Button(text = "C", font = "14", command = BC_click)
BC.place(x = 30, y = 120, width = 150, height = 60)

Equal = Button(text = "=", font = "14", command = Equal_click)
Equal.place(x = 210, y = 120, width = 150, height = 60)

B7 = Button(text = "7", font = "14", command = B7_click)
B7.place(x = 30, y = 210, width = 60, height = 60)

B8 = Button(text = "8", font = "14", command = B8_click)
B8.place(x = 120, y = 210, width = 60, height = 60)

B9 = Button(text = "9", font = "14", command = B9_click)
B9.place(x = 210, y = 210, width = 60, height = 60)

Divide = Button(text = "/", font = "14", command = Divide_click)
Divide.place(x = 300, y = 210, width = 60, height = 60)

B4 = Button(text = "4", font = "14", command = B4_click)
B4.place(x = 30, y = 300, width = 60, height = 60)

B5 = Button(text = "5", font = "14", command = B5_click)
B5.place(x = 120, y = 300, width = 60, height = 60)

B6 = Button(text = "6", font = "14", command = B6_click)
B6.place(x = 210, y = 300, width = 60, height = 60)

Multiply = Button(text = "*", font = "14", command = Multiply_click)
Multiply.place(x = 300, y = 300, width = 60, height = 60)

B1 = Button(text = "1", font = "14", command = B1_click)
B1.place(x = 30, y = 390, width = 60, height = 60)

B2 = Button(text = "2", font = "14", command = B2_click)
B2.place(x = 120, y = 390, width = 60, height = 60)

B3 = Button(text = "3", font = "14", command = B3_click)
B3.place(x = 210, y = 390, width = 60, height = 60)

Minus= Button(text = "-", font = "14", command = Minus_click)
Minus.place(x = 300, y = 390, width = 60, height = 60)

B0 = Button(text = "0", font = "14", command = B0_click)
B0.place(x = 30, y = 480, width = 150, height = 60)

Point = Button(text = ".", font = "14", command = Point_click)
Point.place(x = 210, y = 480, width = 60, height = 60)

Plus= Button(text = "+", font = "14", command = Plus_click)
Plus.place(x = 300, y = 480, width = 60, height = 60)
