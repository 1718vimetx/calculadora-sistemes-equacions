import tkinter as tk

root = tk.Tk()

root.title("Calculadora amb mètode de Gauss")

root.configure(width=100, height=400)
root.minsize(width=420, height=500)

a1_e = tk.Entry(root, width=10);a1_e.grid(row=0, column=1)
x_label = tk.Label(root, text = "x").grid(row=0, column=2)
plus_label = tk.Label(root, text = "+").grid(row=0,column=3)
b1_e = tk.Entry(root, width=10);b1_e.grid(row=0, column=4)
y_label = tk.Label(root, text = "y").grid(row=0, column=5)
plus_label2 = tk.Label(root, text = "+").grid(row=0,column=6)
c1_e = tk.Entry(root, width=10);c1_e.grid(row=0, column=7)
z_label = tk.Label(root, text = "z").grid(row=0, column=8)
equal_label = tk.Label(root, text = "=").grid(row=0,column=9)
d1_e = tk.Entry(root, width=10);d1_e.grid(row=0, column=10)

a2_e = tk.Entry(root, width=10);a2_e.grid(row=1, column=1)
x2_label = tk.Label(root, text = "x").grid(row=1, column=2)
plus_label3 = tk.Label(root, text = "+").grid(row=1,column=3)
b2_e = tk.Entry(root, width=10);b2_e.grid(row=1, column=4)
y2_label = tk.Label(root, text = "y").grid(row=1, column=5)
plus_label4 = tk.Label(root, text = "+").grid(row=1,column=6)
c2_e = tk.Entry(root, width=10);c2_e.grid(row=1, column=7)
z2_label = tk.Label(root, text = "z").grid(row=1, column=8)
equal_label2 = tk.Label(root, text = "=").grid(row=1,column=9)
d2_e = tk.Entry(root, width=10);d2_e.grid(row=1, column=10)

a3_e = tk.Entry(root, width=10);a3_e.grid(row=2, column=1)
x3_label = tk.Label(root, text = "x").grid(row=2, column=2)
plus_label5 = tk.Label(root, text = "+").grid(row=2,column=3)
b3_e = tk.Entry(root, width=10);b3_e.grid(row=2, column=4)
y3_label = tk.Label(root, text = "y").grid(row=2, column=5)
plus_label6 = tk.Label(root, text = "+").grid(row=2,column=6)
c3_e = tk.Entry(root, width=10);c3_e.grid(row=2, column=7)
z3_label = tk.Label(root, text = "z").grid(row=2, column=8)
equal_label3 = tk.Label(root, text = "=").grid(row=2,column=9)
d3_e = tk.Entry(root, width=10);d3_e.grid(row=2, column=10)

a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3 = "","","","","","","","","","","",""
x, y, z = "-", "-", "-"

entries = [a1_e, b1_e, c1_e, d1_e, a2_e, b2_e, c2_e, d2_e, a3_e, b3_e, c3_e, d3_e]



for en in entries:
    en.bind("<Key>", lambda a: "break")
    en.bind("<Button>", lambda a: "break")

selectedentry = a1_e
selectedentry.focus()


def solve_eq():
    global x, y ,z
    global a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3
    global row1, row2, row3, column1, column2, column3, column4, rows, columns
    for en in entries:
        if en.get() == "":
            en.insert("insert", 0)
    a1 = int(a1_e.get());b1 = int(b1_e.get());c1 = int(c1_e.get());d1 = int(d1_e.get())
    a2 = int(a2_e.get());b2 = int(b2_e.get());c2 = int(c2_e.get());d2 = int(d2_e.get())
    a3 = int(a3_e.get());b3 = int(b3_e.get());c3 = int(c3_e.get());d3 = int(d3_e.get())
    x_sol.config(text="")
    y_sol.config(text="")
    z_sol.config(text="")
    x, y, z = "-", "-", "-"
    x2, y2, z2 = "", "", ""

    row1 = [a1_e, b1_e, c1_e, d1_e]
    row2 = [a2_e, b2_e, c2_e, d2_e]
    row3 = [a3_e, b3_e, c3_e, d3_e]
    rows = [row1, row2, row3]
    column1 = [a1_e, a2_e, a3_e]
    column2 = [b1_e, b2_e, b3_e]
    column3 = [c1_e, c2_e, c3_e]
    column4 = [d1_e, d2_e, d3_e]
    columns = [column1, column2, column3, column4]
    zeros = []

    for a in rows:
        zeros = []
        for b in a:
            if int(b.get()) == 0:
                zeros.append(b)
        if len(zeros) > 3:
            if zeros[3] in a:
                a.remove(zeros[3])
        if len(zeros) > 2:
            if zeros[2] in a:
                a.remove(zeros[2])
        if len(zeros) > 1:
            if zeros[1] in a:
                a.remove(zeros[1])
        if len(zeros) > 0:
            if zeros[0] in a:
                a.remove(zeros[0])
        if len(a) == 0:
            x_sol.config(text="Introdueix un valor diferent a zero per algun coecient de l'equació")
            return
        if len(a) == 2:
            if a[1] in column4:
                if a[0] in column1:
                    if x == "-":
                        x = int(column4[column1.index(a[0])].get())/int(a[0].get())
                    else:
                        x2 = int(column4[column1.index(a[0])].get())/int(a[0].get())
                        if x2 != x:
                            x_sol.config(text="L'equació no té solució")
                            return
                elif a[0] in column2:
                    if y == "-":
                        y = int(column4[column2.index(a[0])].get())/int(a[0].get())
                    else:
                        y2 = int(column4[column2.index(a[0])].get())/int(a[0].get())
                        if y2 != y:
                            x_sol.config(text="L'equació no té solució")
                            return
                elif a[0] in column3:
                    if z == "-":
                        z = int(column4[column3.index(a[0])].get())/int(a[0].get())
                    else:
                        z2 = z = int(column4[column3.index(a[0])].get())/int(a[0].get())
                        if z2 != z:
                            x_sol.config(text="L'equació no té solució")
                            return
            else:
                print()
            print("--------")
            print(x)
            print(y)
            print(z)

    b4 = a3*b2 - a2*b3
    c4 = a3*c2 - a2*c3
    d4 = a3*d2 - a2*d3

    b5 = a2*b1 - a1*b2
    c5 = a2*c1 - a1*c2
    d5 = a2*d1 - a1*d2

    c6 = b4*c5 - b5*c4
    d6 = b4*d5 - b5*d4

    z = d6/c6
    y = (d5 - c5*z)/b5
    x = (d1 - b1*y - c1*z)/a1

    
    x_sol.config(text="x = " + str(x))
    y_sol.config(text="y = " + str(y))
    z_sol.config(text="z = " + str(z))


