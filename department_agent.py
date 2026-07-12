from config import client, model_id
from knowledge_agent import get_department_info


def department_agent(query):

    q = query.lower()

    if "cse" in q or "computer" in q:
        department = "Computer Science"

    elif "civil" in q:
        department = "Civil"

    elif "electrical" in q:
        department = "Electrical"

    elif "mechanical" in q:
        department = "Mechanical"

    elif "principal" in q:
        department = "Principal Office"

    elif "academic" in q:
        department = "Academics"

    elif "library" in q:
        department = "Library"

    elif "hostel" in q:
        department = "Hostel"

    elif "placement" in q:
        department = "Placement Cell"

    else:
        return "Sorry, I couldn't identify the department."

    info = get_department_info(department)

    if info is None:
        return "Sorry, department information is not available."

    context = f"""
Department: {info['department']}
Head: {info['head']}
Designation: {info['designation']}
Qualification: {info['qualification']}
Phone: {info['phone']}
Email: {info['email']}
Office: {info['office']}
Meeting Time: {info['meeting_time']}
"""

    prompt = f"""
You are the official AI Assistant of Dumka Engineering College.

Answer ONLY using the information below.
If the answer is not available, politely say:
"Sorry, this information is currently not available."

{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content