import base64
import os
import re
import json

base_dir = r"C:\Users\aicil\.gemini\antigravity\scratch"
html_path = os.path.join(base_dir, "presentation_sarampion_2025.html")
semaforo_path = os.path.join(base_dir, "charts", "semaforo.json")
analysis_path = os.path.join(base_dir, "charts", "analysis_v4.json")
output_path = os.path.join(base_dir, "Campaña_Sarampion_2025_Final.html")

# Read files
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

with open(semaforo_path, 'r', encoding='utf-8') as f:
    semaforo_data = json.load(f)

with open(analysis_path, 'r', encoding='utf-8') as f:
    analysis_data = json.load(f)

# Inject Data
html_content = html_content.replace('SEMAFORO_DATA_PLACEHOLDER', json.dumps(semaforo_data))
html_content = html_content.replace('ANALYSIS_DATA_PLACEHOLDER', json.dumps(analysis_data))

# Embed Images
def embed_images(match):
    img_src = match.group(1)
    # Check in scratch and scratch/charts
    img_path = os.path.join(base_dir, img_src)
    if not os.path.exists(img_path):
        img_path = os.path.join(base_dir, "charts", img_src)
    
    if os.path.exists(img_path):
        ext = os.path.splitext(img_src)[1].lower().replace('.', '')
        if ext == 'jpg': ext = 'jpeg'
        
        with open(img_path, 'rb') as img_f:
            encoded_string = base64.b64encode(img_f.read()).decode('utf-8')
            return f'src="data:image/{ext};base64,{encoded_string}"'
    return match.group(0)

# Replace <img src="...">
new_content = re.sub(r'src="([^"]+\.png)"', embed_images, html_content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Self-contained HTML with Semáforo created at: {output_path}")
