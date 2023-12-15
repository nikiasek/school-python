pocet = int(input("kolik máš přestupků?\n"))                                            #Deklarace hodnoty pro počet přestupků

if pocet == 0:                                                                          #Podmínka říkající, že pokud je počet přestupků 0, tak hraje férově
    print(f"Dopustil ses {pocet} přestupků. Hraješ férově.")
elif pocet < 3:                                                                         #Podmínka říkající, že pokud je počet přestupků menší než 3, tak dostává žlutou kartu
    print(f"Dopustil ses {pocet} přestupků. Dostáváš žlutou kartu.")
else:                                                                                   #Podmínka říkající, že pokud je počet vetší nebo roven 3, tak dostává červenou a je vyloučen
    print(f"Dopustil ses {pocet} přestupků. Dostáváš červenou kartu a jsi vyloučen.")