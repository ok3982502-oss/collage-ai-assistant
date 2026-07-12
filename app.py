import streamlit as st
import base64

from intent_agent import classify_intent
from admission_agent import admission_agent
from exam_agent import exam_agent
from fees_agent import fees_agent
from scholarship_agent import scholarship_agent
from department_agent import department_agent

st.set_page_config(
    page_title="DUMKA Engineering College Assistant AI",
    page_icon="✡️",
    layout="wide"
)

# ---------- Background Image ----------
def get_base64(file):
    with open(file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

img = get_base64("background.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        <h1 style="color:black; text-align:center;">DUMKA ENGINNERING COLLEGE ASSISTANT AI</h1>
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------
with st.sidebar:
    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        st.session_state.messages = []

    st.markdown("---")
    st.write("🏫 DUMKA Engineering College")
    st.write("🤖 AI Assistant")
    st.write(" CREATED BY ONKAR KUMAR ")

# ---------- Main Page ----------
st.title("✡️ DUMKA Engineering College Assistant AI")
st.caption("CREATED BY ONKAR KUMAR--2025-2028")

# ---------- Display Previous Messages ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Chat Input ----------
query = st.chat_input("Ask anything about college...")

if query:

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    intent = classify_intent(query)
    

    if "admission" in intent:
        answer = admission_agent(query)

    elif "exam" in intent:
        answer = exam_agent(query)

    elif "fees" in intent:
        answer = fees_agent(query)

    elif "scholarship" in intent:
        answer = scholarship_agent(query)
    elif "department" in intent:
        answer = department_agent(query)

    else:
        answer = "Sorry, I don't understand."

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )