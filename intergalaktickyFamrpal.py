a, b = int(input("Kolik bodů má tým A\n")), int(input("Kolik bodů má tým B\n"))

if a >= 50:
    print("vítězí tým A")
elif b >= 50:
    print("vítězé tým B")
elif a < b:
    print("vítězé tým A")
elif a > b:
    print("vítězí tým B")
elif a == b:
    print("vítězí oba")
