import pandas as pd
def calculate_total_revenue(df):
    total = (df["quantity"] * df["unit_price"]).sum()
    return total
# Read sales data
sales_df = pd.read_csv("data/sales.csv")

# Read purchase data
purchases_df = pd.read_csv("data/purchases.csv")

# Display sales data
print("SALES DATA")
print(sales_df)

# Display purchase data
print("\nPURCHASE DATA")
print(purchases_df)

# Display basic information
print("\nSALES INFORMATION")
print(sales_df.info())

print("\nPURCHASE INFORMATION")
print(purchases_df.info())

print("\nFIRST FIVE SALES")
print(sales_df.head())

print("\nTOTAL SALES RECORDS")
print(len(sales_df))

print("\nCOLUMN NAMES")
print(sales_df.columns)

print("\nSALES DATA TYPES")
print(sales_df.dtypes)

# Inspect the sales dataset

print("First 5 rows:")
print(sales_df.head())

print("\nDataset shape:")
print(sales_df.shape)

print("\nColumn names:")
print(sales_df.columns)

print("\nDataset information:")
sales_df.info()

print("\nMissing values:")
print(sales_df.isnull().sum())

print("\nDuplicate rows:")
print(sales_df.duplicated().sum())

# Inspect purchase dataset

print("\nPURCHASE DATASET SHAPE")
print(purchases_df.shape)

print("\nPURCHASE MISSING VALUES")
print(purchases_df.isnull().sum())

print("\nPURCHASE DUPLICATE ROWS")
print(purchases_df.duplicated().sum())

print("\nPURCHASE DATA TYPES")
print(purchases_df.dtypes)

# Check duplicate transaction IDs
print("\nDUPLICATE SALES IDs")
print(sales_df["sale_id"].duplicated().sum())

print("\nDUPLICATE PURCHASE IDs")
print(purchases_df["purchase_id"].duplicated().sum())

# Convert date columns to datetime

sales_df["sale_date"] = pd.to_datetime(
    sales_df["sale_date"],
    format="%d-%m-%Y"
)

purchases_df["purchase_date"] = pd.to_datetime(
    purchases_df["purchase_date"],
    format="%d-%m-%Y"
)

# Verify converted data types

print("\nUPDATED SALES DATA TYPES")
print(sales_df.dtypes)

print("\nUPDATED PURCHASE DATA TYPES")
print(purchases_df.dtypes)

# Calculate revenue for each sales transaction

sales_df["revenue"] = (
    sales_df["quantity"] * sales_df["unit_price"]
)

print("\nSALES DATA WITH REVENUE")
print(sales_df)

# Calculate total sales revenue
total_revenue = sales_df["revenue"].sum()

print("\nTOTAL SALES REVENUE")
print(total_revenue)

# Calculate revenue by product
product_revenue = sales_df.groupby("product")["revenue"].sum()

print("\nREVENUE BY PRODUCT")
print(product_revenue)

# Calculate revenue by region
region_revenue = sales_df.groupby("region")["revenue"].sum()

print("\nREVENUE BY REGION")
print(region_revenue)

# Revenue by product
sales_df.groupby("product")["revenue"].sum()

# Revenue by region
sales_df.groupby("region")["revenue"].sum()

# Calculate revenue by product and region
product_region_revenue = (
    sales_df.groupby(["product", "region"])["revenue"].sum()
)

print("\nREVENUE BY PRODUCT AND REGION")
print(product_region_revenue)

# Convert grouped result into a regular DataFrame
product_region_report = (
    sales_df.groupby(["product", "region"])["revenue"]
    .sum()
    .reset_index()
)

print("\nPRODUCT AND REGION REVENUE REPORT")
print(product_region_report)

# Sort product-region revenue from highest to lowest
sorted_product_region = product_region_report.sort_values(
    by="revenue",
    ascending=False
)

print("\nPRODUCT-REGION REVENUE RANKING")
print(sorted_product_region)

# Filter sales transactions with revenue greater than 50000
high_revenue_sales = sales_df[
    sales_df["revenue"] > 50000
]

print("\nHIGH REVENUE SALES")
print(high_revenue_sales)

# Filter high-revenue sales in Asia
asia_high_revenue = sales_df[
    (sales_df["revenue"] > 50000) &
    (sales_df["region"] == "Asia")
]

print("\nHIGH REVENUE SALES IN ASIA")
print(asia_high_revenue)

# Filter sales from Asia or Europe
asia_europe_sales = sales_df[
    (sales_df["region"] == "Asia") |
    (sales_df["region"] == "Europe")
]

