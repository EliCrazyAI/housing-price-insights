import pandas as pd
import numpy as np
import os

# current working directory
print("Working directory:", os.getcwd())

# ✅ Loaded dataset 
df = pd.read_csv("house-price-parquet.csv")

# 🛠️  first few rows to inspect structure
print("Sample data:\n", df.head())

# 📊 column names
print("\nAvailable columns:", df.columns)


if 'price' in df.columns:
    prices = df['price'].to_numpy()

    # 🔢 Basic stats using NumPy
    print("\nPrice stats:")
    print("Average price:", np.mean(prices))
    print("Max price:", np.max(prices))
    print("Min price:", np.min(prices))

    # 🔍 Filter homes priced above average
    above_avg = df[df['price'] > np.mean(prices)]
    print("\nHomes priced above average:\n", above_avg.head())
else:
    print("\n⚠️ Column 'price' not found. Please check the actual column name.")
