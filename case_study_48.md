# Case Study 48: Tuple-Based Employee Shift Conflict Detection

## Problem Statement
Represent employee shifts as tuples, compare time intervals, detect overlapping assignments, and identify employees with conflicting schedules.

## Objectives
- Represent each shift assignment as a tuple containing employee ID, shift ID, start hour, and end hour.
- Detect overlapping time intervals for the same employee using tuple unpacking and interval comparison.
- Produce a clear list of conflicting shift pairs and affected employee IDs.

## Assumptions
- Times are represented as 24-hour integers (`0` to `24`) within a single day, with `start < end`.
- Two intervals `[s1, e1)` and `[s2, e2)` overlap if and only if `s1 < e2` and `s2 < e1` (touching boundaries like `[9, 13)` and `[13, 17)` do not overlap).
- Each shift tuple has the format `(emp_id, shift_code, start_hr, end_hr)`.

## Algorithm
1. Store shift assignments as a list of `(emp_id, shift_code, start_hr, end_hr)` tuples.
2. Validate that each shift has `0 <= start_hr < end_hr <= 24`.
3. Use nested loops over pairs of shifts `(i, j)` with `i < j`:
   - Unpack both shift tuples.
   - Check if `emp_id_1 == emp_id_2`.
   - Check if `start_1 < end_2` and `start_2 < end_1`.
   - If true, record `(emp_id_1, shift_code_1, shift_code_2)` in `conflicts` and add `emp_id_1` to `conflicted_employees` if not already present.
4. Display all detected shift conflicts and the list of employees with conflicting schedules.

## Flowchart
```text
          ┌───────────────────────┐
          │         Start         │
          └───────────┬───────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Load list of (emp_id, shift_code, s, e)   │
│ tuples and validate 0 <= s < e <= 24      │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Outer loop: i = 0 to n - 2                │
│ Unpack emp1, code1, s1, e1 = shifts[i]    │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Inner loop: j = i + 1 to n - 1            │
│ Unpack emp2, code2, s2, e2 = shifts[j]    │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
               ┌─────────────┐
               │emp1==emp2 & │
               │s1<e2 & s2<e1│
               └──────┬──────┘
                      │
         ┌────────────┴────────────┐
        Yes                       No
         │                         │
         ▼                         │
┌─────────────────┐                │
│ Append conflict │                │
│ & record emp1   │                │
└────────┬────────┘                │
         │                         │
         └────────────┬────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Print all conflicts & conflicted employees│
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
    shifts = [
        ("E101", "SH1", 8, 14),
        ("E101", "SH2", 12, 18),
        ("E102", "SH3", 9, 13),
        ("E102", "SH4", 13, 17),
        ("E103", "SH5", 10, 16),
        ("E103", "SH6", 14, 15)
    ]
    conflicts = []
    conflicted_emps = []

    FOR i = 0 TO LENGTH(shifts) - 2 DO
        emp1, code1, s1, e1 = shifts[i]
        FOR j = i + 1 TO LENGTH(shifts) - 1 DO
            emp2, code2, s2, e2 = shifts[j]
            IF emp1 == emp2 AND s1 < e2 AND s2 < e1 THEN
                APPEND (emp1, code1, code2, s1, e1, s2, e2) TO conflicts
                IF emp1 NOT IN conflicted_emps THEN
                    APPEND emp1 TO conflicted_emps
                END IF
            END IF
        END FOR
    END FOR

    PRINT conflicts
    PRINT conflicted_emps
END
```



## Test Cases
| Test Case | Shift Pair Compared | Expected Result |
| :--- | :--- | :--- |
| TC-1 (Overlapping shifts) | `("E101", "SH1", 8, 14)` & `("E101", "SH2", 12, 18)` | Overlap detected (`12:00` to `14:00`); `E101` flagged |
| TC-2 (Adjacent shifts) | `("E102", "SH3", 9, 13)` & `("E102", "SH4", 13, 17)` | No overlap (`9 < 17` and `13 < 13` is false) |
| TC-3 (Contained shift) | `("E103", "SH5", 10, 16)` & `("E103", "SH6", 14, 15)` | Overlap detected (`14:00` to `15:00`); `E103` flagged |

## Sample Output
```text
=== Shift Conflict Report ===
Conflict: E101 | SH1 (08:00-14:00) overlaps with SH2 (12:00-18:00)
Conflict: E103 | SH5 (10:00-16:00) overlaps with SH6 (14:00-15:00)

Employees with Conflicting Schedules: E101, E103
```


## Conclusion
Tuple unpacking and pairwise interval checks make schedule overlap detection concise, readable, and free of external dependencies.
