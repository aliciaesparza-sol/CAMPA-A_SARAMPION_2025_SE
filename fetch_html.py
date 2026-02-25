import urllib.request
import ssl

context = ssl._create_unverified_context()

try:
    with urllib.request.urlopen('https://dondemevacuno.salud.gob.mx/', context=context) as response:
        content = response.read().decode('utf-8')
        with open('page_source.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully saved to page_source.html")
except Exception as e:
    print(f"Error: {e}")
