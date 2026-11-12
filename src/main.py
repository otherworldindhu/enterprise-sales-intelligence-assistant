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

