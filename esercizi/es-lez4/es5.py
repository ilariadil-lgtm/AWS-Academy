def valuta_temperatura(gradi):
	if gradi < 15:
		return "Freddo"
	elif gradi > 25:
		return "Caldo"
	else:
		return "Mite"


print(valuta_temperatura(26))
