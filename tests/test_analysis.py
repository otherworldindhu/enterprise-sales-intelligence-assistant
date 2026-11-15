import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analysis import calculate_total_revenue
from analysis import (
    calculate_total_revenue,
    analyze_sales_by_product
)
import pytest

from data_loader import validate_business_data
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

def test_validate_business_data_rejects_missing_sales_column():

    sales_df = pd.DataFrame({
        "sale_id": [101],
        "sale_date": ["2026-10-01"],
        "product": ["Cocoa"],
        "region": ["Asia"],
        "quantity": [100]
    })

    purchases_df = pd.DataFrame({
        "purchase_id": [201],
        "purchase_date": ["2026-10-01"],
        "supplier": ["Supplier A"],
        "product": ["Cocoa"],
        "quantity": [200],
        "unit_price": [400]
    })

    with pytest.raises(ValueError, match="Sales data is missing columns"):
        validate_business_data(sales_df, purchases_df)

def test_calculate_total_revenue_with_empty_dataframe():

    sales_df = pd.DataFrame({
        "quantity": [],
        "unit_price": []
    })

    result = calculate_total_revenue(sales_df)

    assert result == 0