kolac = int(input("Zadej počet: "))

if kolac < 10:
    print(f"upekl jsi {kolac} koláčů. Jsi začátečník")
elif kolac < 20:
    print(f"upekl jsi {kolac} koláčů. Jsi pokročilý")
else:
    print(f"upekl jsi {kolac} koláčů. Zasloužíš si mišelinskou hvěždu")