import streamlit as st
from datetime import date

def app():
    st.header("Sales Activity Tracker")

    # Initialize activity list in session state if not present
    if "activities" not in st.session_state:
        st.session_state.activities = []

    with st.form("activity_form"):
        activity_date = st.date_input("Date", value=date.today())
        activity_type = st.selectbox("Activity Type", ["Call", "Email", "Meeting", "Demo"])
        contact_name = st.text_input("Contact Name (Optional):")
        company_name = st.text_input("Company Name (Optional):")
        outcome = st.selectbox("Outcome", ["Positive", "Negative", "Neutral"])
        notes = st.text_area("Notes (Optional):")
        submit_button = st.form_submit_button("Log Activity")

        if submit_button:
            new_activity = {
                "date": activity_date.strftime("%Y-%m-%d"),
                "type": activity_type,
                "contact": contact_name,
                "company": company_name,
                "outcome": outcome,
                "notes": notes,
            }
            st.session_state.activities.append(new_activity)
            st.success("Activity Logged!")

    # Display Logged Activities
    st.subheader("Logged Activities")
    if st.session_state.activities:
        for activity in st.session_state.activities:
            st.write(f"""
            **Date:** {activity['date']} | **Type:** {activity['type']} | **Outcome:** {activity['outcome']}
            {f"**Contact:** {activity['contact']}" if activity['contact'] else ""}
            {f"**Company:** {activity['company']}" if activity['company'] else ""}
            {f"**Notes:** {activity['notes']}" if activity['notes'] else ""}
            ---
            """)  # Add a horizontal rule for separation
    else:
        st.write("No activities logged yet.")

# Run the app
if __name__ == "__main__":
    app()
