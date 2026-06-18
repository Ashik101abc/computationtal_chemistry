import pandas as pd

# Load the raw CSV file
df = pd.read_csv('her_data.csv')

print("--- RAW DATA ---")
print(df)
print("\n----------------\n")

# Clean the data by dropping any row that has missing values (NaN)
cleaned_df = df.dropna()

print("--- CLEANED DATA ---")
print(cleaned_df)
