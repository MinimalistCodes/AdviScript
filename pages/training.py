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
        {
            "question": "What is the best way to handle a sales objection?",
            "options": ["Ignore it", "Agree with the customer", "Overcome it", "Argue with the customer"],
            "answer": "Overcome it"
        },
        {
            "question": "What is the purpose of a sales pitch?",
            "options": ["To close the deal", "To build rapport", "To present the product", "To qualify the lead"],
            "answer": "To present the product"
        },
        {
            "question": "What is the best way to follow up with a customer after a sale?",
            "options": ["Send a thank you note", "Call them every day", "Ask for a referral", "Forget about them"],
            "answer": "Send a thank you note"
        },
    ]
    
    # Quiz Logic
    score = 0
    for i, question in enumerate(quiz_questions):
        st.subheader(f"Question {i + 1}")
        st.write(question["question"])
        answer = st.radio("Select an answer:", question["options"])
        if answer == question["answer"]:
            st.write("Correct!")
            score += 1
        else:
            st.write("Incorrect.")
        st.write("")
        
    st.subheader("Quiz Results")
    st.write(f"You scored {score} out of {len(quiz_questions)}.")
    if score == len(quiz_questions):
        st.write("Congratulations! You passed the quiz.")
    else:
        st.write("Better luck next time.")
        
    st.write("")
    st.write("Would you like to retake the quiz?")
    retake_quiz = st.button("Retake Quiz")
    if retake_quiz:
        app()
        
if __name__ == "__main__":
    app()