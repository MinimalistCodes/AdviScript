import gradio as gr
from transformers import pipeline, set_seed

# Initialize the Hugging Face pipeline
model_name = "gpt2-medium"  # Replace with a suitable model if needed
pipe = pipeline("text-generation", model=model_name)
set_seed(42)

# Initialize conversation history
conversation_history = []

# Function to generate sales script
def generate_script(prompt):
    response = pipe(prompt, max_length=200, num_return_sequences=1)
    return response[0]["generated_text"]

# Define the Gradio interface
def chat_interface(user_input):
    global conversation_history
    conversation_history.append(f"User: {user_input}")
    
    # Define a sequence of questions
    questions = [
        "What product or service are you selling?",
        "Who is your target audience?",
        "What are the main benefits of your product or service?",
        "What objections might the customer have?",
        "How would you like to close the call?"
    ]
    
    # Determine the next question
    if len(conversation_history) == 1:
        next_question = questions[0]
    elif len(conversation_history) == 3:
        next_question = questions[1]
    elif len(conversation_history) == 5:
        next_question = questions[2]
    elif len(conversation_history) == 7:
        next_question = questions[3]
    elif len(conversation_history) == 9:
        next_question = questions[4]
    else:
        # Generate the script after the last question
        prompt = " ".join(conversation_history)
        script = generate_script(prompt)
        conversation_history = []  # Reset conversation history
        return f"AI Sales Coach: {script}"

    conversation_history.append(f"AI Sales Coach: {next_question}")
    return next_question

# Create the Gradio app
app = gr.Interface(
    fn=chat_interface,
    inputs=gr.inputs.Textbox(label="Your Response"),
    outputs=gr.outputs.Textbox(label="AI Sales Coach"),
    title="AI Sales Coach Chatbot",
    description="Generate sales call scripts using AI. Answer the questions to get started.",
    theme="compact",
    layout="vertical"
)

# Run the Gradio app
if __name__ == "__main__":
    app.launch()
