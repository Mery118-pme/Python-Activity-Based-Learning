def detect_shift_conflicts(shifts):
    conflicts = []
    conflicted_employees = []

    for emp_id, shift_code, start_hr, end_hr in shifts:
        if not (0 <= start_hr < end_hr <= 24):
            raise ValueError(f"Invalid shift hours ({start_hr}-{end_hr}) for {emp_id} ({shift_code}).")

    total_shifts = len(shifts)
    for i in range(total_shifts - 1):
        emp1, code1, s1, e1 = shifts[i]
        for j in range(i + 1, total_shifts):
            emp2, code2, s2, e2 = shifts[j]
            if emp1 == emp2 and s1 < e2 and s2 < e1:
                conflicts.append((emp1, code1, code2, s1, e1, s2, e2))
                if emp1 not in conflicted_employees:
                    conflicted_employees.append(emp1)

    return conflicts, conflicted_employees


if __name__ == "__main__":
    sample_shifts = [
        ("E101", "SH1", 8, 14),
        ("E101", "SH2", 12, 18),
        ("E102", "SH3", 9, 13),
        ("E102", "SH4", 13, 17),
        ("E103", "SH5", 10, 16),
        ("E103", "SH6", 14, 15),
    ]

    found_conflicts, flagged_emps = detect_shift_conflicts(sample_shifts)

    print("=== Shift Conflict Report ===")
    if not found_conflicts:
        print("No shift conflicts found.")
    else:
        for emp, c1, c2, st1, en1, st2, en2 in found_conflicts:
            print(f"Conflict: {emp} | {c1} ({st1:02d}:00-{en1:02d}:00) overlaps with {c2} ({st2:02d}:00-{en2:02d}:00)")

    print("\nEmployees with Conflicting Schedules:", ", ".join(flagged_emps) if flagged_emps else "None")
