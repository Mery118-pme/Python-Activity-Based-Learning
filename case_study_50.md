# Case Study 50: Tuple-Based Route Distance Analysis

## Problem Statement
Store geographical coordinates as tuples, calculate distances between successive points using a supplied formula, and identify the longest route segment.

## Objectives
- Represent route waypoints as coordinate tuples inside a list.
- Compute Euclidean distance between each pair of consecutive waypoints using $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ (via `** 0.5`).
- Identify the longest route segment along with the total route distance.

## Assumptions
- Coordinates are numeric `(x, y)` values in a 2D plane (e.g., kilometers or grid units).
- A route has at least `2` waypoints so at least `1` segment exists.
- The longest segment is the one with the maximum distance (first occurrence kept on exact ties).

## Algorithm
1. Store waypoints as a list of `(waypoint_name, x, y)` tuples.
2. Validate that at least `2` waypoints exist.
3. Loop from index `1` to `len(waypoints) - 1`:
   - Unpack previous waypoint `(name1, x1, y1)` and current waypoint `(name2, x2, y2)`.
   - Compute `dx = x2 - x1`, `dy = y2 - y1`, and `dist = ((dx ** 2) + (dy ** 2)) ** 0.5`.
   - Append `(segment_num, name1, name2, round(dist, 2))` to `segments` and add `dist` to `total_distance`.
   - Track the segment with the largest distance.
4. Display each segment's distance, total route distance, and the longest segment.

## Flowchart
```text
          ┌───────────────────────┐
          │         Start         │
          └───────────┬───────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Load list of (name, x, y) coordinate tuples│
│ and validate len(waypoints) >= 2          │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Loop idx = 1 to n - 1:                    │
│ Unpack prev & curr waypoint tuples        │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Compute dx = x2 - x1, dy = y2 - y1        │
│ dist = ((dx ** 2) + (dy ** 2)) ** 0.5     │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Add dist to total_distance;               │
│ append segment tuple to segments list     │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
               ┌─────────────┐
               │dist>max_dist│
               └──────┬──────┘
                      │
         ┌────────────┴────────────┐
        Yes                       No
         │                         │
         ▼                         │
┌─────────────────┐                │
│ Update max_dist │                │
│ & longest_seg   │                │
└────────┬────────┘                │
         │                         │
         └────────────┬────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Print segments, total distance &          │
│ longest route segment                     │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │         Stop          │
          └───────────────────────┘
```

## Pseudocode
```text
BEGIN
    points = [("Start", 0.0, 0.0), ("StopA", 3.0, 4.0), ("StopB", 3.0, 16.0), ("End", 8.0, 16.0)]
    segments = []
    total_dist = 0.0
    longest_seg = None
    max_dist = -1.0

    FOR i = 1 TO LENGTH(points) - 1 DO
        p1_name, x1, y1 = points[i - 1]
        p2_name, x2, y2 = points[i]
        dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        total_dist = total_dist + dist
        seg = (i, p1_name, p2_name, ROUND(dist, 2))
        APPEND seg TO segments
        IF dist > max_dist THEN
            max_dist = dist
            longest_seg = seg
        END IF
    END FOR

    PRINT segments
    PRINT ROUND(total_dist, 2)
    PRINT longest_seg
END
```


## Test Cases
| Test Case | Waypoint Segment | Expected Distance |
| :--- | :--- | :--- |
| TC-1 (3-4-5 triangle) | `Start (0, 0)` to `StopA (3, 4)` | `5.00` units |
| TC-2 (Vertical segment) | `StopA (3, 4)` to `StopB (3, 16)` | `12.00` units (longest segment) |
| TC-3 (Horizontal segment) | `StopB (3, 16)` to `End (8, 16)` | `5.00` units |

## Sample Output
```text
=== Route Segment Distances ===
Segment 1: Start (0.0, 0.0) -> StopA (3.0, 4.0) | Distance: 5.00
Segment 2: StopA (3.0, 4.0) -> StopB (3.0, 16.0) | Distance: 12.00
Segment 3: StopB (3.0, 16.0) -> End (8.0, 16.0) | Distance: 5.00

Total Route Distance : 22.00
Longest Segment      : Segment 2 (StopA -> StopB) with distance 12.00
```

## Conclusion
Using coordinate tuples with tuple unpacking and exponentiation (`** 0.5`) computes segment distances, cumulative route length, and longest-leg identification cleanly without external math imports.
