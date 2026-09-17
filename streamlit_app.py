import streamlit as st
from groq import Groq

st.set_page_config(page_title="SHAJIB AI", page_icon="🤖")
st.title("🤖 SHAJIB AI")
st.caption("Created by Shajib Akash Sunny")

groq_key = st.text_input("Groq API Key", type="password")

if not groq_key:
    st.info("উপরে তোমার Groq API Key দাও ভাই")
    st.stop()

client = Groq(api_key=groq_key.strip())

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

if prompt := st.chat_input("তোমার প্রশ্ন লেখো..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages
        )
        ans = res.choices[0].message.content
    except Exception as e:
        ans = f"Error: {e}"
    st.session_state.messages.append({"role": "assistant", "content": ans})
    st.chat_message("assistant").write(ans)
