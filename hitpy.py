from pyscript import display, document

# Class definition
class Classmate:
    def __init__(self, name, section, status):
        self.name = name
        self.section = section
        self.status = status

    def introduce(self):
        return f"Name: {self.name} | Section: {self.section} | Status: {self.status}"


# Initial classmates list
classmates = [
    Classmate("Lewis Laeda", "Emerald", "Alive"),
    Classmate("Eris Salvador", "Emerald", "Dead"),
    Classmate("Wilwen Omnes", "Emerald", "Hospitalized"),
    Classmate("Stephanie Flores", "Ruby", "Alive"),
    Classmate("Arianne Aguilar", "Ruby", "Dead"),
]


# Function to add classmate
def add_classmate(e):

    name = document.getElementById("name").value
    section = document.getElementById("section").value
    status = document.getElementById("status").value

    # (I used conditionals for validation)
    if name == "" or section == "":
        display("Please complete all fields.", target="output")
        return

    new_student = Classmate(name, section, status) # create a new object

    classmates.append(new_student)  # add to list

    document.getElementById("output").innerHTML = ""  # this clears the previous output

    display(f"{name} added successfully!", target="output")

    # Clear input fields
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""


# Function to show list
def show_list(e):

    # Clear previous output
    document.getElementById("output").innerHTML = ""

    # Display all classmates
    for student in classmates:
        display(student.introduce(), append=True, target="output")