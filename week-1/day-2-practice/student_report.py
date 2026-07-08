students = [
    {"id": 1, "name": "Arta",  "city": "Vushtrri",  "course": "Python", "attendance": 90, "homework": 85},
    {"id": 2, "name": "Blend", "city": "Prishtina", "course": "React", "attendance": 60, "homework": 70},
    {"id": 3, "name": "Dion",  "city": "Vushtrri",  "course": "Python", "attendance": 75, "homework": 95},
    {"id": 4, "name": "Elira", "city": "Mitrovica", "course": "React", "attendance": 80, "homework": 60},
    {"id": 5, "name": "Faton", "city": "Vushtrri",  "course": "Data Engineering", "attendance": 100, "homework": 90},
    {"id": 6, "name": "Gresa", "city": "Prishtina", "course": "Python", "attendance": 55, "homework": 88},
]


def get_status(s):
    if s["attendance"] >= 80 and s["homework"] >= 80:
        return "Strong"
    elif s["attendance"] >= 60 and s["homework"] >= 60:
        return "Average"
    else:
        return "Needs Support"


total_students = len(students)
avg_attendance = sum(s["attendance"] for s in students) / total_students
avg_homework = sum(s["homework"] for s in students) / total_students


city_count = {}
course_count = {}

for s in students:
    city_count[s["city"]] = city_count.get(s["city"], 0) + 1
    course_count[s["course"]] = course_count.get(s["course"], 0) + 1


low_attendance = [s for s in students if s["attendance"] < 70]
strong_students = [s for s in students if get_status(s) == "Strong"]
needs_support = [s for s in students if get_status(s) == "Needs Support"]


print(f"Total students: {total_students}")
print(f"Average attendance: {avg_attendance:.2f}")
print(f"Average homework score: {avg_homework:.2f}")

print("\nStudents by city:")
for city, count in city_count.items():
    print(f"{city}: {count}")

print("\nStudents by course:")
for course, count in course_count.items():
    print(f"{course}: {count}")

print("\nStudents with low attendance:")
for s in low_attendance:
    print(s["name"])

print("\nStrong students:")
for s in strong_students:
    print(s["name"])

print("\nStudents that need support:")
for s in needs_support:
    print(s["name"])