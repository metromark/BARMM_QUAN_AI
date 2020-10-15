import streamlit as st
import wikipedia
from ktrain import text
import os
import shutil

# Search wikipedia for topics
st.title('BARMM QUAN.AI')
st.write('A Question-Answering AI')

@st.cache(allow_output_mutation=True)
def QAModel():
    INDEXDIR = os.path.join(os.getcwd(), 'index')
    model = text.SimpleQA(INDEXDIR)
    return model

# Insert question
st.subheader("Ask Me Anything About BARMM!")
question_text = st.text_area("State your question...", "What is BARMM?")

qa = QAModel()
try:
    answers = qa.ask(question_text, batch_size=20)
    short_answer = answers[0]['answer']
    full_answer = answers[0]['full_answer']
    context = answers[0]['context']
    confidence = answers[0]['confidence']
    reference = answers[0]['reference']
    
    if confidence >= 0.0125: # 1 over batch size
        st.write(f"With **{int(confidence*100)}** percent confidence, the answer is: ")
        
        st.subheader("Short Answer")
        st.write(short_answer.capitalize())
        
        st.subheader("Full Answer")
        st.write(full_answer.capitalize())
        
        st.subheader("Reference Document/Link")
        st.write(reference)
        
    else:
        st.write("Couldn't find an answer for that. Maybe try another question or feed me more information.")
except:
    st.write("Couldn't find an answer for that. Try another question about BARMM.")
    