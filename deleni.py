a, b = int(input("Zadejte hodnotu A\n")), int(input("Zadejte hodnotu B\n"))

if (a !=0) and (b !=0):
    if a > b:
        if (a%b) == 0:
            print(f"...\n{a//b}")
        else:
            print("...\nNEJDE DĚLIT")
    else:
        if(b%a) == 0:
            print(f"...\n{b//a}")
        else:
            print("...\nNEJDE DĚLIT")
else:
    print("...\nNULOU NEMŮŽEME DĚLIT")