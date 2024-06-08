import pandas as pd

# Ruta al archivo CSV
file_path = './report/Realized_Capital_Gains.csv'

# Cargar los datos desde CSV
data = pd.read_csv(file_path)

# Ruta del archivo de salida Excel
output_excel_path = './report/Realized_Capital_Gains.xlsx'

# Guardar los datos en formato Excel
data.to_excel(output_excel_path, index=False)

print("El archivo Excel ha sido creado con éxito en:", output_excel_path)
