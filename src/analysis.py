def calculate_total_revenue(df):
    total = (df["quantity"] * df["unit_price"]).sum()
    return total

def calculate_total_purchase_cost(df):
    total = (df["quantity"] * df["unit_price"]).sum()
    return total

def analyze_sales_by_product(df):
    product_summary = df.groupby("product").agg(
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum")
    ).reset_index()

    return product_summary

def analyze_purchases_by_supplier(df):
    supplier_summary = df.groupby("supplier").agg(
        total_quantity=("quantity", "sum"),
        total_purchase_cost=("purchase_cost", "sum")
    ).reset_index()

    return supplier_summary

def analyze_sales_by_region(df):
    region_summary = df.groupby("region").agg(
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum")
    ).reset_index()

    return region_summary
