a, b = int(input("Zadejte hodnotu A\n")), int(input("Zadejte hodnotu B\n"))

if a != 0 or b !=0:
    if a > b:
        if (a%b) == 0:
            print(f"...\n{a//b}")