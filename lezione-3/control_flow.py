# control flow

a: int = 2
b: int = a

print(type(( a == b)))

"""
#pippo vuole guidare l'auto, ma può farlo?
#se pippo ha la patente, può guidare
#se pippo non ha la patente, non può guidare

domanda: str = input("Ha la patente?")

if domanda.lower() == "si":
	print("può guidare")
elif domanda.lower() == "no":
	print("non può guidare")

else:
	print("inserisci solo si o no")
"""

piove: bool = False
if not piove:
	print("è vero, non piove")


# Quanti anni ha pippo?

domanda = input("quanti anni ha pippo?")

if domanda.isdigit():
	result = "può guidare" if int(domanda) >= 18 else "Non può guidare"
	print(result)
else:
	print("inserisci un valore numerico")
