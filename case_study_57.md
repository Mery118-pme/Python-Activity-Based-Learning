# Case Study 57: Smart Canteen Order and Stock Management

## Problem Statement
Process successive customer orders, calculate bills, update available inventory, reject unavailable quantities, and summarize daily sales and remaining stock[cite: 5].

## Objectives
- Maintain a canteen menu/inventory list of `(item_code, item_name, unit_price, stock_qty)` tuples (or parallel lists/tuples) and update stock as orders are fulfilled[cite: 5].
- Validate each order item for valid item code, positive order quantity, and sufficient stock[cite: 5].
- Reject orders with insufficient stock or invalid quantities without deducting inventory, and produce a daily sales and remaining stock summary[cite: 5].

## Assumptions
- Each canteen item has a unique `item_code`, `item_name`, `unit_price` (Rs.), and initial `stock_qty` (integer).
- Each customer order is represented as `(order_id, item_code, qty_requested)`.
- If requested quantity exceeds available stock (or is `<= 0` or item code is not found), the order is rejected.

## Algorithm
1. Store canteen items in a list of tuples `[code, name, price, stock]`? Since tuples are immutable, store item entries in a list of lists `[[code, name, price, stock], ...]` so stock can be updated in place while using tuple unpacking for incoming orders `(order_id, code, qty)`.
2. Initialize `total_revenue = 0.0`, `accepted_orders = []`, and `rejected_orders = []`.
3. For each `(order_id, code, qty)` in `orders`:
   - Search `inventory` for matching `code`.
   - If not found or `qty <= 0`, append a rejection tuple to `rejected_orders`.
   - Else if `qty > item[3]` (available stock), append a rejection tuple (`"Insufficient stock"`) to `rejected_orders`.
   - Else subtract `qty` from `item[3]`, compute `bill = qty * item[2]`, add `bill` to `total_revenue`, and append `(order_id, code, item[1], qty, round(bill, 2))` to `accepted_orders`.
4. Print accepted orders, rejected orders, total daily revenue, and remaining stock.

## Flowchart
```text
[Start]
   |
   v
[Load inventory list & orders list of (order_id, code, qty) tuples]
   |
   v
[For each (order_id, code, qty) in orders]
   |
   +--> (code exists & qty > 0?)
           |--No--> [Append to rejected_orders]
           |--Yes-> (qty <= stock?)
                       |--No--> [Append to rejected_orders: insufficient stock]
                       |--Yes-> [Deduct stock, compute bill, add to revenue & accepted_orders]
   |
   v
[Print accepted orders, rejected orders, daily revenue & remaining stock]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    inventory = [
        ["C01", "Veg Sandwich", 45.0, 20],
        ["C02", "Masala Dosa", 60.0, 15],
        ["C03", "Cold Coffee", 50.0, 25]
    ]
    orders = [
        ("ORD1", "C01", 3),
        ("ORD2", "C02", 20),
        ("ORD3", "C03", 4),
        ("ORD4", "C02", 5),
        ("ORD5", "C99", 1)
    ]
    total_revenue = 0.0
    accepted = []
    rejected = []

    FOR each (oid, code, qty) IN orders DO
        found_idx = -1
        FOR i = 0 TO LENGTH(inventory) - 1 DO
            IF inventory[i][0] == code THEN
                found_idx = i
                BREAK
            END IF
        END FOR

        IF found_idx == -1 THEN
            APPEND (oid, code, qty, "Item code not found") TO rejected
        ELSE IF qty <= 0 THEN
            APPEND (oid, code, qty, "Quantity must be positive") TO rejected
        ELSE IF qty > inventory[found_idx][3] THEN
            APPEND (oid, code, qty, "Insufficient stock") TO rejected
        ELSE
            inventory[found_idx][3] = inventory[found_idx][3] - qty
            bill = qty * inventory[found_idx][2]
            total_revenue = total_revenue + bill
            APPEND (oid, code, inventory[found_idx][1], qty, ROUND(bill, 2)) TO accepted
        END IF
    END FOR

    PRINT accepted, rejected, ROUND(total_revenue, 2), inventory
END
```



## Test Cases
| Test Case | Order Input `(OrderID, Code, Qty)` | Expected Result |
| :--- | :--- | :--- |
| TC-1 (Valid order) | `("ORD1", "C01", 3)` | Accepted; bill `Rs. 135.00`; `C01` stock drops `20 -> 17` |
| TC-2 (Exceeds stock) | `("ORD2", "C02", 20)` (stock `15`) | Rejected (`Insufficient stock`); `C02` stock remains `15` |
| TC-3 (Subsequent valid order) | `("ORD4", "C02", 5)` (stock `15`) | Accepted; bill `Rs. 300.00`; `C02` stock drops `15 -> 10` |
| TC-4 (Unknown item) | `("ORD5", "C99", 1)` | Rejected (`Item code not found`) |

## Sample Output
```text
=== Accepted Orders ===
ORD1 | C01 (Veg Sandwich) x 3 | Bill: Rs. 135.00
ORD3 | C03 (Cold Coffee) x 4 | Bill: Rs. 200.00
ORD4 | C02 (Masala Dosa) x 5 | Bill: Rs. 300.00

=== Rejected Orders ===
ORD2 | Item: C02 | Qty: 20 | Reason: Insufficient stock
ORD5 | Item: C99 | Qty: 1 | Reason: Item code not found

=== Daily Summary ===
Total Sales Revenue : Rs. 635.00

Remaining Stock:
  C01 - Veg Sandwich : 17
  C02 - Masala Dosa  : 10
  C03 - Cold Coffee  : 21
```

## Conclusion
Combining mutable inventory rows inside a list with tuple unpacking for incoming orders and audit records keeps stock updates consistent and prevents overselling.
