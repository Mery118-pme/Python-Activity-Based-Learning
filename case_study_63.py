def analyze_price_fluctuations(products, threshold=15.0):
    summaries = []
    flagged = []
    peak_fluctuation = None
    peak_mag = -1.0

    for prod_code, prod_name, prices in products:
        if len(prices) < 2:
            raise ValueError(f"Product {prod_code} needs at least two prices to compute fluctuations.")

        max_mag = -1.0
        max_signed_pct = 0.0

        for idx in range(1, len(prices)):
            prev_price = float(prices[idx - 1])
            curr_price = float(prices[idx])
            if prev_price <= 0:
                raise ValueError(f"Previous price must be positive for {prod_code}.")

            pct_change = ((curr_price - prev_price) / prev_price) * 100.0
            magnitude = pct_change if pct_change >= 0 else -pct_change

            if magnitude > max_mag:
                max_mag = magnitude
                max_signed_pct = pct_change

        start_price = float(prices[0])
        end_price = float(prices[-1])
        rounded_signed = round(max_signed_pct, 2)
        rounded_mag = round(max_mag, 2)

        row = (prod_code, prod_name, start_price, end_price, rounded_signed, rounded_mag)
        summaries.append(row)

        if rounded_mag > threshold:
            flagged.append((prod_code, prod_name, rounded_signed))

        if rounded_mag > peak_mag:
            peak_mag = rounded_mag
            peak_fluctuation = row

    return summaries, flagged, peak_fluctuation


if __name__ == "__main__":
    fluctuation_threshold = 15.0
    product_histories = [
        ("P01", "USB Hub", [500.0, 520.0, 610.0, 595.0]),
        ("P02", "Keyboard", [1200.0, 1180.0, 1210.0, 1190.0]),
        ("P03", "Webcam", [2000.0, 1600.0, 1650.0, 1580.0]),
    ]

    summary_rows, flagged_items, highest_item = analyze_price_fluctuations(
        product_histories, fluctuation_threshold
    )

    print("=== Product Price Fluctuation Summary ===")
    for code, name, start_p, end_p, signed_pct, _ in summary_rows:
        sign_str = f"+{signed_pct:.2f}%" if signed_pct > 0 else f"{signed_pct:.2f}%"
        print(f"{code} | {name:<10} | Start: Rs. {start_p:<7.2f} -> End: Rs. {end_p:<7.2f} | Max Change: {sign_str}")

    print(f"\n=== Flagged Products (Fluctuation > {fluctuation_threshold:.2f}%) ===")
    if not flagged_items:
        print("None")
    else:
        for code, name, signed_pct in flagged_items:
            sign_str = f"+{signed_pct:.2f}%" if signed_pct > 0 else f"{signed_pct:.2f}%"
            print(f"{code} ({name}): {sign_str}")

    if highest_item is not None:
        h_code, h_name, _, _, h_signed, h_mag = highest_item
        h_sign_str = f"+{h_signed:.2f}%" if h_signed > 0 else f"{h_signed:.2f}%"
        print(f"\nHighest Overall Fluctuation : {h_code} ({h_name}) with {h_mag:.2f}% magnitude ({h_sign_str})")
