from tkinter import*

tk = Tk()
tk.geometry("300x300")
tk.title("Залізнічні білети")
tk["bg"] = "green"

def btn2():
    global ent,btn2,save,b
    lbl5 = Label(tk,text = ent.get())
    lbl5.place(x = 180, y = 50, width = 70, height = 35)
    b = float(ent.get())
    global window
    window.destroy()

def btn2_k():
    global ent3,ok_btn,kupe,a
    lbl6 = Label(tk,text = ent3.get())
    lbl6.place(x = 180, y = 110, width = 70, height = 35)
    a = float(ent3.get())
    kupe.destroy()
  

def click_plac():
    global window, btn2,save,plac_ent,b
    #window = Tk()
    window = Toplevel(tk)
    window.geometry("300x150")
    window.title("Плацкарт")
    lbl3 = Label(window,text = "Увести ціну плацкарта")
    lbl3.place(x = 0, y = 10, width = 150, height = 40)
    global ent
    ent = Entry(window, justify = "right")
    ent.place(x = 30, y = 60, width = 150, height = 35)
    
    save = Button(window,text = "Save", command= btn2)
    save.place(x = 50, y = 100, width = 40, height = 40)
    plac_ent = ent

def btn_k():
    global kupe, ent3,ok_btn,kupe_ent,a
    kupe = Toplevel(tk)
    kupe.geometry("300x150")
    kupe.title("Купе")
    lbl4 = Label(kupe,text = "Увести ціну купе")
    lbl4.place(x = 0, y = 10, width = 150, height = 40)
    ent3 = Entry(kupe,justify = "right")
    ent3.place(x = 30, y = 60, width = 150, height = 35)
    
    ok_btn = Button(kupe,text = "Save", command= btn2_k)
    ok_btn.place(x = 50, y = 100, width = 40, height = 40)
    
    kupe_ent = ent3
def btn_rizn():
    global rizn, ent3, ent,plac_ent,kupe_ent,b,a
    rizn = Tk()
    rizn.geometry("250x200")
    rizn.title("Різниця")
    answer = a - b
    lbl_rizn = Label(rizn, text = "Різниця = " + str(answer))
    lbl_rizn.place(x = 10, y = 60, width = 150, height = 35)

global kupe_ent,plac_ent

lbl = Label(tk,text = "Ціна квитка плацкарта")
lbl.place(x = 10, y = 50, width = 150, height = 40)

lbl2 = Label(tk,text = "Ціна квитка купе")
lbl2.place(x = 10, y = 110, width = 150, height = 40)

btn = Button(tk,text = "Плацкарт", command= click_plac)
btn.place(x = 10, y = 170, width = 70, height = 40)

btn_kupe = Button(tk,text = "Купе",command= btn_k )
btn_kupe.place(x = 100, y = 170, width = 70, height = 40)

btn_difference = Button(tk,text = "Різниця",command= btn_rizn)
btn_difference.place(x = 190, y = 170, width = 70, height = 40)
