import urllib.request
import ssl
import json
import pandas as pd
import unicodedata

def normalize_str(s):
    if not s:
        return ""
    return ''.join(c for c in unicodedata.normalize('NFD', str(s))
                  if unicodedata.category(c) != 'Mn').lower()

def extract_durango_data():
    context = ssl._create_unverified_context()
    url = 'https://dondemevacuno.salud.gob.mx/centros_vacunacion.json'
    
    print(f"Downloading data from {url}...")
    try:
        with urllib.request.urlopen(url, context=context) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        print(f"Total records downloaded: {len(data)}")
        
        durango_records = []
        for item in data:
            entidad = item.get('entidad', '')
            norm_entidad = normalize_str(entidad)
            
            if 'durango' in norm_entidad:
                # Flatten biologics list if it's a list
                biologicos = item.get('biologicos', [])
                if isinstance(biologicos, list):
                    biologicos_str = ", ".join(biologicos)
                else:
                    biologicos_str = str(biologicos)
                
                record = {
                    'Sede': item.get('sede', ''),
                    'Direccion': item.get('direccion', ''),
                    'Municipio': item.get('municipio', ''),
                    'Entidad': entidad,
                    'Horario': item.get('horario', ''),
                    'Dias': item.get('dias', ''),
                    'Biologicos': biologicos_str,
                    'Latitud': item.get('lat', ''),
                    'Longitud': item.get('lng', ''),
                    'Institucion': item.get('institucion', ''),
                    'Tipo': item.get('tipo', '')
                }
                durango_records.append(record)
        
        print(f"Records found for Durango: {len(durango_records)}")
        
        if durango_records:
            df = pd.DataFrame(durango_records)
            output_file = 'vaccination_centers_durango.xlsx'
            df.to_excel(output_file, index=False)
            print(f"Data successfully saved to {output_file}")
            return output_file
        else:
            print("No records found for Durango.")
            return None
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    extract_durango_data()