print("\nSALES FROM ASIA OR EUROPE")
print(asia_europe_sales)

# Filter sales excluding Africa
non_africa_sales = sales_df[
    ~(sales_df["region"] == "Africa")
]

print("\nSALES EXCLUDING AFRICA")
print(non_africa_sales)

# Filter sales from selected regions using isin()
selected_regions = ["Asia", "Europe"]

selected_region_sales = sales_df[
    sales_df["region"].isin(selected_regions)
]

print("\nSALES FROM SELECTED REGIONS")
print(selected_region_sales)

# Filter sales within a revenue range
medium_revenue_sales = sales_df[
    sales_df["revenue"].between(40000, 60000)
]

print("\nSALES WITH REVENUE BETWEEN 40000 AND 60000")
print(medium_revenue_sales)

# Select specific columns for the sales report
sales_summary = sales_df[
    ["product", "region", "revenue"]
]

print("\nSALES SUMMARY REPORT")
print(sales_summary)

purchases_df["purchase_cost"] = (
    purchases_df["quantity"] * purchases_df["unit_price"]
)

print("\nPURCHASE COST")
print(purchases_df[["supplier", "product", "purchase_cost"]])

supplier_purchase_cost = (
    purchases_df.groupby("supplier")["purchase_cost"].sum()
)

print("\nTOTAL PURCHASE COST BY SUPPLIER")
print(supplier_purchase_cost)

product_purchase_cost = (
    purchases_df.groupby("product")["purchase_cost"].sum()
)

print("\nTOTAL PURCHASE COST BY PRODUCT")
print(product_purchase_cost)

product_financial_summary = pd.concat(
    [product_revenue, product_purchase_cost],
    axis=1
)

print("\nPRODUCT FINANCIAL SUMMARY")
print(product_financial_summary)

product_financial_summary["gross_profit"] = (
    product_financial_summary["revenue"]
    - product_financial_summary["purchase_cost"]
)

print("\nPRODUCT PROFIT SUMMARY")
print(product_financial_summary)

sorted_profit_summary = product_financial_summary.sort_values(
    by="gross_profit",
    ascending=False
)

print("\nPRODUCTS RANKED BY GROSS PROFIT")
print(sorted_profit_summary)

total_revenue = calculate_total_revenue(sales_df)

total_purchase_cost = purchases_df["purchase_cost"].sum()

total_gross_profit = total_revenue - total_purchase_cost

print("\nCOMPANY FINANCIAL SUMMARY")
print("Total Revenue:", total_revenue)
print("Total Purchase Cost:", total_purchase_cost)
print("Total Gross Profit:", total_gross_profit)

loss_making_products = product_financial_summary[
    product_financial_summary["gross_profit"] < 0
]

print("\nLOSS-MAKING PRODUCTS")
print(loss_making_products)

product_financial_summary["gross_profit_margin"] = (
    product_financial_summary["gross_profit"]
    / product_financial_summary["revenue"]
) * 100

print("\nPRODUCT PROFIT MARGIN")
print(product_financial_summary)

product_financial_summary["gross_profit_margin"] = (
    product_financial_summary["gross_profit_margin"].round(2)
)

print("\nPRODUCT PROFIT MARGIN")
print(product_financial_summary)

total_gross_profit_margin = (
    total_gross_profit / total_revenue
) * 100

total_gross_profit_margin = round(
    total_gross_profit_margin, 2
)

print("\nCOMPANY GROSS PROFIT MARGIN")
print("Overall Margin:", total_gross_profit_margin, "%")

product_overview = pd.merge(
    sales_df,
    purchases_df,
    on="product",
    how="inner"
)

print("\nPRODUCT OVERVIEW")
print(product_overview.head())

print("Total merged rows:", len(product_overview))
print("DataFrame shape:", product_overview.shape)

product_sales_summary = product_revenue.reset_index(
    name="revenue"
)

product_purchase_summary = product_purchase_cost.reset_index(
    name="purchase_cost"
)

product_summary = pd.merge(
    product_sales_summary,
    product_purchase_summary,
    on="product",
    how="inner",
    validate="one_to_one"
)

print("\nPRODUCT-LEVEL SUMMARY")
print(product_summary)

print("Shape:", product_summary.shape)

product_reconciliation = pd.merge(
    product_sales_summary,
    product_purchase_summary,
    on="product",
    how="outer",
    indicator=True,
    validate="one_to_one"
)

print("\nPRODUCT RECONCILIATION")
print(product_reconciliation)

print("\nRECONCILIATION STATUS")
print(product_reconciliation["_merge"].value_counts())

