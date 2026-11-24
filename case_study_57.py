def process_canteen_orders(inventory, orders):
    total_revenue = 0.0
    accepted_orders = []
    rejected_orders = []

    for order_id, item_code, qty in orders:
        matched_index = -1
        for idx in range(len(inventory)):
            if inventory[idx][0] == item_code:
                matched_index = idx
                break

        if matched_index == -1:
            rejected_orders.append((order_id, item_code, qty, "Item code not found"))
        elif qty <= 0:
            rejected_orders.append((order_id, item_code, qty, "Quantity must be positive"))
        elif qty > inventory[matched_index][3]:
            rejected_orders.append((order_id, item_code, qty, "Insufficient stock"))
        else:
            inventory[matched_index][3] -= qty
            unit_price = inventory[matched_index][2]
            item_name = inventory[matched_index][1]
            bill_amount = qty * unit_price
            total_revenue += bill_amount
            accepted_orders.append((order_id, item_code, item_name, qty, round(bill_amount, 2)))

    return accepted_orders, rejected_orders, round(total_revenue, 2), inventory


if __name__ == "__main__":
    # Each item row: [item_code, item_name, unit_price, stock_qty]
    canteen_stock = [
        ["C01", "Veg Sandwich", 45.0, 20],
        ["C02", "Masala Dosa", 60.0, 15],
        ["C03", "Cold Coffee", 50.0, 25],
    ]

    customer_orders = [
        ("ORD1", "C01", 3),
        ("ORD2", "C02", 20),
        ("ORD3", "C03", 4),
        ("ORD4", "C02", 5),
        ("ORD5", "C99", 1),
    ]

    accepted, rejected, revenue, updated_stock = process_canteen_orders(canteen_stock, customer_orders)

    print("=== Accepted Orders ===")
    for oid, code, name, q, bill in accepted:
        print(f"{oid} | {code} ({name}) x {q} | Bill: Rs. {bill:.2f}")

    print("\n=== Rejected Orders ===")
    for oid, code, q, reason in rejected:
        print(f"{oid} | Item: {code} | Qty: {q} | Reason: {reason}")

    print("\n=== Daily Summary ===")
    print(f"Total Sales Revenue : Rs. {revenue:.2f}")
    print("\nRemaining Stock:")
    for code, name, _, rem_qty in updated_stock:
        print(f"  {code} - {name:<12} : {rem_qty}")
