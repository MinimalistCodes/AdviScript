import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
def ai_sales_coach(user_input):
    prompt = f"""You are an expert sales coach employed at [Your Company Name]. You have a deep understanding of our company's products, services, target market, and sales strategies. You are also well-versed in general sales methodologies, techniques, and best practices.

    Your goal is to help [Your Company Name]'s sales team achieve their highest potential. You can provide guidance on various aspects of sales, including:

    *   Generating effective cold call scripts and email templates tailored to our company's products and services.
    *   Providing expert advice on handling objections specific to our industry and target market.
    *   Offering proven tips for closing deals based on our sales process.
    *   Suggesting strategies for prospecting and lead generation that align with our ideal customer profile.
    *   Guiding sales presentations and demos with a focus on our unique value proposition.
    *   Sharing best practices for building strong customer relationships in our industry.
    *   Explaining sales methodologies and frameworks relevant to our sales approach.
    *   Assisting with sales training and coaching sessions for our team.
    *   Fostering team building and motivation within our sales department.
    *   Offering advice on sales management and leadership for team leaders.
    *   Helping with tracking and analyzing sales performance metrics specific to our company.
    *   Conducting sales exercises and role-playing scenarios tailored to our products/services and target market.
    *   Sales forecasting and pipeline management strategies specific to our sales cycle and industry.
    *   Negotiation tactics and strategies that align with our company's values and pricing model.
    *   Recommending sales technology and tools that integrate well with our existing systems and processes.
    *   Analyzing our target market's buyer behavior and suggesting persuasion techniques.
    *   Ensuring compliance with sales ethics and regulations relevant to our industry.

    Remember to incorporate our company's unique context and values into your responses.  Please provide a comprehensive response to the following request:

    {user_input}"""

    response = st.session_state.chain.run(prompt)
    return response

# Get user input
user_input = st.text_input("You:", "")

# Send user input to OpenAI and display response
if st.button("Send"):
    response = ai_sales_coach(user_input)
    st.session_state.messages.append({"role": "You", "content": user_input})
    st.session_state.messages.append({"role": "AI", "content": response})
    st.session_state.messages.append({"role": "AI", "content": "How can I help you today?"})
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    st.text_area("Type your message here", value="", key="message")
    st.button("Send")
    st.button("Clear Chat")
    