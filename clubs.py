from pyscript import document

from pyscript import document

clubs = {
    "Science Club": """ Science Club
- Meeting Time: Mondays 3:00-4:30 PM
- Adviser: Mr. Joald Calpo
- Number of Members: 15
- Category: Academic
Description: A club for students interested in experiments, research projects, and science fairs. Encourages critical thinking and innovation!""",

    "Varsity": """ Varsity
- Meeting Time: Wednesdays 2:30-4:00 PM
- Adviser: Mr. Mark Gervacio
- Number of Members: 30
- Category: Academic
Description: A club for Athlete's who enjoy sports!""",

    "Math Club": """ Math Club
- Meeting Time: Fridays 3:00-4:00 PM
- Adviser: Mr. Rejean Banting
- Number of Members: 20
- Category: Academic
Description: A club for students who love problem-solving, competitions, and logic games. Enhances analytical thinking and teamwork!"""
}

def show_club(event=None):
    select = document.querySelector("#club-select")
    output = document.querySelector("#club-output")

    selected = select.value
    description = clubs.get(selected, "No info available.")

    output.innerText = description



