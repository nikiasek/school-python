import tkinter as tk


a, b = int(input("zadej stranu A\n")), int(input("Zadej stranu B\n"))
c = tk.Canvas( width=500, height=500)

if a < b:
    c.create_rectangle(100, 200, 100+a, 200+b)
else:
    c.create_rectangle(100, 200, 100+b, 200+a)

c.pack()
c.mainloop()