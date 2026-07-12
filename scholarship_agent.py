from config import client, model_id


def scholarship_agent(query):

    context = """
Scholarship

Eligibility:
Income below 2.5 lakh

Apply:
Online Portal

Last Date:
15 September
"""

    prompt = f"""
Answer only from the following information.

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