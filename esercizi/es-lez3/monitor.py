import sys
import psutil

print("=== SYSTEM MONITOR ===")

print("Seleziona una statistica:\n")

opzioni = [
    "Versione Python",
    "Piattaforma sistema operativo",
    "Memoria RAM totale (bytes)",
    "Memoria RAM disponibile (bytes)",
    "Percentuale utilizzo RAM",
    "Percentuale utilizzo CPU (con 1s di attesa)",
    "Numero di CPU logiche",
    "Spazio disco totale (del filesystem root)",
    "Esci"
]

for i, opzione in enumerate(opzioni, 1):
    print(f"{i}. {opzione}")

print()

try:
    scelta = int(input("Inserisci la tua scelta: "))

    valore = None  # inizializzo

    if scelta == 1:
        valore = sys.version
    elif scelta == 2:
        valore = sys.platform
    elif scelta == 3:
        valore = psutil.virtual_memory().total
    elif scelta == 4:
        valore = psutil.virtual_memory().available
    elif scelta == 5:
        valore = psutil.virtual_memory().percent
    elif scelta == 6:
        print("\n--- Misurando l'utilizzo CPU... attendi un secondo ---")
        valore = psutil.cpu_percent(interval=1)
    elif scelta == 7:
        valore = psutil.cpu_count()
    elif scelta == 8:
        valore = psutil.disk_usage('/').total
    elif scelta == 9:
        print("Grazie per aver usato System Monitor! Arrivederci.")
        sys.exit()
    else:
        print("\nATTENZIONE: Opzione non valida. Scegli un numero presente nel menu (1-9).")
        sys.exit()

    print(f"\nValore: {valore}")

except ValueError:
    print("\nERRORE: Input non valido. Inserisci un NUMERO intero.")

except Exception as e:
    print(f"\nERRORE: Si è verificato un problema durante la raccolta dati: {e}")
