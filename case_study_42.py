def analyze_marks_matrix(students, subjects, matrix, low_threshold=60.0):
    num_students = len(students)
    num_subjects = len(subjects)

    for row in matrix:
        if len(row) != num_subjects:
            raise ValueError("Each student row must have marks for every subject.")

    student_summaries = []
    highest_avg = -1.0

    for r in range(num_students):
        row_total = 0
        for c in range(num_subjects):
            row_total += matrix[r][c]
        avg = row_total / num_subjects
        if avg > highest_avg:
            highest_avg = avg
        student_summaries.append((students[r], row_total, round(avg, 2)))

    top_students = []
    for name, _, avg in student_summaries:
        if avg == round(highest_avg, 2):
            top_students.append(name)

    subject_summaries = []
    weak_subjects = []

    for c in range(num_subjects):
        col_total = 0
        for r in range(num_students):
            col_total += matrix[r][c]
        subj_avg = col_total / num_students
        rounded_subj_avg = round(subj_avg, 2)
        subject_summaries.append((subjects[c], rounded_subj_avg))
        if rounded_subj_avg < low_threshold:
            weak_subjects.append((subjects[c], rounded_subj_avg))

    return student_summaries, top_students, round(highest_avg, 2), subject_summaries, weak_subjects


if __name__ == "__main__":
    student_names = ["Asha", "Rohan", "Meera", "Kabir"]
    subject_names = ["Math", "Physics", "Chemistry", "English"]
    marks = [
        [88, 92, 85, 91],
        [52, 58, 49, 64],
        [88, 92, 85, 91],
        [75, 54, 58, 78],
    ]

    stu_stats, top_list, best_avg, subj_stats, weak_list = analyze_marks_matrix(
        student_names, subject_names, marks
    )

    print("=== Student-Wise Performance ===")
    for name, total, avg in stu_stats:
        print(f"{name:<6} | Total: {total:<3} | Average: {avg:.2f}")

    print(f"\nTop Performer(s) (Avg {best_avg:.2f}): {', '.join(top_list)}")

    print("\n=== Subject-Wise Averages ===")
    for subj, s_avg in subj_stats:
        print(f"{subj:<9} | Average: {s_avg:.2f}")

    print("\n=== Low-Performing Subjects (< 60.00) ===")
    if not weak_list:
        print("None")
    else:
        for subj, s_avg in weak_list:
            print(f"{subj} (Average: {s_avg:.2f})")
