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
row_a, row_b, row_c = "", "", ""

entries = [a1_e, b1_e, c1_e, d1_e, a2_e, b2_e, c2_e, d2_e, a3_e, b3_e, c3_e, d3_e]

def sortfunction(i):
    r = i.count(0)
    if i[3] == 0:
        r -= 1
    return r

def nosol():
    x_sol.config(text="L'equació no té solució")
    y_sol.config(text="")
    z_sol.config(text="")

for en in entries:
    en.bind("<Key>", lambda a: "break")
    en.bind("<Button>", lambda a: "break")

selectedentry = a1_e
selectedentry.focus()

def standard_solve():
    global x, y ,z
    global a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3

    b4 = rowss[2][0]*rowss[1][1] - rowss[1][0]*rowss[2][1]
    c4 = rowss[2][0]*rowss[1][2] - rowss[1][0]*rowss[2][2]
    d4 = rowss[2][0]*rowss[1][3] - rowss[1][0]*rowss[2][3]

    b5 = rowss[1][0]*rowss[0][1] - rowss[0][0]*rowss[1][1]
    c5 = rowss[1][0]*rowss[0][2] - rowss[0][0]*rowss[1][2]
    d5 = rowss[1][0]*rowss[0][3] - rowss[0][0]*rowss[1][3]
    
    c6 = b4*c5 - b5*c4
    d6 = b4*d5 - b5*d4

    if c6 == 0:
        if d6 == 0:
            if (rowss[0][0]*rowss[2][1] - rowss[2][0]*rowss[0][1])*(rowss[2][0]*rowss[1][3] - rowss[1][0]*rowss[2][3])-(rowss[2][0]*rowss[1][1] - rowss[1][0]*rowss[2][1])*(rowss[0][0]*rowss[2][3] - rowss[2][0]*rowss[0][3] == 0):
                if (rowss[1][0]*rowss[0][1] - rowss[0][0]*rowss[1][1])*(rowss[0][0]*rowss[2][3] - rowss[2][0]*rowss[0][3])-(rowss[0][0]*rowss[2][1] - rowss[2][0]*rowss[0][1])*(rowss[1][0]*rowss[0][3] - rowss[0][0]*rowss[1][3] == 0):
                    x_sol.config(text="Sistema compatible indeterminat")
                    y_sol.config(text="")
                    z_sol.config(text="")
                else:
                    x_sol.config(text="L'equació no té solució")
                    y_sol.config(text="")
                    z_sol.config(text="")
            else:
                x_sol.config(text="L'equació no té solució")
                y_sol.config(text="")
                z_sol.config(text="")      
        else:
            x_sol.config(text="L'equació no té solució")
            y_sol.config(text="")
            z_sol.config(text="")
    else:
        if rowss[0][0] != 0 and b5 != 0:
            z = d6/c6
            y = (d5 - c5*z)/b5
            x = (rowss[0][3] - rowss[0][1]*y - rowss[0][2]*z)/rowss[0][0]
            x_sol.config(text="x = " + str(round(x, 8)))
            y_sol.config(text="y = " + str(round(y, 8)))
            z_sol.config(text="z = " + str(round(z, 8)))

