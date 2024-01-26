# pr4.py
from Bio import Entrez
import os
import time

def descargar_genbank_fasta(accession_code, organism):
    # Configuración de Entrez
    Entrez.email = "tu_correo@dominio.com"

    # Realizar la búsqueda con eUtils
    term = f'{organism}[Organism] AND {accession_code}[Accession]'
    handle = Entrez.esearch(db="nucleotide", term=term, retmax=30)
    record_ids = Entrez.read(handle)['IdList']

    # Descargar los archivos genbank y fasta
    for record_id in record_ids:
        handle_genbank = Entrez.efetch(db="nucleotide", id=record_id, rettype="gb", retmode="text")
        handle_fasta = Entrez.efetch(db="nucleotide", id=record_id, rettype="fasta", retmode="text")

        # Guardar los archivos en el disco
        with open(f"data/{record_id}_genbank.gb", "w") as file_genbank:
            file_genbank.write(handle_genbank.read())
        with open(f"data/{record_id}_fasta.fasta", "w") as file_fasta:
            file_fasta.write(handle_fasta.read())

        time.sleep(1)  # Evitar restricciones de Entrez (1 solicitud por segundo)

# Lógica principal
accession_code = "KM288867"
organism = "Plasmodium falciparum"
descargar_genbank_fasta(accession_code, organism)
