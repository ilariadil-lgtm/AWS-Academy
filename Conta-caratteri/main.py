"""
- dove si trova il testo?
    - il testo viene preso da un file
    - i file vengono mostrati a video dalla console 
- voglio contare i caratteri di un testo
    - voglio contare spazi e senza spzi
    - voglio contare anche le parole
    - voglio contare le frasi
    - voglio contare i paragrafi
    - voglio calcolare il tempo di lettura
    - voglio verificare le ripotezioni della parole e della lettera
"""
from typing import TextIO

def get_file(file_path: str) -> TextIO:
    """ Restituisce un oggetto TextIO con il contentuto del file specificato."""
    return open(file_path, "r")

def main() -> None:
    try:
        get_file("pippo.txt")
    except Exception as e:
        print(f"Errore generico: {e}")
    
    print("ciao sono qui")

main ()