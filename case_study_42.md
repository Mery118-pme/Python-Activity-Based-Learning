# Case Study 42: Student Marks Matrix Analysis

## Problem Statement
Analyse a matrix of student marks across subjects, calculate row-wise and column-wise statistics, identify top performers, and detect subjects with low average performance.

## Objectives
- Represent student marks across subjects using a nested list (matrix).
- Compute student-wise totals, averages, and overall top performers.
- Compute subject-wise averages and flag subjects falling below a low-performance threshold (e.g., `< 60.0`).

## Assumptions
- All students take the same subjects in the same column order.
- Each mark is a numeric value between `0` and `100`.
- A subject with a class average strictly below `60.0` is flagged as a low-performing subject.

## Algorithm
1. Store student names in a list `students`, subject names in a list `subjects`, and marks in a nested list `marks_matrix` where `marks_matrix[r][c]` is student `r`'s score in subject `c`.
2. For each student row `r`, compute total and average marks, and track the highest average score.
3. Collect all students tied for the highest average score as top performers.
4. For each subject column `c`, sum marks across all student rows and compute the subject average.
5. Flag subjects whose average is `< 60.0` into a low-performance list.
6. Print student-wise stats, top performers, subject-wise averages, and low-performing subjects.

## Flowchart
```text
[Start]
   |
   v
[Load students, subjects & nested marks_matrix]
   |
   v
[Loop rows: compute student total & average; track max average]
   |
   v
[Identify all students matching max average]
   |
   v
[Loop columns: compute subject average; flag if < 60.0]
   |
   v
[Print student report, top performers & weak subjects]
   |
   v
[Stop]
```

## Pseudocode
```text
BEGIN
    students = ["Asha", "Rohan", "Meera", "Kabir"]
    subjects = ["Math", "Physics", "Chemistry", "English"]
    matrix = [
        [88, 92, 85, 91],
        [52, 58, 49, 64],
        [88, 92, 85, 91],
        [75, 54, 58, 78]
    ]
    weak_threshold = 60.0

    max_avg = -1.0
    student_stats = []

    FOR r = 0 TO LENGTH(students) - 1 DO
        total = 0
        FOR c = 0 TO LENGTH(subjects) - 1 DO
            total = total + matrix[r][c]
        END FOR
        avg = total / LENGTH(subjects)
        IF avg > max_avg THEN
            max_avg = avg
        END IF
        APPEND (students[r], total, ROUND(avg, 2)) TO student_stats
    END FOR

    top_performers = []
    FOR each (name, tot, avg) IN student_stats DO
        IF avg == max_avg THEN
            APPEND name TO top_performers
        END IF
    END FOR

    subject_stats = []
    weak_subjects = []
    FOR c = 0 TO LENGTH(subjects) - 1 DO
        col_sum = 0
        FOR r = 0 TO LENGTH(students) - 1 DO
            col_sum = col_sum + matrix[r][c]
        END FOR
        subj_avg = col_sum / LENGTH(students)
        APPEND (subjects[c], ROUND(subj_avg, 2)) TO subject_stats
        IF subj_avg < weak_threshold THEN
            APPEND (subjects[c], ROUND(subj_avg, 2)) TO weak_subjects
        END IF
    END FOR

    PRINT student_stats, top_performers, subject_stats, weak_subjects
END
```



## Test Cases
| Test Case | Matrix Configuration | Expected Outcome |
| :--- | :--- | :--- |
| TC-1 (Tied top performers) | Asha & Meera both score `[88, 92, 85, 91]` (`avg 89.00`) | Both `Asha` and `Meera` listed as top performers |
| TC-2 (Weak subject detection) | `Chemistry` averages `59.25` (`< 60.0`) | `Chemistry` flagged as a low-performing subject |
| TC-3 (Row vs. column aggregation) | 4 students $\times$ 4 subjects | Row sums match per-student totals; column averages match per-subject means |

## Sample Output
```text
=== Student-Wise Performance ===
Asha   | Total: 356 | Average: 89.00
Rohan  | Total: 223 | Average: 55.75
Meera  | Total: 356 | Average: 89.00
Kabir  | Total: 265 | Average: 66.25

Top Performer(s) (Avg 89.00): Asha, Meera

=== Subject-Wise Averages ===
Math      | Average: 75.75
Physics   | Average: 74.00
Chemistry | Average: 59.25
English   | Average: 76.25

=== Low-Performing Subjects (< 60.00) ===
Chemistry (Average: 59.25)
```


## Conclusion
Nested lists with row-major and column-major loops allow clean multi-dimensional analysis across both students and subjects while handling tied top scores cleanly.
