import pandas as pd
import re

# Localities identified from the text extraction
localities = [
    "VICTORIA DE DURANGO", "VICTORIA DE DURANGO", "VICTORIA DE DURANGO", 
    "LA GUAJOLOTA", "LA GUAJOLOTA", "LA GUAJOLOTA", 
    "COLONIA HIDALGO", "GÓMEZ PALACIO", "LA GUAJOLOTA", "LA GUAJOLOTA",
    "COLONIA HIDALGO", "VICTORIA DE DURANGO", "VICENTE GUERRERO", 
    "COLONIA HIDALGO", "VICTORIA DE DURANGO", "VICTORIA DE DURANGO",
    "VICTORIA DE DURANGO", "VICTORIA DE DURANGO", "VICTORIA DE DURANGO",
    "VICTORIA DE DURANGO", "VICTORIA DE DURANGO", "VICTORIA DE DURANGO",
    "VICTORIA DE DURANGO", "CIHUACORA", "VICTORIA DE DURANGO", "LAS JOYAS",
    "VICTORIA DE DURANGO", "LA JOYA", "LA JOYA", "LAS JOYAS",
    "LA GUAJOLOTA", "LA GUAJOLOTA", "VICTORIA DE DURANGO", "LAS JOYAS",
    "VICTORIA DE DURANGO", "VICTORIA DE DURANGO", "VICTORIA DE DURANGO",
    "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS",
    "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS",
    "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS", "LAS JOYAS"
]

# Note: COLINIA HIDALGO was corrected to COLONIA HIDALGO
# LAS JOYAS vs LA JOYA: We'll keep them as extracted but they might be the same.

df = pd.DataFrame(localities, columns=["Localidad"])
counts = df["Localidad"].value_counts().reset_index()
counts.columns = ["Localidad", "Casos"]

def get_priority(casos):
    if casos >= 10:
        return "Muy Alta (Rojo)"
    if casos >= 5:
        return "Alta (Naranja)"
    if casos >= 2:
        return "Media (Amarillo)"
    return "Baja (Verde)"

counts["Prioridad"] = counts["Casos"].apply(get_priority)

# Sort by cases descending
counts = counts.sort_values(by="Casos", ascending=False)

# Export to Markdown table
markdown_table = counts.to_markdown(index=False)
print(markdown_table)

# Save to CSV for reference
counts.to_csv("prioritization_summary.csv", index=False)
