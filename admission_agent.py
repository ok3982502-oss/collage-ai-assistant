from config import client, model_id
from knowledge_agent import get_department_info


def admission_agent(query):

    # Admission data from JSON
    info = get_department_info("Admission")

    context = f"""
College Admission Information

Admission Last Date: 30 July

Eligibility:
Minimum 60%

Documents:
- 10th Marksheet
- 12th Marksheet
- Aadhar Card
- Passport Photo
- Transfer Certificate

Admission In-charge: {info['head']}
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