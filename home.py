import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
    if user_input.lower() == "help":
        return "I can assist you with various aspects of sales, including generating cold call scripts, handling objections, closing deals, prospecting, lead generation, sales presentations, customer relationships, sales methodologies, sales training, team building, sales management, sales performance metrics, sales forecasting, negotiation tactics, sales technology, buyer behavior, persuasion techniques, sales ethics, email marketing, and more. Please provide a specific request or question for more detailed assistance."
    elif user_input.lower() == "sales":
        return "Sales are the lifeblood of any business. It involves the process of selling products or services to customers in exchange for money or other forms of compensation. Sales can be conducted through various channels, such as direct sales, online sales, retail sales, business-to-business (B2B) sales, and more. Effective sales strategies are essential for driving revenue, acquiring new customers, retaining existing customers, and growing the business. If you have any specific questions or need assistance with sales-related tasks, feel free to ask."
    elif user_input.lower() == "email marketing":
        return "Email marketing is a digital marketing strategy that involves sending commercial messages to a group of people via email. It is a cost-effective and efficient way to reach customers, promote products or services, drive traffic to websites, and build relationships with prospects and customers. Email marketing can include newsletters, promotional offers, product updates, event invitations, and more. To succeed in email marketing, it is essential to create engaging content, segment email lists, personalize messages, optimize deliverability, analyze performance metrics, and comply with email regulations. If you need help with email marketing strategies, tactics, or tools, feel free to ask."
    elif user_input.lower() == "cold calling":
        return "Cold calling is a sales technique that involves contacting potential customers who have not expressed interest in the products or services being offered. It is a proactive approach to sales prospecting and lead generation. Cold calling can be challenging but can also be an effective way to reach new customers, qualify leads, and generate sales opportunities. To succeed in cold calling, it is essential to have a well-crafted script, handle objections effectively, build rapport with prospects, and follow up consistently. If you need assistance with cold call scripts, objection handling, or cold calling strategies, feel free to ask."
    elif user_input.lower() == "sales training":
        return "Sales training is a critical component of developing a high-performing sales team. It involves equipping sales professionals with the knowledge, skills, and tools they need to succeed in their roles. Sales training can cover a wide range of topics, including product knowledge, sales techniques, objection handling, negotiation skills, closing strategies, customer relationship management, and more. Effective sales training can improve sales performance, boost team morale, and drive revenue growth. If you need help with sales training programs, coaching sessions, or training materials, feel free to ask."
    elif user_input.lower() == "sales management":
        return "Sales management is the process of leading and overseeing a sales team to achieve sales targets and business objectives. It involves setting sales goals, developing sales strategies, managing sales pipelines, coaching sales reps, monitoring performance metrics, and driving sales productivity. Effective sales management is essential for optimizing sales performance, motivating the sales team, and maximizing revenue generation. If you need assistance with sales management strategies, leadership tips, or team-building activities, feel free to ask."
    elif user_input.lower() == "sales performance metrics":
        return "Sales performance metrics are key performance indicators (KPIs) that help measure the effectiveness and efficiency of a sales team. These metrics provide valuable insights into sales activities, pipeline health, deal progress, revenue generation, and customer acquisition. Common sales performance metrics include conversion rates, win rates, average deal size, sales cycle length, customer acquisition cost, customer lifetime value, and more. Analyzing sales performance metrics can help identify strengths, weaknesses, and opportunities for improvement in the sales process. If you need help with tracking, analyzing, or interpreting sales performance metrics, feel free to ask."
    elif user_input.lower() == "sales forecasting":
        return "Sales forecasting is the process of predicting future sales performance based on historical data, market trends, and business projections. It involves estimating sales revenue, setting sales targets, and planning sales strategies to achieve business goals. Accurate sales forecasting is essential for resource allocation, budgeting, inventory management, and overall business planning. If you need assistance with sales forecasting techniques, pipeline management strategies, or revenue projections, feel free to ask."
    elif user_input.lower() == "negotiation tactics":
        return "Negotiation tactics are strategies and techniques used to reach mutually beneficial agreements in sales deals. Effective negotiation skills are essential for building rapport with customers, overcoming objections, and closing deals successfully. Common negotiation tactics include active listening, asking probing questions, identifying customer needs, presenting value propositions, and handling objections diplomatically. If you need help with negotiation tactics, deal-closing strategies, or objection-handling techniques, feel free to ask."
    elif user_input.lower() == "sales technology":
        return "Sales technology refers to the tools, software, and platforms that sales teams use to automate, streamline, and optimize sales processes. These technologies can include customer relationship management (CRM) systems, sales enablement tools, sales analytics software, email marketing platforms, and more. Sales technology can help sales professionals manage leads, track customer interactions, analyze sales data, and improve productivity. If you need recommendations for sales technology solutions, integration advice, or training on sales tools, feel free to ask."
    elif user_input.lower() == "buyer persona":
        return "A buyer persona is a semi-fictional representation of an ideal customer based on market research and real data about existing customers. Buyer personas help businesses understand their target audience, identify customer needs, and tailor marketing and sales strategies to specific customer segments. Creating detailed buyer personas can improve lead generation, customer engagement, and sales conversion rates. If you need help with developing buyer personas, segmenting target markets, or personalizing sales messages, feel free to ask."
    elif user_input.lower() == "sales ethics":
        return "Sales ethics are principles and standards that guide ethical behavior in sales interactions. Ethical sales practices involve honesty, transparency, integrity, and respect for customers' interests. Sales professionals should adhere to ethical standards to build trust with customers, maintain a positive reputation, and foster long-term relationships. If you need guidance on sales ethics, compliance with sales regulations, or ethical decision-making in sales, feel free to ask."
    elif user_input.lower() == "What can you help me with?":
        return "I can assist you with various aspects of sales, including generating cold call scripts, handling objections, closing deals, prospecting, lead generation, sales presentations, customer relationships, sales methodologies, sales training, team building, sales management, sales performance metrics, sales forecasting, negotiation tactics, sales technology, buyer behavior, persuasion techniques, sales ethics, email marketing, and more. Please provide a specific request or question for more detailed assistance."
    if user_input.lower() == "sales help":
        return "I can assist you with various aspects of sales, including generating cold call scripts, handling objections, closing deals, prospecting, lead generation, sales presentations, customer relationships, sales methodologies, sales training, team building, sales management, sales performance metrics, sales forecasting, negotiation tactics, sales technology, buyer behavior, persuasion techniques, sales ethics, email marketing, and more. Please provide a specific request or question for more detailed assistance."
    elif user_input.lower() == "email marketing help":
        return "I can help you with email marketing strategies, tactics, tools, and best practices. Email marketing is a powerful digital marketing channel that can help you reach customers, promote products, drive traffic, and build relationships. Whether you need assistance with email copywriting, email design, email automation, email deliverability, email analytics, or email compliance, feel free to ask."
    elif user_input.lower() == "cold calling help":
        return "I can assist you with cold calling strategies, scripts, objection handling, and best practices. Cold calling is a valuable sales technique for reaching new prospects, qualifying leads, and generating sales opportunities. Whether you need help with crafting cold call scripts, overcoming objections, building rapport with prospects, or following up effectively, feel free to ask." 
    elif user_input.lower() == "sales training help":
        return "I can help you with sales training programs, coaching sessions, training materials, and best practices. Sales training is essential for developing the skills, knowledge, and confidence of your sales team. Whether you need assistance with product training, sales techniques, objection handling, negotiation skills, or sales leadership, feel free to ask."
    elif user_input.lower() == "sales management help":
        return "I can assist you with sales management strategies, leadership tips, team-building activities, and performance management. Sales management is crucial for driving sales performance, motivating the sales team, and achieving business goals. Whether you need help with setting sales targets, managing pipelines, coaching sales reps, or analyzing sales data, feel free to ask."
    elif user_input.lower() == "sales performance metrics help":
        return "I can help you with tracking, analyzing, and interpreting sales performance metrics. Sales performance metrics provide valuable insights into the effectiveness and efficiency of your sales team. Whether you need assistance with measuring conversion rates, win rates, average deal size, sales cycle length, or customer acquisition cost, feel free to ask."
    #List the above options


    elif user_input.lower() == "sales forecasting help":
        return "I can assist you with sales forecasting techniques, pipeline management strategies, and revenue projections. Sales forecasting is essential for predicting future sales performance, setting sales targets, and planning sales strategies. Whether you need help with historical data analysis, market trend analysis, or sales projection models, feel free to ask."
    elif user_input.lower() == "negotiation tactics help":
        return "I can help you with negotiation tactics, deal-closing strategies, and objection-handling techniques. Effective negotiation skills are crucial for reaching mutually beneficial agreements and closing sales deals successfully. Whether you need assistance with active listening, asking probing questions, presenting value propositions, or handling objections, feel free to ask."
    elif user_input.lower() == "sales technology help":
        return "I can assist you with recommendations for sales technology solutions, integration advice, and training on sales tools. Sales technology can help you automate, streamline, and optimize your sales processes. Whether you need help with CRM systems, sales enablement tools, sales analytics software, or email marketing platforms, feel free to ask."
    elif user_input.lower() == "buyer persona help":
        return "I can help you with developing buyer personas, segmenting target markets, and personalizing sales messages. Buyer personas are essential for understanding your target audience, identifying customer needs, and tailoring your sales and marketing strategies. Whether you need assistance with market research, data analysis, or persona creation, feel free to ask."
    elif user_input.lower() == "sales ethics help":
        return "I can provide guidance on sales ethics, compliance with sales regulations, and ethical decision-making in sales. Ethical sales practices are crucial for building trust with customers, maintaining a positive reputation, and fostering long-term relationships. Whether you need assistance with honesty, transparency, integrity, or respect for customers' interests, feel free to ask."
    else:
        try:
            ai = GoogleGenerativeAI(model="text-bison", api_key=api_key)
            prompt = user_input
            response = ai.generate_text(prompt=prompt)
            return response.result
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Streamlit UI setup
st.set_page_config(page_title="AdviScript - AI Sales Coach", layout="wide")

