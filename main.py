# Candidate Verification System
from pyscript import document, display

# Uses a list to group ICT club members
ict_club_members = [
    "Joshua Ortiz",
    "Enzo Ruiz",
    "Logan Anaque",
    "Doctor Doom",
    "John Hizon",
    "Khabib Nurmagomedov"
]

# Combines the first and last name inputted and checks if they are in the ICT club members list
def check_club_member(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    club_member_name = first_name + " " + last_name
    is_member = club_member_name in ict_club_members

# Different messages shown to the user depending on whether they are a member or not
    messages = [
        "Sorry " + club_member_name + ", your name is not on the list.",
        "Congratulations " + club_member_name + "! You are now part of the ICT club."
    ]

# Displays the Candidate Verification System
    document.getElementById("result").innerHTML = ""
    display(messages[is_member], target="result")
