# pr1.py
import requests
import os

def descargar_molecula(molecula):
    url_pubchem = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{molecula}/SDF"
    url_wikipedia = f"https://en.wikipedia.org/wiki/{molecula}"

    # Descargar desde PubChem
    response = requests.get(url_pubchem)
    if response.status_code == 200:
        # Guardar el archivo solo si no existe
        file_path = f"data/{molecula}.sdf"
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(response.text)
            print(f"Archivo {molecula}.sdf descargado y guardado correctamente.")
        else:
            print(f"El archivo {molecula}.sdf ya existe en el disco.")

        # Mostrar información al usuario
        print(f"Nombre: {molecula}")
        print(f"URL PubChem: {url_pubchem}")
        print(f"URL Wikipedia: {url_wikipedia}")

    else:
        print(f"Error al descargar la molécula {molecula} desde PubChem.")

# Descargar para las 4 moléculas
moleculas = ["Adenine", "Guanine", "Cytosine", "Thymine"]
for molecula in moleculas:
    descargar_molecula(molecula)
