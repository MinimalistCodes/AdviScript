import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF

# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(
    page_title="SalesTrek - AI Sales Script Generator",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def save_chat_to_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for message in chat_history:
        role = "User" if message["role"] == "user" else "Assistant"
        content = message["content"]
        pdf.multi_cell(0, 10, f"{role}: {content}")
        pdf.ln(10)

    pdf_file = "chat_history.pdf"
    pdf.output(pdf_file)
    return pdf_file

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
    else:
      prompt = f"""
      You are an expert salesperson, manager, and copywriter. You can help with various aspects of the subject given, including:

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
      *   Crafting engaging subject lines
      *   Writing compelling email copy
      *   Personalizing emails for different audiences
      *   A/B testing email campaigns
      *   Optimizing email deliverability
      *   Analyzing email performance metrics
      *   Building email lists and segments
      *   Creating automated email sequences
      *   Integrating email marketing tools
      *   Compliance with email regulations (e.g., CAN-SPAM, GDPR)
      *   Email design best practices
      *   Email marketing strategy and planning
      *   Email copywriting tips and techniques
      *   Email marketing automation
      *   Email personalization and segmentation
      *   Email campaign optimization
      *   Email marketing analytics and reporting
      *   Email marketing trends and innovations
      *   Email marketing case studies and examples
      *   Email marketing tools and software
      *   Generating cold call scripts
      *   Crafting effective email templates
      *   Providing advice on handling objections
      *   Offering tips for closing deals
      *   Suggesting strategies for prospecting and lead generation
      *   Guiding sales presentations and demos
      *   Sharing best practices for building customer relationships
      *   Explaining sales methodologies and frameworks
      *   Assisting with sales training and coaching
      *   Team building and motivation
      *   Sales management and leadership
      *   Tracking and analyzing sales performance
      *   Sales exercises and role-playing scenarios
      *   Sales forecasting and pipeline management
      *   Sales negotiation tactics and strategies
      *   Recommendations for sales technology and tools
      *   Sales psychology, buyer behavior, and persuasion techniques
      *   Sales ethics and compliance
      *   Emotional intelligence in sales

      Please provide a comprehensive response to the following request:

      {user_input}
      """
      llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
      return llm.invoke(prompt)

#load styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with st.sidebar:
    st.title("SalesTrek AI Sales Coach")
    # clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
    st.markdown("---")  # Horizontal line
    #save to pdf button
    if st.button("Save Chat to PDF"):
        #use FPDF to save chat to pdf
        pdf_file = save_chat_to_pdf(st.session_state.messages)
        st.success(f"Chat history saved to {pdf_file}")
    st.markdown("---")  # Horizontal line
    # Chatbot settings
    st.markdown("### Chatbot Settings")
    st.markdown("Customize the chatbot settings.")
    # Chatbot settings form
    chatbot_settings = st.form("chatbot_settings")
    with chatbot_settings:
        # Chatbot settings form fields
        st.markdown("#### Chatbot Settings")
        st.info("Have a different API key? Enter it below.(Google Gemerative AI API Key)")
        # Chatbot settings form fields
        api_key = st.text_input("API Key", value=api_key)
        # Save button
        submit_button = st.form_submit_button("Save")
    # Save chatbot settings
    if submit_button:
        os.environ["GOOGLE_API_KEY"] = api_key
        st.success("Chatbot settings saved successfully.")


# UI Title
st.markdown("## SalesTrek - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("---")  # Horizontal line
    
    
# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # Welcome message
    st.session_state.messages.append({"role": "assistant", "content": "Welcome! Type 'help' to get started!"})


# Display chat messages
with st.container():  # Use container for styling
    for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
# User Input
if prompt := st.chat_input("Your message"):
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display "Sales Coach is typing..."
    with st.chat_message("assistant"):
        message_placeholder = st.empty() 
        message_placeholder.markdown("Sales Coach is typing...")

    # Get and append AI response (with a delay to simulate typing)
    time.sleep(1)  # Adjust the delay as needed
    response = ai_sales_coach(prompt)
    message_placeholder.markdown(response)  # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear user input after sending message
    st.session_state.messages = st.session_state.messages[-100:]  # Limit chat history to last 100 messages
    
    
  
