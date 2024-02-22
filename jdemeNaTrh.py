v, c = int(input("Počet vajec:\n")), int(input("Počet cibulí:\n"))

if (v*3 + c*2) > (v*5 + c):
    print("JDI NA TRH")
elif (v*3 + c*2) < (v*5 + c):
    print("JDI DO HOSPODY")
else:
    print("JDI NA TRH")