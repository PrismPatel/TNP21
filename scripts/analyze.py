# scripts/analyze.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv(os.path.join("outputs", "tna2021_cleaned.csv"))

# Set output path
os.makedirs("outputs", exist_ok=True)

# Set style
sns.set(style="whitegrid")

# --- 1. Bar plot: Median household income by neighbourhood (Top 10) ---
top_income = df.sort_values("median_household_income", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x="median_household_income", y="neighbourhood_name", data=top_income, palette="Blues_d")
plt.title("Top 10 Neighbourhoods by Median Household Income (2021)")
plt.xlabel("Median Household Income")
plt.ylabel("Neighbourhood")
plt.tight_layout()
plt.savefig("outputs/top_income_neighbourhoods.png")
plt.close()

# --- 2. Histogram: Distribution of population ---
plt.figure(figsize=(10, 6))
sns.histplot(df["population_total"], bins=30, kde=True, color="skyblue")
plt.title("Population Distribution Across Toronto Neighbourhoods")
plt.xlabel("Total Population")
plt.ylabel("Number of Neighbourhoods")
plt.tight_layout()
plt.savefig("outputs/population_distribution.png")
plt.close()

# --- 3. Scatter: Income vs Unemployment Rate ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="median_household_income", y="unemployment_rate", color="skyblue", s=80)
plt.title("Income vs Unemployment Rate (Colored by Housing Suitability)")
plt.xlabel("Median Household Income")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("outputs/income_vs_unemployment.png")
plt.close()

# --- 4. Pie chart: Immigrant percentage range ---
bins = [0, 25, 50, 75, 100]
labels = ['0-25%', '26-50%', '51-75%', '76-100%']
df['immigrant_category'] = pd.cut(df['percent_immigrants'], bins=bins, labels=labels, include_lowest=True)
immigrant_dist = df['immigrant_category'].value_counts().sort_index()

plt.figure(figsize=(7, 7))
plt.pie(immigrant_dist, labels=immigrant_dist.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Distribution of Immigrant Population (%)")
plt.tight_layout()
plt.savefig("outputs/immigrant_distribution_pie.png")
plt.close()

print("✅ All visualizations saved in outputs/")
