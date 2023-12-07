import tkinter as tk
import random as r

c = tk.Canvas()
c.pack()

[x, y, time] = [r.randint(10, 304), r.randint(10, 304), r.randint(1, 16)]

noc = ["navy", "white"]
den = ["blue", "yellow"]

if time < 8:
    c.create_rectangle(0, 0, 380, 180, fill=noc[0])
    c.create_oval(x-50, y-50, x+50, y+50, fill=noc[1])
    c.create_rectangle(0, 180, 480, 280, fill="green")
else:
    c.create_rectangle(0, 0, 380, 180, fill=den[0])
    c.create_oval(x-50, y-50, x+50, y+50, fill=den[1])
    c.create_rectangle(0, 180, 480, 280, fill="green")

c.mainloop()