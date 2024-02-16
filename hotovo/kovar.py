x, k = int(input("kolik máme podkov?\n")), int(input("kolik máme koní?"))*4
pocet = x - k

if pocet > 0:
    print(f"přebývá {pocet} podkov")
elif pocet < 0:
    print(f"Chybí ti {-pocet} podkov")
else:
    print("máš přesně podkov na koně")