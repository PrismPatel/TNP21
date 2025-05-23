# scripts/clean_data.py

import pandas as pd
import os

# File paths
input_path = os.path.join("data", "neighbourhood_profiles_2021.csv")
output_path = os.path.join("outputs", "tna2021_cleaned.csv")

# Load raw data
df_raw = pd.read_csv(input_path)

# Step 1: Set "Neighbourhood Name" as index
df_raw.set_index("Neighbourhood Name", inplace=True)

# Step 2: Transpose so each row is a neighbourhood
df_t = df_raw.T.reset_index()
df_t = df_t.rename(columns={"index": "neighbourhood_name"})

# Step 3: Extract only needed variables (change if necessary)
columns_map = {
    "Total population": "population_total",
    "Median total income in 2020 ($)": "median_household_income",
    "Unemployment rate": "unemployment_rate",
    "Immigrants": "percent_immigrants",
    "Suitable housing": "housing_suitability"
}

# Step 4: Try to find closest matching keys
extracted_cols = {}
for row_label in df_raw.index:
    for keyword in columns_map:
        if keyword.lower() in row_label.lower():
            extracted_cols[columns_map[keyword]] = row_label
            break

# Debug print to see what's matched
print("✔️ Matched variables:")
for k, v in extracted_cols.items():
    print(f"{k} ← {v}")

# Step 5: Extract and rename selected columns
df_clean = df_t[["neighbourhood_name"] + list(extracted_cols.values())]
df_clean = df_clean.rename(columns={v: k for k, v in extracted_cols.items()})

# Step 6: Clean numeric columns
for col in df_clean.columns:
    if col != "neighbourhood_name":
        df_clean[col] = df_clean[col].astype(str).str.replace(",", "").str.replace("%", "").str.strip()
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

# Step 7: Fill missing values
df_clean.fillna(df_clean.median(numeric_only=True), inplace=True)

# Step 8: Save
os.makedirs("outputs", exist_ok=True)
df_clean.to_csv(output_path, index=False)

print(f"✅ Cleaned data saved to: {output_path}")
