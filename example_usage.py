"""
example_usage.py -- Demonstrates BulkDiscountOptimizerClient
"""
from client import BulkDiscountOptimizerClient

def main():
    client = BulkDiscountOptimizerClient()
    result = client.optimize(unit_price=20.00, unit_cost=8.00, max_discount_pct=20)
    print("[Bulk Discount Optimization]")
    for t in result['tiers']:
        print(f"Qty: {t['min_quantity']}+ | Disc: {t['discount_percentage']}% | Price: ${t['price_per_unit']} | Margin: {t['margin_percentage']}%")

if __name__ == "__main__":
    main()
