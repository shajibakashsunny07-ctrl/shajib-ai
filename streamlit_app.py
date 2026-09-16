import streamlit as st
st.set_page_config(page_title="SHAJIB AI", page_icon="🤖")
st.title("🤖 SHAJIB AI")
st.caption("Created by Shajib Akash Sunny")
if "messages" not in st.session_state:
    st.session_state.messages = []
for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])
if prompt := st.chat_input("তোমার প্রশ্ন লেখো..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    reply = f"তুমি বললে: {prompt} - আমি LIVE! 🚀"
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
