## 1. Definire una domanda ("qual è il tuo linguaggio di programmazione preferito?")
# Definire le quattro opzioni di risposta (es: 1. Python, 2.JavaScript, 3. Java, 4. C++)

domanda =  "Qual è il linguaggio di programmazione preferito?"
risposta = [ "Python", "JavaScript", "Java", "C++" ]
	
print("QUIZ PYTHON")
print(f"{domanda}\n")

#opzioni numerate
for i, opzione in enumerate (risposta, 1):
	print(f" {i}. {opzione}")

print()

# Chiedere di inserire un numero da 1 a 4
try:
	domanda = input("scegli un numero da 1 a 4:")
	scelta = int(domanda)

## inserire le opzioni di risposta

	if domanda == "1":
		print(f"Ottima scelta perchè lo useremo per i prossimi 4 mesi")

	elif domanda == "2":
		print(f"Interessante! Ma mi vuoi male! (Scherzo, è ottimo per il web.")

	elif domanda == "3":
		print(f"Solida scelta! Ok, però si potrebbe fare meglio! Tipo Python!")

	elif domanda == "4":
		print(f"Potente! C++ è ottimo per le performance, ma lasciamolo agli specialisti!")


## ERRORI ##
	
	else:
		domanda = "SCELTA NON VALIDA"
		messaggio = "Errore: devi scegliere un numero tra 1 e 4!"

		if scelta >= 1 and scelta <= 4:
			print({domanda})
			print(messaggio)

##Errore non numerico
except ValueError:
	print("Errore: devi inserire un numero, non un testo o un carattere non numerico!")