st.markdown(
    """
    <style>
        .main {
            background-color: #F7F7F7;
            padding: 20px;
        }
        .title {
            font-size: 24px;
            font-weight: bold;
            color: #333333;
            text-align: center;
        }
        .input-area {
            margin-top: 20px;
            background-color: #FFFFFF;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .response-area {
            margin-top: 20px;
            background-color: #FFFFFF;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .input-box {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #DDDDDD;
            border-radius: 5px;
        }
        .response-box {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #DDDDDD;
            border-radius: 5px;
            background-color: #FAFAFA;
        }
        .submit-button {
            background-color: #50C878;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        .submit-button:hover {
            background-color: #45B267;
        }
        .chat-history {
            margin-top: 20px;
            background-color: #FFFFFF;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-height: 400px;
            overflow-y: auto;
        }
        .chat-item {
            margin-bottom: 10px;
            padding: 10px;
            background-color: #E0F7FA;
            border-radius: 5px;
        }
        .chat-title {
            font-size: 18px;
            font-weight: bold;
            color: #333333;
            cursor: pointer;
        }
        .chat-timestamp {
            font-size: 12px;
            color: #666666;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("AdviScript - AI Sales Coach")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input area
user_input = st.text_input("Ask the AI Sales Coach a question:", key="user_input")

# Process user input
if st.button("Submit"):
    if user_input:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        response = ai_sales_coach(user_input)
        st.session_state.chat_history.append({"timestamp": timestamp, "user_input": user_input, "response": response})

# Display chat history in the sidebar as clickable titles
with st.sidebar:
    st.markdown("## Chat History")
    for i, chat in enumerate(st.session_state.chat_history):
        if st.button(f"{chat['timestamp']} - {chat['user_input']}"):
            st.session_state.selected_chat_index = i

# Display the selected chat conversation
if "selected_chat_index" in st.session_state:
    selected_chat = st.session_state.chat_history[st.session_state.selected_chat_index]
    st.markdown(
        f"""
        <div class="response-area">
            <p class="response-box"><strong>You:</strong> {selected_chat['user_input']}</p>
            <p class="response-box"><strong>AdviScript:</strong> {selected_chat['response']}</p>
            <p class="chat-timestamp">{selected_chat['timestamp']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
```