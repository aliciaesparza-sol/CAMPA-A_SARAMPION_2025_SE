import pandas as pd
import re

# Full data based on extraction of 61 cases
data = [
    # Page 0
    {"ID": 1, "Edad": 47, "Localidad": "VICTORIA DE DURANGO", "Centro": "IMSS HGZ 1"},
    {"ID": 2, "Edad": 7, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA 1"},
    {"ID": 3, "Edad": 41, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA 1"},
    {"ID": 4, "Edad": 1, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 5, "Edad": 1, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 6, "Edad": 17, "Localidad": "LA GUAJOLOTA", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    {"ID": 7, "Edad": 8, "Localidad": "COLONIA HIDALGO", "Centro": "SSD CESSA 1"},
    {"ID": 8, "Edad": 1, "Localidad": "GÓMEZ PALACIO", "Centro": "IMSS H. GENERAL 46"},
    # Page 1
    {"ID": 9, "Edad": 11, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 10, "Edad": 8, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 11, "Edad": 8, "Localidad": "COLONIA HIDALGO", "Centro": "SSD CESSA N° 1"},
    {"ID": 12, "Edad": 21, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD HOSP. GRAL. 450"},
    {"ID": 13, "Edad": 26, "Localidad": "VICENTE GUERRERO", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    {"ID": 14, "Edad": 8, "Localidad": "COLONIA HIDALGO", "Centro": "SSD CESSA N° 1"},
    {"ID": 15, "Edad": 39, "Localidad": "VICTORIA DE DURANGO", "Centro": "IMSS HOSPITAL GENERAL DE ZONA N° 1"},
    {"ID": 16, "Edad": 7, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 17, "Edad": 30, "Localidad": "VICTORIA DE DURANGO", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    # Page 2
    {"ID": 18, "Edad": 14, "Localidad": "VICTORIA DE DURANGO", "Centro": "IMSS HOSPITAL GENERAL DE ZONA N° 1"},
    {"ID": 19, "Edad": 10, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 20, "Edad": 19, "Localidad": "VICTORIA DE DURANGO", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    {"ID": 21, "Edad": 2, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA N° 1"},
    {"ID": 22, "Edad": 17, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA N° 1"},
    {"ID": 23, "Edad": 40, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA N° 1"},
    {"ID": 24, "Edad": 1, "Localidad": "CIHUACORA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 25, "Edad": 3, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 26, "Edad": 4, "Localidad": "LAS JOYAS", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    # Page 3
    {"ID": 27, "Edad": 4, "Localidad": "VICTORIA DE DURANGO", "Centro": "IMSS HOSPITAL GENERAL DE ZONA N° 1"},
    {"ID": 28, "Edad": 8, "Localidad": "LA JOYA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 29, "Edad": 14, "Localidad": "LA JOYA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 30, "Edad": 20, "Localidad": "LAS JOYAS", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 31, "Edad": 4, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 32, "Edad": 33, "Localidad": "LA GUAJOLOTA", "Centro": "SSD H. MATERNO INF. LA GUAJOLOTA"},
    {"ID": 33, "Edad": 6, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 34, "Edad": 15, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 35, "Edad": 10, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 36, "Edad": 10, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 37, "Edad": 11, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    # Page 4
    {"ID": 38, "Edad": 7, "Localidad": "LAS JOYAS", "Centro": "SSD HOSP. INTEGRAL LA GUAJOLOTA"},
    {"ID": 39, "Edad": 21, "Localidad": "LAS JOYAS", "Centro": "SSD HOSP. INTEGRAL LAGUAJOLOTA"},
    {"ID": 40, "Edad": 33, "Localidad": "LAS JOYAS", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 41, "Edad": 22, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 42, "Edad": 16, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 43, "Edad": 20, "Localidad": "LAS JOYAS", "Centro": "SSD H. MATERNO INF. MEZQUITAL"},
    {"ID": 44, "Edad": 11, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 45, "Edad": 17, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 46, "Edad": 6, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 47, "Edad": 19, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 48, "Edad": 2, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    # Page 5
    {"ID": 49, "Edad": 1, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 50, "Edad": 5, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 51, "Edad": 10, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 52, "Edad": 9, "Localidad": "LAS JOYAS", "Centro": "IMSS OP. GUADALUPE VICTORIA MEZQUITAL"},
    {"ID": 53, "Edad": 7, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 54, "Edad": 13, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 55, "Edad": 32, "Localidad": "VICTORIA DE DURANGO", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    {"ID": 56, "Edad": 34, "Localidad": "VICTORIA DE DURANGO", "Centro": "ISSSTE H. SANTIAGO RAMÓN Y CAJAL"},
    {"ID": 57, "Edad": 11, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA N° 1 DR. CARLOS LEÓN"},
    {"ID": 58, "Edad": 10, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD CESSA N° 1 DR. CARLOS LEÓN"},
    # Page 6
    {"ID": 59, "Edad": 8, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."},
    {"ID": 60, "Edad": 32, "Localidad": "COLONIA HIDALGO", "Centro": "SSD CESSA N° 1 DR. CARLOS LEÓN"},
    {"ID": 61, "Edad": 0.83, "Localidad": "VICTORIA DE DURANGO", "Centro": "SSD H. MATERNO INF."} # 10mss = 0.83 years
]

df = pd.DataFrame(data)

# Analysis: Locality
locality_counts = df["Localidad"].value_counts().reset_index()
locality_counts.columns = ["Localidad", "Casos"]

# Analysis: Age Group
bins = [-1, 4, 9, 14, 19, 39, 100]
labels = ["0-4 años", "5-9 años", "10-14 años", "15-19 años", "20-39 años", "40+ años"]
df["Grupo de Edad"] = pd.cut(df["Edad"], bins=bins, labels=labels)
age_counts = df["Grupo de Edad"].value_counts().reset_index().sort_values("Grupo de Edad")
age_counts.columns = ["Grupo de Edad", "Casos"]

# Analysis: Notification Center
center_counts = df["Centro"].value_counts().reset_index()
center_counts.columns = ["Centro de Notificación", "Casos"]

# Save results
locality_counts.to_csv("update_localidad_1602.csv", index=False)
age_counts.to_csv("update_edad_1602.csv", index=False)
center_counts.to_csv("update_centro_1602.csv", index=False)

print("Analysis by Locality:")
print(locality_counts.to_markdown(index=False))
print("\nAnalysis by Age Group:")
print(age_counts.to_markdown(index=False))
print("\nAnalysis by Center:")
print(center_counts.to_markdown(index=False))
