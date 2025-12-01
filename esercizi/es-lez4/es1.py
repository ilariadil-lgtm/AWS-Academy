
"""
def separatore():
	## istruzione1  true se numero pari
	## istruzione2  false se numero dispari
	print("="*50)

##print("la funzione è stata definita, ma non eseguita")

print("\nchiamiamo la funzione:")
separatore()

print("\nChiamiamola altre due volte:")
separatore()
separatore()
"""

def stampa_tabellina(numero):
    for i in range(1, 11):
        risultato = numero * i
        print(f"{numero} x {i} = {risultato}")

print("Stampo la tabellina del 2:")
stampa_tabellina(2)
stampa_tabellina(3) 



