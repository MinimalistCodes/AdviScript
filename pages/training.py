import streamlit as st

def app():
    st.title("Interactive Sales Training")

    # Quiz Data (Replace with your own content)
    quiz_questions = [
        {
            "question": "What is the most important step in the sales process?",
            "options": ["Closing the deal", "Building rapport", "Qualifying the lead", "Presenting the product"],
            "answer": "Qualifying the lead"
        },
        {
            "question": "Which of the following is NOT a common sales objection?",
            "options": ["Price", "Need", "Time", "Weather"],
            "answer": "Weather"
        },
        # Add more questions here...
    ]

    # Quiz Logic
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0

    current_question = quiz_questions[st.session_state.current_question]

    st.subheader(f"Question {st.session_state.current_question + 1}")
    st.write(current_question["question"])

    user_answer = st.radio("Select your answer:", current_question["options"])

    if st.button("Submit Answer"):
        if user_answer == current_question["answer"]:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer was: {current_question['answer']}")

        st.session_state.current_question += 1

        if st.session_state.current_question >= len(quiz_questions):
            st.subheader("Quiz Completed!")
            st.write(f"Your final score is: {st.session_state.score}/{len(quiz_questions)}")
            # Reset quiz state
            del st.session_state.current_question
            del st.session_state.score
        else:
            st.experimental_rerun()  # Move to the next question
