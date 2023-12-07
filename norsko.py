import tkinter as tk

c = tk.Canvas()
c.pack()

c.create_rectangle(0, 0, 250, 160, fill="red")
c.create_rectangle(60, 0, 100, 160, fill="white")
c.create_rectangle(0, 60, 250, 100, fill="white")
c.create_rectangle(70, 0, 90, 160, fill="navy")
c.create_rectangle(0, 70, 250, 90, fill="navy")
c.mainloop()