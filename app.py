import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessor import preprocess_chat
from helper import get_message_count, most_common_words

st.title("WhatsApp Chat Analyzer")

uploaded_file = st.file_uploader("Upload your WhatsApp chat file", type=["txt"])

if uploaded_file:
    with open("uploaded_chat.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    df = preprocess_chat("uploaded_chat.txt")

    st.subheader("Message Count per User")
    user_counts = get_message_count(df)
    st.bar_chart(user_counts)

    st.subheader("Most Common Words")
    st.write(most_common_words(df))
