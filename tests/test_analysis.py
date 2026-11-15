import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analysis import calculate_total_revenue
from analysis import (
    calculate_total_revenue,
    analyze_sales_by_product
)

def test_calculate_total_revenue():

    sales_df = pd.DataFrame({
        "quantity": [10, 20],
        "unit_price": [100, 200]
    })

    result = calculate_total_revenue(sales_df)

    assert result == 5000

def test_analyze_sales_by_product():

    sales_df = pd.DataFrame({
        "product": ["Cocoa", "Coffee", "Cocoa"],
        "quantity": [10, 20, 30],
        "revenue": [5000, 12000, 15000]
    })

    result = analyze_sales_by_product(sales_df)

    cocoa = result[result["product"] == "Cocoa"].iloc[0]

    assert cocoa["total_quantity"] == 40
    assert cocoa["total_revenue"] == 20000