import streamlit as st
from groq import Groq

st.set_page_config(page_title="SHAJIB AI", page_icon="🤖")
st.title("🤖 SHAJIB AI")
st.caption("Created by Shajib Akash Sunny")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

if prompt := st.chat_input("তোমার প্রশ্ন লেখো..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are SHAJIB AI, created by Shajib Akash Sunny. Reply in Bangla mixed English, friendly."}] + st.session_state.messages
    )
    reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
