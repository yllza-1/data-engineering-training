import csv
import os

# Reads student data from the CSV file.
def read_csv_file():

    try:

        with open(
            "data/students_raw.csv",
            "r",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            students = []

            for row in reader:

                clean_row = {}

                for key, value in row.items():

                    if key is not None:
                        clean_row[key.strip()] = value.strip() if value else ""

                students.append(clean_row)

        return students, list(students[0].keys())

    except FileNotFoundError:

        print("Error: data/students_raw.csv was not found.")

        return [], []

# Displays basic information about the datase
def inspect_records(students, columns):

    print(f"Total raw records: {len(students)}")

    print("Columns:")
    print(", ".join(columns))

    print("First 3 records:")

    for student in students[:3]:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['city']} - "
            f"{student['course']}"
        )

# Finds missing, invalid, and inconsistent data.
def find_data_quality_issues(students):

    issues = []

    for student in students:

        missing_fields = [
            "attendance",
            "homework_score",
            "city",
            "age",
            "registered_date",
            "course"
        ]

        for field in missing_fields:
            if student[field] == "":
                issues.append(
                    f"student_id={student['student_id']}, column={field}"
                )


        for field in ["age", "attendance", "homework_score"]:

            if student[field] != "":
                try:
                    int(student[field])

                except ValueError:
                    issues.append(
                        f"student_id={student['student_id']}, "
                        f"column={field}, "
                        f"value={student[field]}"
                    )

        if student["city"] in ["VUSHTRRI", "prishtina"]:
            issues.append(
                f"student_id={student['student_id']}, "
                f"column=city, "
                f"value={student['city']}"
            )

        if student["course"] == "Data engineering":
            issues.append(
                f"student_id={student['student_id']}, "
                f"column=course, "
                f"value={student['course']}"
            )
    return issues


# Creates the data quality report.
def generate_quality_report(issues):

    report = "Data Quality Report\n"
    report += f"Total issues found: {len(issues)}\n"

    report += "\nMissing values:\n"

    for issue in issues:
        if "value=" not in issue:
            report += issue + "\n"

    report += "\nInvalid numeric values:\n"

    for issue in issues:
        if "value=" in issue and "city" not in issue and "course" not in issue:
            report += issue + "\n"

    report += "\nInconsistent text values:\n"

    for issue in issues:
        if "value=" in issue and ("city" in issue or "course" in issue):
            report += issue + "\n"

    return report

