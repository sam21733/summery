#pip install streamlit transformers torch
pip install transformers
pip install torch
pip install tensorflow
#from transformers import pipeline
import streamlit as st
from transformers import pipeline

# Title and description
st.title("Text Summarization App")
st.write("Summarize long texts into concise summaries using a state-of-the-art NLP model.")

# Input text box
input_text = st.text_area("Enter the text you want to summarize", height=200)

# Summarizer model from Hugging Face
summarizer = pipeline("summarization")

# Button to perform summarization
if st.button("Summarize"):
    if input_text.strip() != "":
        # Summarize the input text
        summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)

        # Display the summary
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
