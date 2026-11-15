import pandas as pd


def load_business_data():
    sales_df = pd.read_csv("data/sales.csv")
    purchases_df = pd.read_csv("data/purchases.csv")

    return sales_df, purchases_df

def validate_business_data(sales_df, purchases_df):

    required_sales_columns = {
        "sale_id",
        "sale_date",
        "product",
        "region",
        "quantity",
        "unit_price"
    }

    required_purchase_columns = {
        "purchase_id",
        "purchase_date",
        "supplier",
        "product",
        "quantity",
        "unit_price"
    }

    missing_sales_columns = required_sales_columns - set(sales_df.columns)
    missing_purchase_columns = required_purchase_columns - set(purchases_df.columns)

    if missing_sales_columns:
        raise ValueError(
            f"Sales data is missing columns: {missing_sales_columns}"
        )

    if missing_purchase_columns:
        raise ValueError(
            f"Purchase data is missing columns: {missing_purchase_columns}"
        )