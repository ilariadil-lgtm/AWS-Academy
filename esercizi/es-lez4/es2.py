
def disegna_rettangolo(larghezza, altezza):
	for _  in range(altezza):
		riga = ""
		for _ in range(larghezza):
			riga  += "*"
		print(riga)

print("stampa rettangolo:")
disegna_rettangolo(5, 3)






