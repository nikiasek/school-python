import tkinter as tk

# konstanty
backgroud_color = "#283747"



# TKINTER OKNO

w = tk.Canvas(
    width=350,
    height=500,
    bg=backgroud_color
    )

w.columnconfigure(0, weight=1)
w.columnconfigure(1, weight=1)
w.columnconfigure(2, weight=1)
w.columnconfigure(3, weight=1)

vstupL = tk.Label(w, text="random", height=2, width=26)
vstupL.grid(row=0, column=0, columnspan=4)

vystupL = tk.Label(w, text="random", height=2, width=26)
vystupL.grid(row=1, column=0, columnspan=4)

b1 = tk.Button(w, text="1", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b1.grid(row=4, column=0)

b2 = tk.Button(w, text="2", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b2.grid(row=4, column=1)

b3 = tk.Button(w, text="3", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b3.grid(row=4, column=2)

b4 = tk.Button(w, text="4", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b4.grid(row=3, column=0)

b5 = tk.Button(w, text="5", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b5.grid(row=3, column=1)

b6 = tk.Button(w, text="6", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b6.grid(row=3, column=2)

b7 = tk.Button(w, text="7", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b7.grid(row=2, column=0)

b8 = tk.Button(w, text="8", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b8.grid(row=2, column=1)

b9 = tk.Button(w, text="9", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b9.grid(row=2, column=2)

b0 = tk.Button(w, text="0", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
b0.grid(row=5, column=1)

bC = tk.Button(w, text="C", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bC.grid(row=6, column=0)

bNasobek = tk.Button(w, text="*", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bNasobek.grid(row=3, column=3)

bDeleni = tk.Button(w, text="/", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bDeleni.grid(row=4, column=3)

bMinus = tk.Button(w, text="-", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bMinus.grid(row=5, column=3)

bPlus = tk.Button(w, text="+", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bPlus.grid(row=6, column=3)

bCara = tk.Button(w, text=",", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bCara.grid(row=5, column=2)

bVycistit = tk.Button(w, text="C", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bVycistit.grid(row=6, column=0)

bUmazat = tk.Button(w, text="CE", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bUmazat.grid(row=2, column=3)

bNaDruhou = tk.Button(w, text="**", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee")
bNaDruhou.grid(row=6, column=2)

# FYZIKA



# KONEC

w.pack()
w.mainloop()