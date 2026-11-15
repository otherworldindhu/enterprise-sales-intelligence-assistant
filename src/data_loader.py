import pandas as pd


def load_business_data():
    sales_df = pd.read_csv("data/sales.csv")
    purchases_df = pd.read_csv("data/purchases.csv")

    return sales_df, purchases_df