def format_data_for_display(people):
    return [f"{person['first_name']} {person['last_name']}, {person['title']}, {person['age']} years old" for person in people]

def format_data_for_excel(people):
    lines = ["first_name,last_name,title,age"]
    for person in people:
        lines.append(f"{person['first_name']},{person['last_name']},{person['title']},{person['age']}")
    return "\n".join(lines)