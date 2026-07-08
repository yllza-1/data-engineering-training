students = [
    {"id": 1, "name": "Arta",  "city": "Vushtrri",  "course": "Python", "age": 17, "attendance": 90, "homework": 85},
    {"id": 2, "name": "Blend", "city": "Prishtina", "course": "React", "age": 18, "attendance": 60, "homework": 70},
    {"id": 3, "name": "Dion",  "city": "Vushtrri",  "course": "Python", "age": 16, "attendance": 75, "homework": 95},
    {"id": 4, "name": "Elira", "city": "Mitrovica", "course": "React", "age": 17, "attendance": 80, "homework": 60},
    {"id": 5, "name": "Faton", "city": "Vushtrri",  "course": "Data Engineering", "age": 19, "attendance": 100, "homework": 90},
    {"id": 6, "name": "Gresa", "city": "Prishtina", "course": "Python", "age": 18, "attendance": 55, "homework": 88},
]


def get_status(s):
    if s["attendance"] >= 80 and s["homework"] >= 80:
        return "Strong"
    elif s["attendance"] >= 60 and s["homework"] >= 60:
        return "Average"
    else:
        return "Needs Support"


def print_total(students):
    print(f"Total students: {len(students)}")


def print_names(students):
    print("\nStudent names:")
    for s in students:
        print(s["name"])


def print_details(students):
    print("\nStudent details:")
    for s in students:
        print(f"{s['name']} is from {s['city']} and is learning {s['course']}.")


def filter_by_city(students, city):
    print(f"\nStudents from {city}:")
    for s in students:
        if s["city"] == city:
            print(s["name"])


def filter_low_attendance(students):
    print("\nStudents with low attendance:")
    for s in students:
        if s["attendance"] < 70:
            print(s["name"])


def filter_high_homework(students):
    print("\nStudents with homework score above 85:")
    for s in students:
        if s["homework"] > 85:
            print(s["name"])


def calculate_averages(students):
    avg_attendance = sum(s["attendance"] for s in students) / len(students)
    avg_homework = sum(s["homework"] for s in students) / len(students)

    print(f"\nAverage attendance: {avg_attendance:.2f}")
    print(f"Average homework score: {avg_homework:.2f}")


def count_by_field(students, key):
    result = {}
    for s in students:
        result[s[key]] = result.get(s[key], 0) + 1
    return result


def print_counts(title, data):
    print(f"\n{title}")
    for k, v in data.items():
        print(f"{k}: {v}")


def print_performance(students):
    print("\nPerformance status:")
    for s in students:
        print(f"{s['name']}: {get_status(s)}")


def build_clean_report(students):
    report = []
    for s in students:
        report.append({
            "student_id": s["id"],
            "name": s["name"],
            "course": s["course"],
            "performance_status": get_status(s)
        })
    return report


def print_clean_report(report):
    print("\nClean report records:")
    for r in report:
        print(f"{r['student_id']} - {r['name']} - {r['course']} - {r['performance_status']}")


def is_empty(data):
    if not data:
        print("No students available.")
        return True
    return False



def get_score(s):
    return s["attendance"] + s["homework"]

    
def add_student(students, student):
    students.append(student)
    

def sort_by_homework(students):
    return sorted(students, key=lambda s: s["homework"], reverse=True)

def print_sorted_homework(students):
    print("\nStudents sorted by homework :")
    for s in sort_by_homework(students):
        print(f"{s['name']}")
      


def top_3_students(students):
    return sorted(students, key=get_score, reverse=True)[:3]


def print_top_3(students):
    print("\n Top 3 students:")
    for s in top_3_students(students):
        print(f"{s['name']}")

def build_report(students):
    report = []
    for s in students:
        report.append({
            "id": s["id"],
            "name": s["name"],
            "course": s["course"],
            "status": get_status(s)
        })
    return report


def print_report(report):
    print("\n📄 Report:")
    for r in report:
        print(f"{r['id']} - {r['name']} - {r['course']} - {r['status']}")


def main():
    if is_empty(students):
        return

    print_total(students)
    print_names(students)
    print_details(students)

    filter_by_city(students, "Vushtrri")
    filter_low_attendance(students)
    filter_high_homework(students)

    calculate_averages(students)

    city_count = count_by_field(students, "city")
    course_count = count_by_field(students, "course")

    print_counts("Students by city:", city_count)
    print_counts("Students by course:", course_count)

    print_performance(students)

    new_student = {
        "id": 7,
        "name": "Yllza",
        "city": "Prishtina",
        "course": "Python",
        "age": 18,
        "attendance": 92,
        "homework": 96
    }

    add_student(students, new_student)


    print_sorted_homework(students)

    print_top_3(students)

    report = build_clean_report(students)
    print_clean_report(report)


main()