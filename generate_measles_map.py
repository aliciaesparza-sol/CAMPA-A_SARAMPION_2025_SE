import pandas as pd
import folium
from folium.plugins import MarkerCluster
import os

def generate_map():
    # Load case coordinates
    cases_df = pd.read_csv('case_coordinates.csv')
    
    # Load vaccination centers (from previous task)
    vaccination_centers_file = 'vaccination_centers_durango.xlsx'
    vax_df = None
    if os.path.exists(vaccination_centers_file):
        try:
            vax_df = pd.read_excel(vaccination_centers_file)
        except Exception as e:
            print(f"Warning: Could not read vaccination centers: {e}")

    # Center map on Durango
    m = folium.Map(location=[24.0277, -104.6532], zoom_start=7, tiles='CartoDB positron')
    
    # Add Cases (Traffic Light Logic)
    for _, row in cases_df.iterrows():
        # Traffic Light Color Logic:
        # Red (High): 3+ cases
        # Orange (Medium): 2 cases
        # Yellow (Low): 1 case
        if row['casos'] >= 3:
            color = 'red'
            icon_name = 'exclamation-triangle'
        elif row['casos'] == 2:
            color = 'orange'
            icon_name = 'exclamation-circle'
        else:
            color = 'yellow'
            icon_name = 'info-circle'
        
        popup_text = f"<b>Colonia/Localidad:</b> {row['colonia']}<br>"
        popup_text += f"<b>Municipio:</b> {row['municipio']}<br>"
        popup_text += f"<b>Código Postal:</b> {row['cp']}<br>"
        popup_text += f"<b>Casos:</b> {row['casos']}"
        
        folium.Marker(
            location=[row['lat'], row['lng']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=f"{row['colonia']} ({row['casos']} casos)",
            icon=folium.Icon(color=color, icon=icon_name, prefix='fa')
        ).add_to(m)
        
        # Add a radius circle for red zones (High Priority)
        if color == 'red':
            folium.Circle(
                location=[row['lat'], row['lng']],
                radius=1500, # 1.5km radius for high priority
                color='red',
                fill=True,
                fill_opacity=0.25
            ).add_to(m)
        elif color == 'orange':
            folium.Circle(
                location=[row['lat'], row['lng']],
                radius=800, # 0.8km radius for medium priority
                color='orange',
                fill=True,
                fill_opacity=0.15
            ).add_to(m)

    # Add Vaccination Centers as reference (Green)
    if vax_df is not None:
        vax_cluster = MarkerCluster(name="Centros de Vacunación").add_to(m)
        for _, row in vax_df.iterrows():
            if pd.notna(row['Latitud']) and pd.notna(row['Longitud']):
                vax_popup = f"<b>Sede:</b> {row['Sede']}<br>"
                vax_popup += f"<b>Dirección:</b> {row['Direccion']}<br>"
                vax_popup += f"<b>Municipio:</b> {row['Municipio']}"
                
                folium.Marker(
                    location=[row['Latitud'], row['Longitud']],
                    popup=vax_popup,
                    tooltip=row['Sede'],
                    icon=folium.Icon(color='green', icon='medkit', prefix='fa')
                ).add_to(vax_cluster)

    # Add Legend
    legend_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 230px; height: 160px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color: white; opacity: 0.9; padding: 10px; border-radius: 5px;">
     <b>Semáforo de Prioridad</b><br>
     &nbsp; <i class="fa fa-map-marker" style="color:red"></i> &nbsp; Prioridad Alta (3+ casos)<br>
     &nbsp; <i class="fa fa-map-marker" style="color:orange"></i> &nbsp; Prioridad Media (2 casos)<br>
     &nbsp; <i class="fa fa-map-marker" style="color:yellow"></i> &nbsp; Prioridad Baja (1 caso)<br>
     &nbsp; <i class="fa fa-map-marker" style="color:green"></i> &nbsp; Punto de Vacunación<br>
     </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))

    output_file = 'measles_map_durango.html'
    m.save(output_file)
    print(f"Map created: {output_file}")
    return output_file

if __name__ == "__main__":
    generate_map()
