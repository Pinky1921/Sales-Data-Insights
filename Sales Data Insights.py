# -*- coding: utf-8 -*-
"""
Created on Sun May 25 12:33:27 2025

@author: Pinky
"""

import pandas as pd
import numpy as np

# Load dataset

df = pd.read_csv("datset - Sheet1.csv")

# View first few rows

print("Dataset Preview:\n", df.head())

# Clean missing/null values

df.dropna(inplace = True)

# Sum of sales by region
sales_by_region = df.groupby('Region')['TotalSales'].sum()
print("\nSum of Sales by Region:\n", sales_by_region)

# Average sales per product
avg_sales_product = df.groupby('Product')['TotalSales'].mean()
print("\nAverage Sales per Product:\n", avg_sales_product)

# Highest & lowest selling products
total_sales_product = df.groupby('Product')['TotalSales'].sum()
highest_selling = total_sales_product.idxmax()
lowest_selling = total_sales_product.idxmin()

print("\nHighest Selling Product:", highest_selling)
print("Lowest Selling Product:", lowest_selling)

# NumPy Calculations
sales_values = df['TotalSales'].values
mean_sales = np.mean(sales_values)
median_sales = np.median(sales_values)
std_sales = np.std(sales_values)

print("\nSales Statistics (using NumPy):")
print("Mean:", mean_sales)
print("Median:", median_sales)
print("Standard Deviation:", std_sales)
