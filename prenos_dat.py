x = int(input("kolik jste přenesl dat?\n"))

if x < 15:
    cena = x*2
else:
    cena = 30 + 3*(x-15)

print(f"Přenesl jsi {x}MB. Zaplatíš {cena} korun.")