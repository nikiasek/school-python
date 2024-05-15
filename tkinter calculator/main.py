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


b1 = tk.Button(w, text="1")
b1.grid(row=4, column=0)

b2 = tk.Button(w, text="2")
b2.grid(row=4, column=1)

b3 = tk.Button(w, text="3")
b3.grid(row=4, column=2)

b4 = tk.Button(w, text="4")
b4.grid(row=3, column=0)

b5 = tk.Button(w, text="5")
b5.grid(row=3, column=1)

b6 = tk.Button(w, text="6")
b6.grid(row=3, column=2)

b7 = tk.Button(w, text="7")
b7.grid(row=2, column=0)

b8 = tk.Button(w, text="8")
b8.grid(row=2, column=1)

b9 = tk.Button(w, text="9")
b9.grid(row=2, column=2)

b0 = tk.Button(w, text="0")
b0.grid(row=5, column=1)

bC = tk.Button(w, text="C")
bC.grid(row=6, column=0)

bNasobek = tk.Button(w, text="*")
bNasobek.grid(row=3, column=3)

bDeleni = tk.Button(w, text="/")
bDeleni.grid(row=4, column=3)

bMinus = tk.Button(w, text="-")
bMinus.grid(row=5, column=3)

bPlus = tk.Button(w, text="+")
bPlus.grid(row=6, column=3)

bCara = tk.Button(w, text=",")
bCara.grid(row=5, column=2)

bVycistit = tk.Button(w, text="C")
bVycistit.grid(row=6, column=0)

bUmazat = tk.Button(w, text="CE")
bUmazat.grid(row=2, column=3)


w.pack()
w.mainloop()