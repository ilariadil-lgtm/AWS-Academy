def calcola_sconto(prezzo, età):
	if età > 18:
		return prezzo * 0.8
	elif età >= 64:	
		return prezzo * 0.7
	else:
		return prezzo

print(calcola_sconto(65, 18))
