from config import client, model_id


def exam_agent(query):

    context = """
Exam Information

Exam Starts:
10 August

Admit Card:
7 days before exam

Result:
30 days after exam
"""

    prompt = f"""
Use only the following data.

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