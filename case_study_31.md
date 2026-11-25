# Case Study 31: String-Based Examination Answer Evaluation

## Problem Statement
Compare student answer strings against an answer key, calculate correct, incorrect, and unanswered responses, apply negative marking, and produce student-wise results[cite: 3].

## Objectives
- Compare each character of a student's response string against the official answer key string.
- Count correct, incorrect, and unanswered (`'-'`) items.
- Apply positive and negative marking rules to compute each student's net score and percentage.

## Assumptions
- Answer key and student response strings have equal length $N > 0$.
- `'-'` (or `' '` after stripping) denotes an unanswered question (`0` marks).
- Each correct answer awards `+4.0` marks; each incorrect answer deducts `-1.0` mark.

## Algorithm
1. Store the answer key string and a list of `(student_id, response_str)` tuples.
2. For each student, validate that `len(response_str) == len(answer_key)`.
3. Loop through index `0` to `len(answer_key) - 1`:
   - If `response_str[i] == '-'`, increment `unanswered`.
   - Else if `response_str[i] == answer_key[i]`, increment `correct`.
   - Else increment `incorrect`.
4. Compute `net_score = (correct * correct_marks) - (incorrect * negative_marks)` and `max_score = len(answer_key) * correct_marks`.
5. Store `(student_id, correct, incorrect, unanswered, net_score, percentage)` in a results list and print the summary.

## Flowchart
```text
          ┌───────────────────────┐
          │         Start         │
          └───────────┬───────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Load answer_key & list of (sid, response) │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ For each student: check equal length      │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Loop each question index idx              │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
               ┌─────────────┐
               │ resp[idx]=='-'│
               └──────┬──────┘
                      │
         ┌────────────┴────────────┐
        Yes                       No
         │                         │
         ▼                         ▼
┌─────────────────┐         ┌───────────────────┐
│ unanswered += 1 │         │ resp[idx]==key[idx]│
└────────┬────────┘         └─────────┬─────────┘
         │                            │
         │               ┌────────────┴────────────┐
         │              Yes                       No
         │               │                         │
         │               ▼                         ▼
         │      ┌─────────────────┐       ┌─────────────────┐
         │      │ correct += 1    │       │ incorrect += 1  │
         │      └────────┬────────┘       └────────┬────────┘
         │               │                         │
         └───────┬───────┴───────────┬─────────────┘
                 │                   │
                 ▼                   ▼
┌───────────────────────────────────────────┐
│ Compute net_score & percentage            │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│ Print student-wise results table          │
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
    answer_key = "ABCDABCDAB"
    correct_marks = 4.0
    negative_marks = 1.0
    submissions = [("S01", "ABCDABCDAB"), ("S02", "AB-DACBD-B"), ("S03", "DDDDDDDDDD")]
    max_score = LENGTH(answer_key) * correct_marks
    evaluated = []

    FOR each (student_id, response) IN submissions DO
        cleaned = UPPER(TRIM(response))
        IF LENGTH(cleaned) != LENGTH(answer_key) THEN
            RAISE LengthMismatchError
        END IF

        correct = 0
        incorrect = 0
        unanswered = 0

        FOR idx = 0 TO LENGTH(answer_key) - 1 DO
            ans = cleaned[idx]
            IF ans == "-" THEN
                unanswered = unanswered + 1
            ELSE IF ans == answer_key[idx] THEN
                correct = correct + 1
            ELSE
                incorrect = incorrect + 1
            END IF
        END FOR

        net_score = (correct * correct_marks) - (incorrect * negative_marks)
        percentage = (net_score / max_score) * 100.0
        APPEND (student_id, correct, incorrect, unanswered, ROUND(net_score, 2), ROUND(percentage, 2)) TO evaluated
    END FOR

    PRINT evaluated, max_score
END
```


## Test Cases
| Test Case | Response String (Key: `"ABCDABCDAB"`) | Correct / Incorrect / Unanswered | Score (Max 40.0) |
| :--- | :--- | :--- | :--- |
| TC-1 (Full marks) | `"ABCDABCDAB"` | `10 / 0 / 0` | `40.00` (`100.00%`) |
| TC-2 (Mixed + skipped) | `"AB-DACBD-B"` | `5 / 3 / 2` (`5*4 - 3*1`) | `17.00` (`42.50%`) |
| TC-3 (Mostly wrong) | `"DDDDDDDDDD"` | `3 / 7 / 0` (`3*4 - 7*1`) | `5.00` (`12.50%`) |

## Sample Output
```text
Answer Key: ABCDABCDAB (10 Questions, Max Marks: 40.0)

Student | Correct | Wrong | Skipped | Score  | Percentage
-----------------------------------------------------------
S01     | 10      | 0     | 0       | 40.00  | 100.00%
S02     | 5       | 3     | 2       | 17.00  | 42.50%
S03     | 3       | 7     | 0       | 5.00   | 12.50%
```


## Conclusion
Index-by-index string comparison cleanly separates answered and unanswered items while applying positive and negative marking rules accurately.
