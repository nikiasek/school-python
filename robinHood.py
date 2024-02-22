money = int(input("Zadejte množství peněz:\n"))

if money < 100:
    money *= 2
    print("DAR")
else:
    money -= 50
    print("LUP")