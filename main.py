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