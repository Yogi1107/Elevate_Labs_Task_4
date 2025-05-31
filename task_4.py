import pandas as pd

# Load your original dataset
df = pd.read_csv("sales_data_sample.csv", encoding='ISO-8859-1')

# Clean the data
df = df.drop_duplicates()
df['COUNTRY'] = df['COUNTRY'].str.strip().str.title()

# Convert ORDERDATE and drop rows with invalid dates
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df = df.dropna(subset=['ORDERDATE'])

# Clean column headers
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Fix data types
df['year_id'] = pd.to_numeric(df['year_id'], errors='coerce', downcast='integer')
df['quantityordered'] = pd.to_numeric(df['quantityordered'], errors='coerce', downcast='integer')
df['priceeach'] = pd.to_numeric(df['priceeach'], errors='coerce')
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# Save to new CSV
df.to_csv("cleaned_sales_data.csv", index=False)
