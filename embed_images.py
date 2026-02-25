import base64
import os
import re

html_path = r"C:\Users\aicil\.gemini\antigravity\scratch\presentation_sarampion_2025.html"
output_path = r"C:\Users\aicil\.gemini\antigravity\scratch\Campaña_Sarampion_2025_Final.html"
base_dir = r"C:\Users\aicil\.gemini\antigravity\scratch"

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

def embed_images(match):
    img_src = match.group(1)
    img_path = os.path.join(base_dir, img_src)
    
    if os.path.exists(img_path):
        ext = os.path.splitext(img_src)[1].lower().replace('.', '')
        if ext == 'jpg': ext = 'jpeg'
        
        with open(img_path, 'rb') as img_f:
            encoded_string = base64.b64encode(img_f.read()).decode('utf-8')
            return f'src="data:image/{ext};base64,{encoded_string}"'
    return match.group(0)

# Replace <img src="..."> with <img src="data:image/...">
new_content = re.sub(r'src="([^"]+\.png)"', embed_images, html_content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Self-contained HTML created at: {output_path}")
