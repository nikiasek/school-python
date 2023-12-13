# kreslení korálků
import tkinter as tk    # Import knihovny grafiky
import random as r      # Import náhodných znaků

c = tk.Canvas()         # vytvoření plátna
c.pack()                # zabalení plátna

y, x = 0, 100                   # počáteční hodnota "y"
for i in range(12):      # for loop pro tvoření všeho
    x = 20 + x
    y = 20+y
    if i < 3:
        c.create_oval(x-10, y-10, x+10, y+10, fill=r.choice(["red","aquamarine"]))
    elif i < 6:
        c.create_oval(x-10, y-10, x+10, y+10, fill=r.choice(["yellow","aquamarine"]))
    elif i < 7:
        c.create_oval(x-10, y-10, x+10, y+10, fill=r.choice(["yellow","red"]))
    else:
        c.create_oval(x-10, y-10, x+10, y+10, fill=r.choice(["yellow","red","aquamarine"]))
c.mainloop()

text=r.choice(["yellow","red","aquamarine"])
print(text)