import tkinter as tk
import random as r


c = tk.Canvas(
    width=400,
    height=400
)
c.pack()
for i in range(5):
    a, b, s = r.randint(30, 300), r.randint(30,300), r.randint(1,10)
    c.create_rectangle(a, b, a+50, b+50, fill="white")
    c.create_text(a+25, b+25, text=s)