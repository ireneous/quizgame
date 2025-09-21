import streamlit as st
import json
import random

# Load questions from JSON file
with open("questions.json") as f:
    questions = json.load(f)

# Shuffle questions
random.shuffle(questions)

st.title("Quiz App")
st.write("Answer the questions below and submit at the end to see your score.")

# Track user's answers
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Display questions
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio(
        "Choose an answer:",
        options=[""] + q["options"],  # add blank option
        key=f"q_{i}"
    )
    if selected != "":
        st.session_state.answers[i] = selected

# Submit button
if st.button("Submit Quiz"):
    score = 0
    st.write("---")
    st.subheader("Results")

    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i, "")
        correct_ans = q["answer"]
        if user_ans == correct_ans:
            st.success(f"Q{i+1}: Correct! ✅")
            score += 1
        elif user_ans == "":
            st.warning(f"Q{i+1}: No answer selected ⚠️. Correct answer: {correct_ans}")
        else:
            st.error(f"Q{i+1}: Wrong ❌. Correct answer: {correct_ans}")

    st.write(f"**Your final score: {score} / {len(questions)}**")
    st.session_state.answers = {}  # Reset for next quiz
