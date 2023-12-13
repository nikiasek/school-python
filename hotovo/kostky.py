import random as r

for i in range(5):
    a, b = r.randint(1,6), r.randint(1,6)
    print(f"{i+1}. hod:\nNa první kostce padlo {a}, na druhé {b}.\nSoučet těchto čísel je {a+b}.")