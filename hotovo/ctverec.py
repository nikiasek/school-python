import tkinter as tk                                                        #Deklarace knihovny pro grafiku
import random as r                                                          #Deklarace knihovny pro náhodné hodnoty

c = tk.Canvas()                                                             #Deklarace hodnoty pro plátno

first, second = ["white","cyan"], ["red", "yellow"]                         #Deklarace 2 hodnot, které jsou listy
y = 100                                                                     #Deklarace souřadnice y

for i in range(1, 13):                                                      #For loop pro tvoření čtverců které od sebe budou posunuté
    x = 10*i                                                                #Deklarace souřadnice x
    if i < 6:                                                               #Podmínka, která říká, že pokud je i menší než 6, tak vytvoří čtverec ->
        c.create_rectangle(x-5, y-5, x+5, y+5, fill=r.choice(first))        #čtverec, který má buď bílou nebo šedou barvu.
    else:                                                                   #Podmínk, která říká, že pokud je i vetší než 6, tak vytvoří čtverec ->
         c.create_rectangle(x-5, y-5, x+5, y+5, fill=r.choice(second))      #čtverec, který má buď červenou nebo žlutou barvu.

c.pack()                                                                    #Zabalení plátna
c.mainloop()