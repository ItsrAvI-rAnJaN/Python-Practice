student_records = {
    'Alice': {'Math': 85, 'Science': 90, 'History': 78},
    'Carol': {'Math': 92, 'Science': 88, 'History': 70},
    'Bob': {'Math': 78, 'Science': 95, 'History': 82}
}

highest_science_marks = -1
student_with_highest_science_marks = None

for student, marks in student_records.items():
    science_marks = marks['Science']
    if science_marks > highest_science_marks:
        highest_science_marks = science_marks
        student_with_highest_science_marks = student

print("Student with the highest marks in Science:", student_with_highest_science_marks)
