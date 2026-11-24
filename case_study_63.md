# Case Study 63: Multi-Product Price Fluctuation Analysis

## Problem Statement
Process historical product prices stored in lists, calculate percentage changes, identify maximum fluctuations, and flag products exceeding a supplied threshold.

## Objectives
- Represent historical price series across multiple products using lists of prices.
- Calculate period-over-period percentage changes and overall price change across each product's history.
- Identify the maximum fluctuation and flag products whose maximum absolute percentage jump/drop exceeds a specified threshold (e.g., `15.0%`).

## Assumptions
- Each product entry is a tuple `(product_code, product_name, price_list)` where `price_list` contains at least `2` positive numeric prices in chronological order.
- Period-over-period percentage change from `prev_price` to `curr_price` is `((curr_price - prev_price) / prev_price) * 100`.
- Fluctuation magnitude for a step is the absolute percentage change (`abs(pct_change)`), and a product is flagged if its maximum single-step percentage fluctuation is `>=` (or `>`) `15.0%`.

## Algorithm
1. Store product records as a list of `(prod_code, prod_name, prices)` tuples and set `alert_threshold = 15.0`.
2. For each product, validate that `len(prices) >= 2`.
3. Loop through consecutive price pairs `(prices[i - 1], prices[i])`:
   - Compute `pct_change = ((curr_p - prev_p) / prev_p) * 100` and `magnitude = abs(pct_change)`.
   - Track the step with the largest `magnitude` for that product.
4. Store `(prod_code, prod_name, first_price, last_price, round(max_signed_pct, 2), round(max_mag, 2))` in `summary_list`.
5. If `max_mag > alert_threshold`, append `(prod_code, prod_name, round(max_signed_pct, 2))` to `flagged_products`.
6. Also identify the single product with the highest overall maximum fluctuation across all products.
7. Display the product summary, flagged products, and top fluctuation product.

## Flowchart
```text
[Start]
   |
   v
[Load (code, name, prices_list) tuples & threshold]
   |
   v
[For each product: loop consecutive prices (prev_p, curr_p)]
   |
   v
[Compute pct_change & abs(pct_change); track max fluctuation]
   |
   v
[Store product summary; if max_mag > threshold, flag product]
   |
   v
[Identify highest overall fluctuation across products]
   |
   v
[Print summary, flagged products & peak fluctuation]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    threshold = 15.0
    products = [
        ("P01", "USB Hub", [500.0, 520.0, 610.0, 595.0]),
        ("P02", "Keyboard", [1200.0, 1180.0, 1210.0, 1190.0]),
        ("P03", "Webcam", [2000.0, 1600.0, 1650.0, 1580.0])
    ]
    summaries = []
    flagged = []

    FOR each (code, name, prices) IN products DO
        max_mag = -1.0
        max_signed = 0.0
        FOR i = 1 TO LENGTH(prices) - 1 DO
            prev_p = prices[i - 1]
            curr_p = prices[i]
            pct = ((curr_p - prev_p) / prev_p) * 100.0
            IF pct < 0 THEN
                mag = -pct
            ELSE
                mag = pct
            END IF
            IF mag > max_mag THEN
                max_mag = mag
                max_signed = pct
            END IF
        END FOR

        APPEND (code, name, prices[0], prices[LENGTH(prices) - 1], ROUND(max_signed, 2), ROUND(max_mag, 2)) TO summaries
        IF max_mag > threshold THEN
            APPEND (code, name, ROUND(max_signed, 2)) TO flagged
        END IF
    END FOR

    PRINT summaries, flagged
END
```



## Test Cases
| Test Case | Product Price History | Max Step Change | Threshold `> 15.0%` |
| :--- | :--- | :--- | :--- |
| TC-1 (Upward jump) | `USB Hub`: `[500.0, 520.0, 610.0, 595.0]` | `+17.31%` (`520 -> 610`) | Flagged (`17.31% > 15.0%`) |
| TC-2 (Stable prices) | `Keyboard`: `[1200.0, 1180.0, 1210.0, 1190.0]` | `+2.54%` (`1180 -> 1210`) | Not flagged |
| TC-3 (Sharp drop) | `Webcam`: `[2000.0, 1600.0, 1650.0, 1580.0]` | `-20.00%` (`2000 -> 1600`) | Flagged (`20.00% > 15.0%`, highest overall) |

## Sample Output
```text
=== Product Price Fluctuation Summary ===
P01 | USB Hub    | Start: Rs. 500.00 -> End: Rs. 595.00  | Max Change: +17.31%
P02 | Keyboard   | Start: Rs. 1200.00 -> End: Rs. 1190.00 | Max Change: +2.54%
P03 | Webcam     | Start: Rs. 2000.00 -> End: Rs. 1580.00 | Max Change: -20.00%

=== Flagged Products (Fluctuation > 15.00%) ===
P01 (USB Hub): +17.31%
P03 (Webcam): -20.00%

Highest Overall Fluctuation : P03 (Webcam) with 20.00% magnitude (-20.00%)
```


## Conclusion
Tracking consecutive percentage changes and absolute fluctuation magnitudes across nested price lists enables reliable volatility detection and threshold alerting using basic lists, tuples, loops, and conditionals.
