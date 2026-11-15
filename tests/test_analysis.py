import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analysis import calculate_total_revenue


def test_calculate_total_revenue():

    sales_df = pd.DataFrame({
        "quantity": [10, 20],
        "unit_price": [100, 200]
    })

    result = calculate_total_revenue(sales_df)

    assert result == 5000