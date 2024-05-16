import tkinter as tk
import parse

# konstanty
backgroud_color = "#283747"

w = tk.Canvas(
    width=350,
    height=500,
    bg=backgroud_color,
    border=0
    )

vstupniPriklad = ""

priklad = tk.StringVar()

# FYZIKA

def getValue(x):
    global vstupniPriklad
    vstupniPriklad = vstupniPriklad + str(x)
    priklad.set(vstupniPriklad)

def getClear():
    global vstupniPriklad
    vstupniPriklad = ""
    priklad.set(vstupniPriklad)

def getClearEntry():
    global vstupniPriklad
    vstupniPriklad = vstupniPriklad[:-1]
    priklad.set(vstupniPriklad)
	
def soucet(vstup):
	arg1, arg2 = vstup.split("+")
	return(int(arg1) + int(arg2))

def podil(vstup):
	arg1, arg2 = vstup.split("/")
	return(int(arg1) / int(arg2))

def soucin(vstup):
	arg1, arg2 = vstup.split("*")
	return(int(arg1) * int(arg2))

def rozdil(vstup):
	arg1, arg2 = vstup.split("-")
	return(int(arg1) - int(arg2))

def umocneni(vstup):
	arg1, arg2 = vstup.split("**")
	return(int(arg1) ** int(arg2))

def getSolve():
    global vstupniPriklad
    match parse.search('{:D}', vstupniPriklad)[0]:
        case "+":
            priklad.set(soucet(vstupniPriklad))
        case "-":
            priklad.set(rozdil(vstupniPriklad))
        case "/":
            priklad.set(podil(vstupniPriklad))
        case "*":
            priklad.set(soucin(vstupniPriklad))
        case "**":
            priklad.set(umocneni(vstupniPriklad))
        case _:
            priklad.set("wrong input")


# TKINTER OKNO

w.columnconfigure(0, weight=1)
w.columnconfigure(1, weight=1)
w.columnconfigure(2, weight=1)
w.columnconfigure(3, weight=1)

vstupL = tk.Label(w, textvariable=priklad, height=2, width=27, background=backgroud_color, foreground="#ebedee")
vstupL.grid(row=0, column=0, columnspan=4)


b1 = tk.Button(w, text="1", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(1))
b1.grid(row=4, column=0)

b2 = tk.Button(w, text="2", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(2))
b2.grid(row=4, column=1)

b3 = tk.Button(w, text="3", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(3))
b3.grid(row=4, column=2)

b4 = tk.Button(w, text="4", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(4))
b4.grid(row=3, column=0)

b5 = tk.Button(w, text="5", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(5))
b5.grid(row=3, column=1)

b6 = tk.Button(w, text="6", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(6))
b6.grid(row=3, column=2)

b7 = tk.Button(w, text="7", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(7))
b7.grid(row=2, column=0)

b8 = tk.Button(w, text="8", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(8))
b8.grid(row=2, column=1)

b9 = tk.Button(w, text="9", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(9))
b9.grid(row=2, column=2)

b0 = tk.Button(w, text="0", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(0))
b0.grid(row=5, column=1)

bNasobek = tk.Button(w, text="*", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue("*"))
bNasobek.grid(row=3, column=3)

bDeleni = tk.Button(w, text="/", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue("/"))
bDeleni.grid(row=4, column=3)

bMinus = tk.Button(w, text="-", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue("-"))
bMinus.grid(row=5, column=3)

bPlus = tk.Button(w, text="+", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue("+"))
bPlus.grid(row=6, column=3)

bCara = tk.Button(w, text=",", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue(","))
bCara.grid(row=5, column=2)

bVycistit = tk.Button(w, text="C", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getClear())
bVycistit.grid(row=6, column=0)

bUmazat = tk.Button(w, text="CE", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getClearEntry())
bUmazat.grid(row=2, column=3)

bNaDruhou = tk.Button(w, text="**", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getValue("**"))
bNaDruhou.grid(row=6, column=2)

bRovnaSe = tk.Button(w, text="=", height=2, width=6, background="#3D4B59", borderwidth=0, foreground="#ebedee", command= lambda: getSolve())
bRovnaSe.grid(row=5, column=0)

# KONEC

w.pack()
w.mainloop()