def solve_eq():
    global x, y ,z
    global a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3
    global row_a, row_b, row_c, row11, row22, row33, rowss
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
    x2, y2, z2, row_a, row_b, row_c = "", "", "", "", "", ""

    row11 = [a1, b1, c1, d1]
    row22 = [a2, b2, c2, d2]
    row33 = [a3, b3, c3, d3]
    rowss = [row11, row22, row33]

    rowss.sort(key=sortfunction)
    for n in range(3):
        x, y, z = "-", "-", "-"
        x2, y2, z2, row_a, row_b, row_c = "", "", "", "", "", ""
        n += 1
        if n == 2:
            row11[0], row11[1] = row11[1], row11[0]
            row22[0], row22[1] = row22[1], row22[0]
            row33[0], row33[1] = row33[1], row33[0]
        if n == 3:
            row11[0], row11[2] = row11[2], row11[0]
            row22[0], row22[2] = row22[2], row22[0]
            row33[0], row33[2] = row33[2], row33[0]
        for rw in rowss:
            if (rw.count(0) == 2 and rw[3] != 0) or (rw.count(0) == 3 and rw[3] == 0):
                if rw[0] != 0:
                    x = rw[3]/rw[0]
                elif rw[1] != 0:
                    y = rw[3]/rw[1]
                else:
                    z = rw[3]/rw[2]

        for rw in rowss:
            if (rw.count(0) == 1 and rw[3] != 0) or (rw.count(0) == 2 and rw[3] == 0):
                if rw[0] == 0:
                    if y != "-" and z == "-":
                        z = (rw[3] - rw[1]*y)/rw[2]
                    elif y == "-" and z !="-":
                        y = (rw[3] - rw[2]*z)/rw[1]
                    else:
                        if row_a == "":
                            row_a = rw
                        elif row_b == "":
                            row_b = rw
                        else:
                            row_c = rw
                elif rw[1] == 0:
                    if x != "-" and z == "-":
                        z = (rw[3] - rw[0]*x)/rw[2]
                    elif x == "-" and z !="-":
                        x = (rw[3] - rw[2]*z)/rw[0]
                    else:
                        if row_a == "":
                            row_a = rw
                        elif row_b == "":
                            row_b = rw
                        else:
                            row_c = rw
                else:
                    if x != "-" and y == "-":
                        y = (rw[3] - rw[0]*x)/rw[1]
                    elif x == "-" and y !="-":
                        x = (rw[3] - rw[1]*y)/rw[0]
                    else:
                        if row_a == "":
                            row_a = rw
                        elif row_b == "":
                            row_b = rw
                        else:
                            row_c = rw

        
        if row_a != "" and row_b != "":
            if row_a[0] == 0 and row_b[0] == 0:
                if z != "-":
                    z2 = z
                if y != 0:
                    y2 = y
                z = (row_b[1]*row_a[3] - row_a[1]*row_b[3])/(row_b[1]*row_a[2] - row_a[1]*row_b[2])
                y = (row_a[3] - row_a[2]*z)/row_a[1]
                if (z2 != "-" and z2 != z) or (y2 != "-" and y2 != y):
                    nosol()  
            elif row_a[1] == 0 and row_b[1] == 0:
                if z != "-":
                    z2 = z
                if x != "-":
                    x2 = x
                z = (row_b[0]*row_a[3] - row_a[0]*row_b[3])/(row_b[0]*row_a[2] - row_a[0]*row_b[2])
                x = (row_a[3] - row_a[2]*z)/row_a[0]
                if (z2 != "-" and z2 != z) or (x2 != "-" and x2 != x):
                    nosol()
            elif row_a[2] == 0 and row_b[2] == 0:
                if x != "-":
                    x2 = x
                if y != "-":
                    y2 = y
                y = (row_b[0]*row_a[3] - row_a[0]*row_b[3])/(row_b[0]*row_a[1] - row_a[0]*row_b[1])
                x = (row_a[3] - row_a[1]*y)/row_a[0]
                if (x2 != "-" and x2 != x) or (y2 != "-" and y2 != y):
                    nosol()
            elif row_c != "":
                if row_a[0] == 0 and row_c[0] == 0:
                    if z != "-":
                        z2 = z
                    if y != "-":
                        y2 = y
                    z = (row_c[1]*row_a[3] - row_a[1]*row_c[3])/(row_c[1]*row_a[2] - row_a[1]*row_c[2])
                    y = (row_a[3] - row_a[2]*z)/row_a[1]
                    if (z2 != "-" and z2 != z) or (y2 != "-" and y2 != y):
                        nosol()
                elif row_a[1] == 0 and row_c[1] == 0:
                    if z != "-":
                        z2 = z
                    if x != "-":
                        x2 = x
                    z = (row_c[0]*row_a[3] - row_a[0]*row_c[3])/(row_c[0]*row_a[2] - row_a[0]*row_c[2])
                    x = (row_a[3] - row_a[2]*z)/row_a[0]
                    if (z2 != "-" and z2 != z) or (x2 != "-" and x2 != x):
                        nosol()
                elif row_a[2] == 0 and row_c[2] == 0:
                    if x != "-":
                        x2 = x
                    if y != "-":
                        y2 = y
                    y = (row_c[0]*row_a[3] - row_a[0]*row_c[3])/(row_c[0]*row_a[1] - row_a[0]*row_c[1])
                    x = (row_a[3] - row_a[1]*y)/row_a[0]
                    if (x2 != "-" and x2 != x) or (y2 != "-" and y2 != y):
                        nosol()
                elif row_b[0] == 0 and row_c[0] == 0:
                    if z != "-":
                        z2 = z
                    if y != "-":
                        y2 = y
                    z = (row_c[1]*row_b[3] - row_b[1]*row_c[3])/(row_c[1]*row_b[2] - row_b[1]*row_c[2])
                    y = (row_b[3] - row_b[2]*z)/row_b[1]
                    if (z2 != "-" and z2 != z) or (y2 != "-" and y2 != y):
                        nosol()
                elif row_b[1] == 0 and row_c[1] == 0:
                    if z != "-":
                        z2 = z
                    if x != "-":
                        x2 = x
                    z = (row_c[0]*row_b[3] - row_b[0]*row_c[3])/(row_c[0]*row_b[2] - row_b[0]*row_c[2])
                    x = (row_b[3] - row_b[2]*z)/row_b[0]
                    if (z2 != "-" and z2 != z) or (x2 != "-" and x2 != x):
                        nosol()
                elif row_b[2] == 0 and row_c[2] == 0:
                    if x != "-":
                        x2 = x
                    if y != "-":
                        y2 = y
                    y = (row_c[0]*row_b[3] - row_b[0]*row_c[3])/(row_c[0]*row_b[1] - row_b[0]*row_c[1])
                    x = (row_b[3] - row_b[1]*y)/row_b[0]
                    if (x2 != "-" and x2 != x) or (y2 != "-" and y2 != y):
                        nosol()

        for rw in rowss:
            if rw.count(0) == 0 or (rw.count(0) == 1 and rw[3] == 0):
                if x != "-" and y != "-" and z == "-":
                    z = (rw[3] - (rw[0]*x + rw[1]*y))/rw[2]
                elif x != "-" and y == "-" and z != "-":
                    y = (rw[3] - (rw[0]*x + rw[2]*z))/rw[1]
                elif x == "-" and y != "-" and z != "-":
                    x = (rw[3] - (rw[1]*y + rw[2]*z))/rw[0]
        if x != "-" and y != "-" and z != "-":
            if n == 2:
                x, y = y, x
            if n == 3:
                x, y, z = y, z, x
            x_sol.config(text="x = " + str(round(x, 8)))
            y_sol.config(text="y = " + str(round(y, 8)))
            z_sol.config(text="z = " + str(round(z, 8)))
            break
        else:
            standard_solve()
            if x != "-" and y != "-" and z != "-":
                if n == 2:
                    x, y = y, x
                if n == 3:
                    x, y, z = y, z, x
                x_sol.config(text="x = " + str(round(x, 8)))
                y_sol.config(text="y = " + str(round(y, 8)))
                z_sol.config(text="z = " + str(round(z, 8)))
                break
    return

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
    selectedentry.icursor("end")

