import os
import streamlit as st
import google.generativeai as gen_ai

# Your Gemini-pro API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Streamlit Frontend configuration
st.set_page_config(
    page_title="Engage-AI",
    page_icon="🕸️", 
    layout="centered",
)

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "🤖"
    else:
        return "🧒"

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🚀 Engage-AI ")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
# Input field for user's message
user_prompt = st.chat_input("Ask Engage-AI...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
