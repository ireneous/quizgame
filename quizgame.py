import streamlit as st
import json
import random

# Load questions from JSON file
with open("questions.json") as f:
    questions = json.load(f)

# Shuffle questions
random.shuffle(questions)

st.title("Quiz App")
st.write("Answer all questions below, then click Submit to see your score.")

# Track answers
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Display questions without preselecting
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    st.session_state.answers[i] = st.radio(
        "Choose an answer:",
        options=q["options"],
        index=None,  # No preselection
        key=f"q{i}"
    )

# Submit button
if st.button("Submit Quiz"):
    score = 0
    st.write("---")
    st.subheader("Results")
    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i)
        correct_ans = q["answer"]
        if user_ans is None:
            st.warning(f"Q{i+1}: No answer selected.")
        elif user_ans == correct_ans:
            st.success(f"Q{i+1}: Correct ✅")
            score += 1
        else:
            st.error(f"Q{i+1}: Wrong ❌ (Correct: {correct_ans})")

    st.write(f"**Your final score: {score} / {len(questions)}**")
