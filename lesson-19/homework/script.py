import pandas as pd
import sqlite3

# ------------------ 1
sales_data = pd.read_csv("sales_data.csv")

category_stats = sales_data.groupby("Category").agg(
    Total_Quantity=("Quantity", "sum"),
    Max_Quantity=("Quantity", "max"),
    Avg_Price=("Price", "mean")
).reset_index()

print("\n1 — Category Statistics:")
print(category_stats)

# ------------------ 2
grouped = sales_data.groupby(["Category", "Product"], as_index=False)["Quantity"].sum()
top_products = grouped.loc[grouped.groupby("Category")["Quantity"].idxmax()]

print("\n2 — Top-selling product in each category:")
print(top_products)

# ------------------ 3
sales_data["Total_sales"] = sales_data["Quantity"] * sales_data["Price"]
daily_sales = sales_data.groupby("Date")["Total_sales"].sum().reset_index()
top_sales_day = daily_sales.loc[daily_sales["Total_sales"].idxmax()]

print("\n3 — Date with highest total sales:")
print(top_sales_day)

# ------------------ 4
customer_orders = pd.read_csv("customer_orders.csv")
grouped_cus = customer_orders.groupby("CustomerID")["OrderID"].count().reset_index()
active_customers = grouped_cus[grouped_cus["OrderID"] >= 20]

print("\n4 — Customers with >= 20 orders:")
print(active_customers)

# ------------------ 5
customer_orders["avg_per_unit"] = customer_orders["Price"] / customer_orders["Quantity"]
high_value_customers = (
    customer_orders.groupby("CustomerID")["avg_per_unit"].mean().reset_index()
)
high_value_customers = high_value_customers[high_value_customers["avg_per_unit"] > 120]

print("\n5 — Customers with avg unit price > $120:")
print(high_value_customers)

# ------------------ 6
product_summary = customer_orders.groupby('Product').agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("Price", "sum")
).reset_index()

product_summary = product_summary[product_summary["Total_Quantity"] >= 5]

print("\n6 — Products with total quantity >= 5:")
print(product_summary)

# ------------------ Population DB Query ------------------
with sqlite3.connect("population.db") as conn:
    query = "SELECT * FROM population"
    pop_df = pd.read_sql_query(query, conn)

print("\nPopulation Data from DB:")
print(pop_df)
