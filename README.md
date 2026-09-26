# Supply Chain Data Analytics

## Overview

This project performs data analysis on supply chain data using Python and Pandas.

The project analyzes sales, inventory levels, demand forecasts, warehouses, products, and stockout records to identify useful patterns in the supply chain data.

## Objectives

- Analyze total sales and inventory levels
- Identify top-performing products
- Analyze inventory levels across warehouses
- Compare actual sales with demand forecasts
- Analyze daily sales trends
- Examine stockout records
- Visualize important supply chain patterns

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Dataset

## Project Structure

```text
Supply-Chain-Data-Analytics/
│
├── datasets/
│   └── Supply_chain_dataset1.csv
│
├── outputs/
│   ├── actual_vs_demand_forecast.png
│   ├── daily_sales_trend.png
│   ├── inventory_by_warehouse.png
│   ├── stockout_analysis.png
│   └── top_10_products.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
main.py
Python
supply_chain_dataset1(1).csv
Spreadsheet
cleaned_supply_chain.csv
Spreadsheet

Yes. Since your project is basically complete, let's make the GitHub version clean and proper without unnecessarily adding complexity.

I recommend these 4 files/folders:

Supply-Chain-Data-Analytics/
│
├── datasets/
│   └── Supply_chain_dataset1.csv
│
├── outputs/
│   ├── actual_vs_demand_forecast.png
│   ├── daily_sales_trend.png
│   ├── inventory_by_warehouse.png
│   ├── stockout_analysis.png
│   └── top_10_products.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Don't upload cleaned_supply_chain.csv unless you specifically need it. Your main code already reads the original dataset.

1. main.py

You can replace your current main.py with this version. It keeps your existing summary analysis and also generates the five graphs you already made.

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("datasets/Supply_chain_dataset1.csv")

df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# Create output folder
os.makedirs("outputs", exist_ok=True)


# -------------------------------
# Basic Summary
# -------------------------------

print("SUPPLY CHAIN DATA ANALYTICS SUMMARY")
print("-----------------------------------")

print("Total Records:", len(df))
print("Total Units Sold:", df["Units_Sold"].sum())
print("Average Inventory Level:", df["Inventory_Level"].mean())
print("Total Stockout Records:", df["Stockout_Flag"].sum())


# -------------------------------
# Top 5 Products by Sales
# -------------------------------

top_5_products = (
    df.groupby("SKU_ID")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products by Sales:")
print(top_5_products)


# -------------------------------
# Average Inventory by Warehouse
# -------------------------------

inventory_by_warehouse = (
    df.groupby("Warehouse_ID")["Inventory_Level"]
    .mean()
)

print("\nAverage Inventory by Warehouse:")
print(inventory_by_warehouse)


# -------------------------------
# 1. Actual Sales vs Demand Forecast
# -------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Units_Sold"],
    df["Demand_Forecast"],
    alpha=0.5
)

plt.title("Actual Sales vs Demand Forecast")
plt.xlabel("Actual Units Sold")
plt.ylabel("Demand Forecast")

plt.tight_layout()
plt.savefig("outputs/actual_vs_demand_forecast.png")
plt.close()


# -------------------------------
# 2. Daily Sales Trend
# -------------------------------

daily_sales = (
    df.groupby("Date")["Units_Sold"]
    .sum()
)

plt.figure(figsize=(10, 5))

plt.plot(
    daily_sales.index,
    daily_sales.values
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Units Sold")

plt.tight_layout()
plt.savefig("outputs/daily_sales_trend.png")
plt.close()


# -------------------------------
# 3. Average Inventory by Warehouse
# -------------------------------

plt.figure(figsize=(8, 5))

inventory_by_warehouse.plot(
    kind="bar"
)

plt.title("Average Inventory by Warehouse")
plt.xlabel("Warehouse ID")
plt.ylabel("Average Inventory Level")

plt.tight_layout()
plt.savefig("outputs/inventory_by_warehouse.png")
plt.close()


# -------------------------------
# 4. Stockout Analysis
# -------------------------------

stockout_counts = (
    df["Stockout_Flag"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(7, 5))

stockout_counts.plot(
    kind="bar"
)

plt.title("Stockout Analysis")
plt.xlabel("Stockout Flag")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.savefig("outputs/stockout_analysis.png")
plt.close()


# -------------------------------
# 5. Top 10 Products by Sales
# -------------------------------

top_10_products = (
    df.groupby("SKU_ID")["Units_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(9, 5))

top_10_products.plot(
    kind="bar"
)

plt.title("Top 10 Products by Sales")
plt.xlabel("SKU ID")
plt.ylabel("Total Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/top_10_products.png")
plt.close()


print("\nAnalysis completed successfully.")
print("Graphs have been saved in the outputs folder.")

Your original summary section is preserved here.

2. requirements.txt

Create a file named:

requirements.txt

Paste:

pandas
matplotlib

That's enough for this project.

3. .gitignore

Create a file named:

.gitignore

Paste:

__pycache__/
*.pyc
.venv/
venv/
.env
.idea/
.vscode/

This prevents unnecessary Python/IDE files from going onto GitHub.

4. README.md

Create:

README.md

Paste this:

# Supply Chain Data Analytics

## Overview

This project performs data analysis on supply chain data using Python and Pandas.

The project analyzes sales, inventory levels, demand forecasts, warehouses, products, and stockout records to identify useful patterns in the supply chain data.

## Objectives

- Analyze total sales and inventory levels
- Identify top-performing products
- Analyze inventory levels across warehouses
- Compare actual sales with demand forecasts
- Analyze daily sales trends
- Examine stockout records
- Visualize important supply chain patterns

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Dataset

## Project Structure

```text
Supply-Chain-Data-Analytics/
│
├── datasets/
│   └── Supply_chain_dataset1.csv
│
├── outputs/
│   ├── actual_vs_demand_forecast.png
│   ├── daily_sales_trend.png
│   ├── inventory_by_warehouse.png
│   ├── stockout_analysis.png
│   └── top_10_products.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
Analysis Performed
1. Actual Sales vs Demand Forecast

