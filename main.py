from intent_agent import classify_intent

from admission_agent import admission_agent
from exam_agent import exam_agent
from fees_agent import fees_agent
from scholarship_agent import scholarship_agent

from response_agent import response_agent

query = input("Ask: ")

intent = classify_intent(query)

print("Intent:", intent)

if "admission" in intent:
    ans = admission_agent(query)

elif "exam" in intent:
    ans = exam_agent(query)

elif "fees" in intent:
    ans = fees_agent(query)

elif "scholarship" in intent:
    ans = scholarship_agent(query)

else:
    ans = "Sorry, I don't understand."

print(response_agent(ans))