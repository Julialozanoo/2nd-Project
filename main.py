from pyscript import document

subjects = ["science", "math", "english", "filipino", "ict", "pe"]
units = [4, 3, 3, 3, 2, 1]

def calculating_gwa(event=None):
    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()

    grades = []
    for sub in subjects:
        value = document.getElementById(sub).value
        grades.append(float(value) if value else 0)

    weighted_sum = sum(g * u for g, u in zip(grades, units))
    gwa = weighted_sum / sum(units)

    receipt = "--- Student Grades Summary ---\n"
    receipt += f"Name: {first} {last}\n\nSubjects:\n"

    for sub, grade in zip(subjects, grades):
        receipt += f"- {sub.title()}: {grade}\n"

    receipt += f"\nGeneral Weighted Average: {gwa:.2f}"

    document.getElementById("output").innerText = receipt