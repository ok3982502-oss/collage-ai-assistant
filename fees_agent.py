from config import client, model_id


def fees_agent(query):

    context = """
Semester Fees: ₹45000

Hostel Fees: ₹20000

Payment Methods:
- Online
- Offline
- UPI
"""

    prompt = f"""
Use only the following information.

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

