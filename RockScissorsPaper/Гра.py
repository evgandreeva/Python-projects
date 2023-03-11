from tkinter import*
import random

tk = Tk()
tk.geometry("500x500")

def click():
    comp_choise = random.randint(1,3)
    canvas = Canvas(tk, width = 300, height = 300)
    canvas.place(x = 300, y = 200)
    if comp_choise == 1:
        lbl2 = Label(text = "Камінь")
        lbl2.place (x = 250, y = 100, width = 70, height = 40)
    elif comp_choise == 2:
        lbl2 = Label(text = "Ножиці")
        lbl2.place (x = 250, y = 100, width = 70, height = 40)
    else:
        lbl2 = Label(text = "Папір")
        lbl2.place (x = 250, y = 100, width = 70, height = 40)
        
    if (comp_choise == 1 and var.get() == 1) or (comp_choise == 2 and var.get() == 2) or(comp_choise == 3 and var.get() == 3):
        lbl3 = Label(text = "Нічия", font = "12")
        lbl3.place(x = 150, y = 400, width = 200 , height = 40)
    elif (comp_choise == 1 and var.get() == 2) or (comp_choise == 3 and var.get() == 1) or (comp_choise == 2 and var.get() == 3):
        lbl3 = Label(text = "Комп'ютер переміг!", font = "12")
        lbl3.place(x = 150, y = 400, width = 200 , height = 40)
    elif (comp_choise == 1 and var.get() == 3) or (comp_choise == 2 and var.get() == 1) or (comp_choise == 3 and var.get() == 2):
        lbl3 = Label(text = "Ти переміг!", font = "12")
        lbl3.place(x = 150, y = 400, width = 200 , height = 40)

    if (comp_choise == 3 and var.get() == 2)or (comp_choise == 2 and var.get() == 3):
        canvas.create_image(0, 0, anchor = NW, image = p1)
    elif (comp_choise == 1 and var.get() == 3)or(comp_choise == 3 and var.get() == 1):
        canvas.create_image(0, 0, anchor = NW, image = p3)
    elif (comp_choise == 1 and var.get() == 2) or (comp_choise == 2 and var.get() == 1):
        canvas.create_image(0, 0, anchor = NW, image = p2)
        
p1 = PhotoImage(file = "resources/папір ножиці.png")
p2 = PhotoImage(file = "resources/камінь-ножиці.png")
p3 = PhotoImage(file = "resources/камінь-бумага.png") 

lbl = Label(text = "Твій вибір", font = "Arial 14 bold")
lbl.place(x = 50, y = 30, width = 100, height = 40)

lbl1 = Label(text = "Вибір комп'ютера", font = "Arial 14 bold")
lbl1.place(x = 250, y = 30, width = 200, height = 40)

var = IntVar()
rbt1 = Radiobutton(text = "Камінь",variable = var, value = 1)
rbt1.place(x = 50, y = 100, width = 70, height = 40)

rbt2 = Radiobutton(text = "Ножиці",variable = var, value = 2)
rbt2.place(x = 50, y = 140, width = 75, height = 40)

rbt3 = Radiobutton(text = "Папір",variable = var, value = 3)
rbt3.place(x = 50, y = 180, width = 65, height = 40)

btn = Button(text = "Ввести", font = "Arial 16", command = click)
btn.place(x = 50, y = 250, width = 120, height = 40)
tk.mainloop()