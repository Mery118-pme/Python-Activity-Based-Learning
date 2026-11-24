def analyze_route(waypoints):
    if len(waypoints) < 2:
        raise ValueError("At least two waypoints are required to form a route segment.")

    segments = []
    total_distance = 0.0
    longest_segment = None
    max_dist = -1.0

    for idx in range(1, len(waypoints)):
        name1, x1, y1 = waypoints[idx - 1]
        name2, x2, y2 = waypoints[idx]

        dx = float(x2) - float(x1)
        dy = float(y2) - float(y1)
        dist = ((dx ** 2) + (dy ** 2)) ** 0.5

        total_distance += dist
        rounded_dist = round(dist, 2)
        seg_tuple = (idx, name1, x1, y1, name2, x2, y2, rounded_dist)
        segments.append(seg_tuple)

        if dist > max_dist:
            max_dist = dist
            longest_segment = seg_tuple

    return segments, round(total_distance, 2), longest_segment


if __name__ == "__main__":
    route_points = [
        ("Start", 0.0, 0.0),
        ("StopA", 3.0, 4.0),
        ("StopB", 3.0, 16.0),
        ("End", 8.0, 16.0),
    ]

    seg_list, total_dist, longest = analyze_route(route_points)

    print("=== Route Segment Distances ===")
    for seg_no, n1, x1, y1, n2, x2, y2, dist in seg_list:
        print(f"Segment {seg_no}: {n1} ({x1:.1f}, {y1:.1f}) -> {n2} ({x2:.1f}, {y2:.1f}) | Distance: {dist:.2f}")

    print(f"\nTotal Route Distance : {total_dist:.2f}")
    if longest is not None:
        l_no, ln1, _, _, ln2, _, _, l_dist = longest
        print(f"Longest Segment      : Segment {l_no} ({ln1} -> {ln2}) with distance {l_dist:.2f}")
