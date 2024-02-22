vek = int(input("Zadejte věk\n"))

if vek < 6:
    print("Neplatíte nic")
elif vek < 18 or vek > 70:
    print("Platíte 50")
else:
    print("platíte 100")
