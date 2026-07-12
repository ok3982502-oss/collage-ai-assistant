import json

def get_department_info(department_name):
    with open("data/college_data.json", "r") as file:
        data = json.load(file)

    for department in data["departments"]:
        if department["department"].lower() == department_name.lower():
            return department

    return None