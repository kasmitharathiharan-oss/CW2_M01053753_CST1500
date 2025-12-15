import streamlit as st
from openai import OpenAI
client = OpenAI(api_key="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")

st.title("Chat with GPT-5.2")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Ask me anything!")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar = "🐇").markdown(prompt)

    completion = client.chat.completions.create(
        model="gpt-5.2",
        messages=st.session_state.messages
        )

    reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "user", "content": reply})
    st.chat_message("assistant").markdown(reply)




