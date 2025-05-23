import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('data/neighbourhood_profiles_2021.csv')  # You already converted it

# Check the shape (rows, columns)
print("🧾 Shape of the dataset:", df.shape)

# Get all column names — very useful to understand structure
print("\n📋 Columns:\n", df.columns.tolist())

# See what types of data each column holds
print("\n🔍 Data types:\n", df.dtypes)

# Peek at the top few rows
print("\n👀 First 5 rows:\n", df.head())

# See how many missing values each column has
print("\n❌ Missing values:\n", df.isnull().sum())

# Get stats: mean, min, max, etc. for numeric columns
print("\n📊 Summary Stats:\n", df.describe(include='all'))
