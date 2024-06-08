import pandas as pd

# Load the CSV file to understand its structure and content
file_path = './report/Realized_Capital_Gains.xlsx'
data = pd.read_excel(file_path)

# Verifying and replacing missing or NaN values in 'Acquired' with 0 in 'Cost basis (EUR)'
data['Cost basis (EUR)'] = data.apply(
    lambda row: 0 if pd.isna(row['Acquired']) else row['Cost basis (EUR)'], axis=1
)

# Display the first few rows of the dataframe and the column names to understand its structure
print(data.head(), data.columns)

# Grouping the data by 'Currency name' and summing 'Proceeds (EUR)' and 'Cost basis (EUR)'
grouped_data = data.groupby('Currency name').agg({
    'Proceeds (EUR)': 'sum',
    'Cost basis (EUR)': 'sum'
}).reset_index()

# Renaming the columns as specified
grouped_data.columns = ['Denominación de la moneda virtual', 'Valor de transmisión', 'Valor de adquisición']

# Saving the dataframe to a new Excel file
output_file_path = './report/Resumen_Criptomonedas.xlsx'
grouped_data.to_excel(output_file_path, index=False)
