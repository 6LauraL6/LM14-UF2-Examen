# pr3.py (Flask web service)
from flask import Flask, request, jsonify
from Bio import SeqIO, Entrez
import os

app = Flask(__name__)

def obtener_info_genbank(accession_code):
    # Directorio donde se encuentran los archivos GenBank
    genbank_dir = "./data"

    # Nombre del archivo GenBank basado en el código de acceso
    genbank_filename = f"{accession_code}_genbank.gb"

    # Ruta completa del archivo GenBank
    genbank_path = os.path.join(genbank_dir, genbank_filename)

    # Verificar si el archivo GenBank existe
    if os.path.exists(genbank_path):
        # Leer el archivo GenBank
        with open(genbank_path, "r") as genbank_file:
            record = SeqIO.read(genbank_file, "genbank")

            # Obtener información solicitada
            title = record.annotations.get('organism', 'N/A')
            accession_id = record.id
            organism = record.annotations.get('organism', 'N/A')
            ncbi_link = f"https://www.ncbi.nlm.nih.gov/nuccore/{accession_id}"
            references = record.annotations.get('references', [])
            latest_reference = references[-1]['title'] if references else 'N/A'
            num_features = len(record.features)

            cds_info = []
            for feature in record.features:
                if feature.type == "CDS":
                    cds_info.append({
                        'type': feature.type,
                        'location': feature.location,
                    })

            origin_sequence = str(record.seq)[:90]
            translation_sequence = record.seq.translate()[:30]

            # Devolver la información en formato diccionario
            info = {
                'Title': title,
                'Accession ID': accession_id,
                'Organism': organism,
                'NCBI Link': ncbi_link,
                'Latest Reference': latest_reference,
                'Number of Features': num_features,
                'CDS Information': cds_info,
                'Origin Sequence': origin_sequence,
                'Translation Sequence': str(translation_sequence),
            }
            return info

    else:
        # Archivo GenBank no encontrado
        return {'Error': 'El archivo GenBank no existe.'}

@app.route('/info_genbank', methods=['GET', 'POST'])
def info_genbank():
    accession_code = request.args.get('accession_code')

    # Lógica para obtener la información del genbank
    info = obtener_info_genbank(accession_code)

    # Devolver la información al cliente en formato JSON
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
