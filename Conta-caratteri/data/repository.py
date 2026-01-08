# ===============================
#   Repository
# =============================== 

import requests

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Il file '{file_path}' non esiste") from e
    except OSError as e:
        raise IOError(f"Errore leggendo il file '{file_path}': {e}") from e


def get_data_from_server(url: str) -> str:
    if not url or not isinstance(url, str):
        raise ValueError("L'URL deve essere una stringa non vuota")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise ConnectionError(f"Problema con la chiamata a {url}: {e}") from e