# Saves the data quality report to a text file.
def save_text_report(report):

    os.makedirs("output", exist_ok=True)

    print(report)

    with open(
        "output/data_quality_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

# Cleans and standardizes one student record.
def clean_student(student):

    if student["city"] == "":
        student["city"] = "Unknown"

    if student["city"] == "VUSHTRRI":
        student["city"] = "Vushtrri"

    if student["city"] == "prishtina":
        student["city"] = "Prishtina"

    if student["course"] == "":
        student["course"] = "Not Assigned"

    if student["course"] == "Data engineering":
        student["course"] = "Data Engineering"

    for field in ["age", "attendance", "homework_score"]:

        if student[field] == "":
            student[field] = 0

        try:
            student[field] = int(student[field])
        except ValueError:
            student[field] = 0

    if student["registered_date"] == "":
        student["registered_date"] = "Unknown Date"

    student["total_score"] = (
        student["attendance"] +
        student["homework_score"]
    )

    if (
        student["attendance"] >= 80
        and student["homework_score"] >= 80
    ):
        student["performance_status"] = "Strong"

    elif (
        student["attendance"] >= 60
        and student["homework_score"] >= 60
    ):
        student["performance_status"] = "Average"

    else:
        student["performance_status"] = "Needs Support"

    if (
        student["attendance"] < 60
        or student["homework_score"] < 60
    ):
        student["risk_flag"] = "At Risk"
    else:
        student["risk_flag"] = "OK"

    if student["attendance"] >= 80:
        student["attendance_level"] = "High"
    elif student["attendance"] >= 60:
        student["attendance_level"] = "Medium"
    else:
        student["attendance_level"] = "Low"

    return student

# Saves the cleaned student data to a CSV file.
def save_cleaned_csv(cleaned_students):

    os.makedirs("output", exist_ok=True)

    columns = [
        "student_id",
        "name",
        "city",
        "course",
        "age",
        "attendance",
        "homework_score",
        "registered_date",
        "total_score",
        "performance_status",
        "risk_flag",
        "attendance_level"
    ]

    with open(
        "output/students_clean.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=columns
        )

        writer.writeheader()

        writer.writerows(cleaned_students)

# Generates the final summary report.
def generate_summary_report(students, issues):

    report = "Final Student Data Report\n\n"

    report += f"Total raw records: {len(students)}\n"
    report += f"Total cleaned records: {len(students)}\n"
    report += f"Total data quality issues found: {len(issues)}\n"

    average_attendance = (
        sum(student["attendance"] for student in students)
        / len(students)
    )

    average_homework = (
        sum(student["homework_score"] for student in students)
        / len(students)
    )

    report += f"Average attendance: {average_attendance:.2f}\n"
    report += f"Average homework score: {average_homework:.2f}\n\n"
    report += "Students by city:\n"
    cities = {}

    for student in students:
        city = student["city"]
        cities[city] = cities.get(city, 0) + 1

    for city, count in cities.items():
        report += f"{city}: {count}\n"

    report += "\nStudents by course:\n"

    courses = {}

    for student in students:
        course = student["course"]
        courses[course] = courses.get(course, 0) + 1

    for course, count in courses.items():
        report += f"{course}: {count}\n"

    report += "\nStrong students:\n"

    for student in students:
        if student["performance_status"] == "Strong":
            report += f"{student['name']}\n"

    report += "\nStudents that need support:\n"

    for student in students:
        if student["performance_status"] == "Needs Support":
            report += f"{student['name']}\n"

    report += "\nAt Risk students:\n"

    for student in students:
        if student["risk_flag"] == "At Risk":
            report += f"{student['name']}\n"

    report += "\nPerformance Status:\n"

    for student in students:
        report += (
            f"{student['name']}: "
            f"{student['performance_status']} - "
            f"{student['risk_flag']}\n"
        )

    report += "\nTop 3 students by total score:\n"

    top_students = sorted(
        students,
        key=lambda student: student["total_score"],
        reverse=True
    )

    for student in top_students[:3]:
        report += (
            f"{student['name']}: "
            f"{student['total_score']}\n"
        )

    report += "\nAverage attendance by course:\n"

    attendance_by_course = {}

    for student in students:

        course = student["course"]

        if course not in attendance_by_course:
            attendance_by_course[course] = []

        attendance_by_course[course].append(student["attendance"])

    for course, values in attendance_by_course.items():

        average = sum(values) / len(values)

        report += f"{course}: {average:.2f}\n"

    report += "\nAverage homework score by city:\n"

    homework_by_city = {}

    for student in students:

        city = student["city"]

        if city not in homework_by_city:
            homework_by_city[city] = []

        homework_by_city[city].append(student["homework_score"])

    for city, values in homework_by_city.items():

        average = sum(values) / len(values)

        report += f"{city}: {average:.2f}\n"
    return report

# Saves the summary report to a text file.
def save_summary_report(report):
 
    os.makedirs("output", exist_ok=True)

    print(report)

    with open(
        "output/summary_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

# Checks for duplicate student IDs.
def check_duplicate_ids(students):

    ids = set()

    duplicates = []

    for student in students:

        if student["student_id"] in ids:

            duplicates.append(student["student_id"])

        else:

            ids.add(student["student_id"])

    return duplicates

# Runs the complete CSV data pipeline.
def main():

    students, columns = read_csv_file()

    if not students:
        return

    inspect_records(students, columns)

    issues = find_data_quality_issues(students)

    report = generate_quality_report(issues)

    save_text_report(report)

    cleaned_students = []

    for student in students:
        cleaned_students.append(
            clean_student(student)
        )

    save_cleaned_csv(cleaned_students)

    summary = generate_summary_report(
        cleaned_students,
        issues
    )

    save_summary_report(summary)

    duplicates = check_duplicate_ids(students)

    if duplicates:

        print("\nDuplicate student IDs found:")

        for duplicate in duplicates:

            print(duplicate)

main()