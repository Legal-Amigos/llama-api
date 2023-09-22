import streamlit as st
import test

st.set_page_config(layout = "wide")

with st.sidebar:
    st.title("LegalEase: \nLegal Document Assistant")
    st.write("""
    Generative AI powered legal document creator or drafter. automatically generate a wide range of legal documents, including contracts, agreements, wills, deeds, and more. Users can input specific details, such as names, dates, and terms, and the AI system produces a customized document based on predefined templates and legal language.
    """)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Send a message"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    reply = test.query_engine.query(prompt)

    response = reply
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})