A scatter plot is used to compare actual units sold with the demand forecast.

2. Daily Sales Trend

The daily total units sold are plotted to observe changes in sales over time.

3. Average Inventory by Warehouse

Average inventory levels are calculated and compared across warehouses.

4. Stockout Analysis

The stockout flag is analyzed to identify the number of records associated with stockout conditions.

5. Top 10 Products by Sales

Products are ranked according to their total units sold to identify the highest-selling SKUs.

Key Observations
Actual sales and demand forecast show a clear positive relationship.
Daily sales vary considerably over the analyzed period.
Average inventory levels differ across warehouses.
The dataset contains no recorded stockout cases, with the Stockout Flag remaining 0 in the provided data.
The top products have relatively similar total sales values.
Dataset

The dataset used in this project was obtained from Kaggle.

The dataset is used for educational and academic analysis.

How to Run
Clone or download this repository.
Install the required libraries:
pip install -r requirements.txt
Make sure the dataset is located at:
datasets/Supply_chain_dataset1.csv
Run the Python program:
python main.py
The analysis results will be displayed in the terminal and the graphs will be saved in the outputs folder.
Author

Priyanka Umesh Thakre

B.Tech - Robotics & Artificial Intelligence


---

# 5. What you should actually upload

Your final folder should look **exactly roughly like this**:

```text
📁 Supply-Chain-Data-Analytics

   📁 datasets
      └── Supply_chain_dataset1.csv

   📁 outputs
      ├── actual_vs_demand_forecast.png
      ├── daily_sales_trend.png
      ├── inventory_by_warehouse.png
      ├── stockout_analysis.png
      └── top_10_products.png

   📄 main.py
   📄 requirements.txt
   📄 README.md
   📄 .gitignore
Don't upload these

❌ cleaned_supply_chain.csv
❌ __pycache__
❌ .idea
❌ .venv
❌ random screenshots
❌ unnecessary duplicate Python files

One thing before uploading the Kaggle dataset

Because the CSV came from Kaggle, check its Kaggle license/terms before publicly redistributing the actual CSV on GitHub. If redistribution isn't permitted, we'll leave the CSV out and put the Kaggle source in the README instead.

For now, create these 4 files using the content above. Once you've done that, send me a screenshot of your project folder, and I'll check the structure before you upload it to GitHub.

how much content needs to paste in readme

You don't need to paste the whole long README. For your college project, keep it short and clean.

I recommend about 30–50 lines. This is enough:

# Supply Chain Data Analytics

## Overview

This project performs data analysis on supply chain data using Python, Pandas, and Matplotlib.

The project analyzes sales, inventory levels, demand forecasts, warehouses, products, and stockout records.

## Objectives

- Analyze total sales and inventory levels
- Identify top-performing products
- Analyze inventory across warehouses
- Compare actual sales with demand forecasts
- Analyze daily sales trends
- Examine stockout records

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Dataset

## Project Structure

```text
Supply-Chain-Data-Analytics/
├── datasets/
│   └── Supply_chain_dataset1.csv
├── outputs/
│   ├── actual_vs_demand_forecast.png
│   ├── daily_sales_trend.png
│   ├── inventory_by_warehouse.png
│   ├── stockout_analysis.png
│   └── top_10_products.png
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

 ##Analysis Performed
Actual Sales vs Demand Forecast

Compares actual units sold with the demand forecast.

Daily Sales Trend

Shows changes in total daily sales over time.

Average Inventory by Warehouse

Compares average inventory levels across warehouses.

Stockout Analysis

Analyzes stockout records in the dataset.

Top 10 Products by Sales

Identifies the products with the highest total units sold.

## Dataset

The dataset used in this project is the "High-Dimensional Supply Chain Inventory Dataset" obtained from Kaggle.

Source: Kaggle – ziya07/high-dimensional-supply-chain-inventory-dataset

License: CC0-1.0