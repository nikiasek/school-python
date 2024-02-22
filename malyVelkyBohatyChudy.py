tonik = {
    "vyska": int(input("vyska\n")),
    "počet pěnez": int(input("počet peněz\n")),
}

if tonik["vyska"] < 150:
    tonik["vyska"] == "MALÝ"
else:
    tonik["vyska"] == "VELKÝ"

if tonik["počet pěnez"] < 1000:
    tonik["počet pěnez"] == "CHUDÝ"
else:
    tonik["počet pěnez"] == "BOHATÝ"

print(f"TONÍK JE {tonik['vyska']} A {tonik['počet pěnez']}")