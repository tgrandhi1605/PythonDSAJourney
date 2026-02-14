class Troubleshooting:
    def __init__(self):
        pass


    def calculate_total_revenue(self, transactions):
        total = 0.0
        seen_ids = set()

        for tx in transactions:
            tx_id = tx.get('id')

            # Bug 1: Efficiency & Uniqueness
            if not tx_id or tx_id in seen_ids:
                continue

            # Bug 2: Handling explicit None values
            raw_price = tx.get('price')
            if raw_price is not None:
                try:
                    total += float(raw_price)
                    seen_ids.add(tx_id)  # Don't forget to add to set!
                except ValueError:
                    print(f"Skipping invalid price format for ID {tx_id}")

        return round(total, 2)

if __name__ == "__main__":
    test_transactions = [
        # 1. Standard Happy Path
        {'id': 'tx_001', 'price': '10.50', 'type': 'subscription'},
        {'id': 'tx_002', 'price': 15.00, 'type': 'purchase'},  # Note: This is an int, not a string

        # 2. Duplicate Transaction ID (Should be skipped)
        {'id': 'tx_001', 'price': '10.50', 'type': 'subscription'},

        # 3. Explicit None Value (The "Trap" we discussed)
        {'id': 'tx_003', 'price': None, 'type': 'trial'},

        # 4. Missing Key entirely (Should return 0 from .get())
        {'id': 'tx_004', 'type': 'gift_card'},

        # 5. Invalid String format (The "Dirty Data")
        {'id': 'tx_005', 'price': 'free', 'type': 'promo'},

        # 6. Negative Value (Business logic edge case)
        {'id': 'tx_006', 'price': '-5.00', 'type': 'refund'}
    ]

    calculate = Troubleshooting()
    revenue = calculate.calculate_total_revenue(test_transactions)
    print(f"Revenue: {revenue}")