def goleft():
    global selectedentry
    global entries
    if entries.index(selectedentry) != 0:
        selectedentry = entries[entries.index(selectedentry)-1]
    else:
        selectedentry = entries[len(entries)-1]
    selectedentry.focus()
   
def goright():
    global selectedentry
    global entries
    if entries.index(selectedentry) < (len(entries)-1):
        selectedentry = entries[entries.index(selectedentry)+1]
    else:
        selectedentry = entries[0]
    selectedentry.focus()

def button_click(n):
    selectedentry.insert("insert", n)

def backspace():
    if len(selectedentry.get()) > 0:
        if selectedentry.get()[-1] == " ":
            selectedentry.delete(len(selectedentry.get())-3, "end")
        else:
            selectedentry.delete(len(selectedentry.get())-1, "end")

button_num1 = tk.Button(root, text="1",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(1)).grid(row=7, column=0, columnspan=3, sticky="we")
button_num2 = tk.Button(root, text="2",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(2)).grid(row=7, column=3, columnspan=3, sticky="we")
button_num3 = tk.Button(root, text="3",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(3)).grid(row=7, column=6, columnspan=3, sticky="we")
button_num4 = tk.Button(root, text="4",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(4)).grid(row=6, column=0, columnspan=3, sticky="we")
button_num5 = tk.Button(root, text="5",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(5)).grid(row=6, column=3, columnspan=3, sticky="we")
button_num6 = tk.Button(root, text="6",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(6)).grid(row=6, column=6, columnspan=3, sticky="we")
button_num7 = tk.Button(root, text="7",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(7)).grid(row=5, column=0, columnspan=3, sticky="we")
button_num8 = tk.Button(root, text="8",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(8)).grid(row=5, column=3, columnspan=3, sticky="we")
button_num9 = tk.Button(root, text="9",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(9)).grid(row=5, column=6, columnspan=3, sticky="we")
button_num0 = tk.Button(root, text="0",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click(0)).grid(row=8, column=0, columnspan=3, sticky="we")

backspacebutton = tk.Button(root, text="<",  fg="black", bg="#D2DEEE", padx=40, pady=30, command=backspace).grid(row=5, column=9, columnspan=3, sticky="we")
enterbutton = tk.Button(root, text="Resoldre", fg="black", bg="#D2DEEE", padx=40, pady=30, command=solve_eq).grid(row=8, column=9, columnspan=3, sticky="we")

dividebutton = tk.Button(root, text="/", fg="black", bg="#D2DEEE", padx=40, pady=30, command="").grid(row=7, column=9, columnspan=3, sticky="we")
minusbutton = tk.Button(root, text="-", fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click("-")).grid(row=6, column=9, columnspan=3, sticky="we")

goleftb = tk.Button(root, text="<--", fg="black", bg="#D2DEEE", padx=40, pady=30, command=goleft).grid(row=8, column=3, columnspan=3, sticky="we")
gorightb = tk.Button(root, text="-->", fg="black", bg="#D2DEEE", padx=40, pady=30, command=goright).grid(row=8, column=6, columnspan=3, sticky="we")

x_sol = tk.Label(root, text="");x_sol.grid(row=9, column=0, columnspan = 12, sticky="we")
y_sol = tk.Label(root, text="");y_sol.grid(row=10, column=0, columnspan = 12, sticky="we")
z_sol = tk.Label(root, text="");z_sol.grid(row=11, column=0, columnspan = 12, sticky="we")


root.mainloop()
