from pathlib import Path

def generate_sales_report(
        total_revenue,
        total_purchase_cost,
        total_gross_profit,
        product_sales_report,
        regional_report,
        supplier_report
):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    highest_revenue_product = product_sales_report.loc[
    product_sales_report["total_revenue"].idxmax()]

    highest_revenue_region = regional_report.loc[
    regional_report["total_revenue"].idxmax()
]

    html_report = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Sales Intelligence Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f6f8;
        }}

        h1 {{
            color: #1f2937;
        }}

        h2 {{
            color: #2563eb;
            margin-top: 30px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background-color: white;
        }}

        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: left;
        }}

        th {{
            background-color: #1f2937;
            color: white;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>

<body>
    <h1>Enterprise Sales Intelligence Report</h1>

    <h2>Business Overview</h2>

    <p><strong>Total Revenue:</strong> {total_revenue:,.0f}</p>
    <p><strong>Total Purchase Cost:</strong> {total_purchase_cost:,.0f}</p>
    <p><strong>Simplified Gross Profit Estimate:</strong> {total_gross_profit:,.0f}</p>
    <p><strong>Top Product:</strong> {highest_revenue_product["product"]}</p>
    <p><strong>Top Region:</strong> {highest_revenue_region["region"]}</p>

        <h2>Revenue Visualisations</h2>

    <h3>Revenue by Product</h3>
    <img src="../product_revenue.png"
         alt="Revenue by Product"
         width="600">

    <h3>Revenue by Region</h3>
    <img src="../regional_revenue.png"
         alt="Revenue by Region"
         width="600">

    <h2>Product Sales Performance</h2>
    {product_sales_report.to_html(index=False)}

    <h2>Regional Sales Performance</h2>
    {regional_report.to_html(index=False)}

    <h2>Supplier Performance</h2>
    {supplier_report.to_html(index=False)}
</body>
</html>
"""

    report_path = reports_dir / "sales_intelligence_report.html"
    report_path.write_text(html_report, encoding="utf-8")

    print("\nBusiness report generated:", report_path)
