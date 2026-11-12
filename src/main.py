import pandas as pd

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