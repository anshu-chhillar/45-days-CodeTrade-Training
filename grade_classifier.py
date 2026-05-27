#grade_classifier.py classifies students into grades based on scores

students = [
    {"name": "Anshu", "score":92},

    {"name": "Rahul", "score": 18},

    {"name": "Priya", "score": 47},

    {"name": "Aman", "score": 65},

    {"name": "Neha", "score": 84}
]

def classify(score):
    if score >= 90:
        return"A"
        
    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"

sorted_students = sorted(
    students,
    key = lambda student: student["score"],
    reverse = True
)

print("Student Grades:\n")

for student in sorted_students:

    grade = classify(student["score"])

    print(
        f"{student['name']} "
        f"(Score: {student['score']}) "
        f"-> Grade: {grade}"
    )