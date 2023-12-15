x = int(input("kolik jste přenesl dat?\n"))             #Deklarace vstupní hodnoty kterou zadá uživatel

if x < 15:                                              #Podmínka která říká, že když je proměnná x menší než 15, tak vynásobí x dvojkou a dá to do proměnné cena
    cena = x*2
else:                                                   #Podmínka která říká, že když je proměnná x vetší než 15, tak přidá k ceně 30 a vynásobí x trojkou za každou hodinu navíc a dá to do hodnoty cena
    cena = 30 + 3*(x-15)

print(f"Přenesl jsi {x}MB. Zaplatíš {cena} korun.")     #Vypsání počtu přenesených dat a výsledné ceny