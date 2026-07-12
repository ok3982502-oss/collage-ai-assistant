from config import client, model_id

def classify_intent(query):

    q = query.lower()

    # Fast keyword matching
    if any(word in q for word in ["hod", "department", "principal", "library", "hostel",
                                  "placement", "cse", "computer", "civil",
                                  "electrical", "mechanical", "academic"]):
        return "department"

    elif "admission" in q:
        return "admission"

    elif any(word in q for word in ["exam", "examination"]):
        return "exam"

    elif "fees" in q:
        return "fees"

    elif "scholarship" in q:
        return "scholarship"

    # Fallback to AI
    prompt = f"""
You are an Intent Classifier.

Possible intents:
admission
exam
fees
scholarship
department

Return ONLY one word.

Question:
{query}
"""

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip().lower()