def button_click(n):
    selectedentry.insert("insert", n)

def backspace():
    if len(selectedentry.get()) > 0:
        if selectedentry.get()[-1] == " ":
            selectedentry.delete(len(selectedentry.get())-3, "end")
        else:
            selectedentry.delete(len(selectedentry.get())-1, "end")

def clear():
    for en in entries:
        en.delete(0, "end")
    x_sol.config(text="")
    y_sol.config(text="")
    z_sol.config(text="")

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

acbutton = tk.Button(root, text="AC", fg="black", bg="#D2DEEE", padx=40, pady=30, command=clear).grid(row=7, column=9, columnspan=3, sticky="we")
minusbutton = tk.Button(root, text="-", fg="black", bg="#D2DEEE", padx=40, pady=30, command=lambda: button_click("-")).grid(row=6, column=9, columnspan=3, sticky="we")

goleftb = tk.Button(root, text="<--", fg="black", bg="#D2DEEE", padx=40, pady=30, command=goleft).grid(row=8, column=3, columnspan=3, sticky="we")
gorightb = tk.Button(root, text="-->", fg="black", bg="#D2DEEE", padx=40, pady=30, command=goright).grid(row=8, column=6, columnspan=3, sticky="we")

x_sol = tk.Label(root, text="");x_sol.grid(row=9, column=0, columnspan = 12, sticky="we")
y_sol = tk.Label(root, text="");y_sol.grid(row=10, column=0, columnspan = 12, sticky="we")
z_sol = tk.Label(root, text="");z_sol.grid(row=11, column=0, columnspan = 12, sticky="we")


root.mainloop()
