import os
from Bio import SeqIO  # Asegúrate de que esta línea esté presente

def procesar_fasta(file_path):
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            header = record.id
            sequence = record.seq

            print(f"Header: {header}")
            print(f"Sequence: {sequence}")

# Lógica principal
fasta_file = "data/Inocybe rufuloides strain JLS 4076.fasta"  # Reemplaza con tu archivo .fasta
if os.path.exists(fasta_file):
    procesar_fasta(fasta_file)
else:
    print(f"El archivo {fasta_file} no existe.")