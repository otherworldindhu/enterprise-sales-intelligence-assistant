import matplotlib.pyplot as plt


def generate_sales_charts(product_sales_report, regional_report):
    plt.figure(figsize=(8, 5))

    plt.bar(
        product_sales_report["product"],
        product_sales_report["total_revenue"]
    )

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()

    plt.savefig("product_revenue.png", dpi=300)
    plt.show()
    plt.close()

    plt.figure(figsize=(8, 5))

    plt.bar(
        regional_report["region"],
        regional_report["total_revenue"]
    )

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()

    plt.savefig("regional_revenue.png", dpi=300)
    plt.show()
    plt.close()