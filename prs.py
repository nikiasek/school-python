import random

while True:
    pc_actions, pcAct = ["kámen", "nůžky", "papír"], random.choice(pc_actions)
    userAct = input("Zadej možnost (kámen, nůžky, papír):\n").lower()
    print(f"Hraješ {userAct} a počítač hraje {pcAct}.")

    if userAct == pcAct:
        print(f"Takže je to remíza")
    elif (userAct == "kámen" and pcAct == "nůžky") or (userAct == "nůžky" and pcAct == "papír") or (userAct == "papír" and pcAct == "kámen"):
        print("Takže je to výhra")
    else:
        print("Takže je to prohra")
