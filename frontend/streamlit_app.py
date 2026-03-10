import streamlit as st
from app.main import process_user_input
from app.modules.guided_journal import get_prompt
from app.modules.thought_reframe import reframe_thought
from app.modules.mindful_moments import get_mindfulness_exercise

st.title("🧠 SentiCare Mental Wellness Assistant")

user_input = st.text_area("Share what's on your mind")

if st.button("Send"):

    result = process_user_input(user_input)

    st.write("Sentiment:", result["sentiment"])

    st.write("Response:", result["response"])


st.subheader("Guided Journal")

if st.button("Get Journal Prompt"):

    st.write(get_prompt())


st.subheader("Thought Reframing")

thought = st.text_input("Enter a negative thought")

if st.button("Reframe Thought"):

    st.write(reframe_thought(thought))


st.subheader("Mindful Moment")

if st.button("Start Exercise"):

    st.write(get_mindfulness_exercise())
