import urllib.request
import ssl
import json

context = ssl._create_unverified_context()
url = 'https://dondemevacuno.salud.gob.mx/centros_vacunacion.json'

try:
    with urllib.request.urlopen(url, context=context) as response:
        data = json.loads(response.read().decode('utf-8'))
        print(f"Successfully downloaded {len(data)} records.")
        # Print first record to see structure
        if data:
            print("First record sample:", data[0])
            
        # Check for Durango
        durango_count = sum(1 for item in data if 'durango' in str(item.get('entidad', '')).lower())
        print(f"Found {durango_count} records for Durango.")
        
except Exception as e:
    print(f"Error: {e}")
