import tkinter as tk                                                    #Deklarace knihovny pro tvoření věcí s grafikou


a, b = int(input("zadej stranu A\n")), int(input("Zadej stranu B\n"))   #Deklarace proměnných A, B, které získáváme od uživatele
c = tk.Canvas( width=500, height=500)                                   #Deklarace plátna o velikosti 500x500

if a < b:                                                               #Podmínka která říká, že pokud je a menší než b tak vytvoření obdelníku na stojato
    c.create_rectangle(100, 200, 100+a, 200+b)
else:                                                                    #Podmínka která říká, že pokud je b menší než a tak vytvoření obdelníku na stojato
    c.create_rectangle(100, 200, 100+b, 200+a)

c.pack()
c.mainloop()