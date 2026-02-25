import pandas as pd
import os

def create_excel():
    data = {
        'Concepto': [
            'Población 2026 (Durango)', 
            'Población Meta (Durango)', 
            'Dosis Aplicadas (Durango)', 
            'Población Susceptible (Durango)'
        ],
        'Valor': [1922647, 47754, 28647, 19107],
        'Metodología de Cálculo': [
            '', 
            '', 
            '', 
            'Población Meta - Dosis Aplicadas = Población Susceptible'
        ]
    }
    
    df = pd.DataFrame(data)
    
    output_path = r'C:\Users\aicil\OneDrive\Escritorio\PVU\SARAMPIÓN\CAMPAÑA SARAMPIÓN 10 SEMANAS\Poblacion_Susceptible_Durango_2026.xlsx'
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create Excel with nice formatting
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Resultados Durango')
        
        workbook = writer.book
        worksheet = writer.sheets['Resultados Durango']
        
        # Add some basic formatting
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#D7E4BC',
            'border': 1
        })
        
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(col_num, col_num, 30)
            
    print(f"Archivo creado exitosamente en: {output_path}")

if __name__ == "__main__":
    create_excel()
