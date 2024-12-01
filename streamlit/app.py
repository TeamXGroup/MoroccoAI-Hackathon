import streamlit as st
import numpy as np
from load_llm2 import LLMGeneration
import pandas as pd
#from load_gen_img import ImageGenerator
from huggingface_hub import login
import pandas as pd
import time

# Create mock FAQ data
faq_data = pd.DataFrame({
    'question': [
        "What is Streamlit?",
        "How do I install Streamlit?",
        "Can I use Streamlit with machine learning?",
        "How do I create a simple app in Streamlit?",
        "How do I deploy a Streamlit app?",
        "Can I use custom CSS in Streamlit?",
        "How do I add interactivity to my Streamlit app?",
        "Can Streamlit handle large datasets?",
        "Can Streamlit handle large datasets?",
        "Can Streamlit handle large datasets?",
        "How do I update Streamlit?",
        "Is Streamlit free to use?"
    ],
    'materials': [
        "Python, Streamlit library",
        "Python, pip",
        "Streamlit, Python libraries, ML model",
        "Streamlit, Python, basic knowledge",
        "Heroku, AWS, Docker",
        "CSS, Streamlit themes",
        "Streamlit widgets, Python",
        "Streamlit, pandas, NumPy",
        "Streamlit, pandas, NumPy",
        "Streamlit, pandas, NumPy",
        "pip, terminal access",
        "Streamlit website"
    ],
    'steps': [
        "1. Install Streamlit using pip. 2. Write Python code for the app. 3. Run `streamlit run`.",
        "1. Open terminal. 2. Run `pip install streamlit`.",
        "1. Write a machine learning model. 2. Display it using Streamlit's widgets.",
        "1. Create a new Python file. 2. Import Streamlit. 3. Add widgets and elements.",
        "1. Choose a deployment platform. 2. Set up your app on the platform. 3. Deploy the app.",
        "1. Create a custom CSS file. 2. Use `st.markdown` with `unsafe_allow_html=True`.",
        "1. Use widgets like sliders, buttons, and text inputs. 2. Connect them to your code.",
        "1. Use pandas or NumPy for data handling. 2. Streamlit will handle display automatically.",
        "1. Use pandas or NumPy for data handling. 2. Streamlit will handle display automatically.",
        "1. Use pandas or NumPy for data handling. 2. Streamlit will handle display automatically.",
        "1. Run `pip install --upgrade streamlit`. 2. Restart your Streamlit app.",
        "Yes, Streamlit is open-source and free to use."
    ]
})
def simulate_typing_effect(response):
    typed_response = ""
    # Create a placeholder to update text
    text_placeholder = st.empty()

    # Typing effect: add one character at a time
    for char in response:
        #if stop_flag():  # Check if the stop button was pressed
            #break'''
        typed_response += char
        text_placeholder.text(typed_response)  # Update the placeholder with the new text
        time.sleep(0.05)  # Adjust to control typing speed

llm = LLMGeneration()

icon =  r"C:\Users\warag\Downloads\november_projet\morocco_ai_hackaton_2024\MoroccoAI-Hackathon\LO2.png"
st.set_page_config(page_title="chicillo" , page_icon=icon,layout='wide')
# Initialize session state to keep track of the conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Title and description
st.title("♻️ Chicillo - Your Eco-Friendly Assistant 🌍")
st.write("intro")

# CSS styling for chat bubbles and input field
st.markdown("""
    <style>
        /* Set the background color of the whole page */
        body {
            background-color: #00FF00;  /* Pure green */
        }
    .stTextInput>div>div>input {
        background-color: #f1f1f1;
        border: none;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #56b6c2;
        outline: none;
    }
    .stWrite>div>div>p {
        padding: 10px;
        background-color: #e5e5e5;
        border-radius: 10px;
        font-size: 16px;
        width: fit-content;
    }
    .stWrite>div>div>p:nth-child(odd) {
        background-color: #d1f5f0; /* Bot message */
    }
    .stWrite>div>div>p:nth-child(even) {
        background-color: #f5d1d1; /* User message */
    }
                <style>
    /* Resize the Streamlit sidebar icon */
    .css-1v3fvcr {
        font-size: 1px; /* Adjust size here */
    }
    /* Resize the sidebar header */
    .css-15tx938 {
        font-size: 20px; /* Adjust size here */
    }
    /* Optional: Change the size of other sidebar components */
    .css-1n76uvv {
        font-size: 18px; /* Adjust size of text in sidebar */
    }
    .css-1d391kg {
            background-color: #00f000;  /* Lighter background for sidebar */
    }
    </style>
""", unsafe_allow_html=True)
icon_bar = st.sidebar.image(icon)
menu = st.sidebar.selectbox("Choose an option", ["Start Chat", "FAQ"])

# Main content based on the selected menu
with st.container():
    if menu == "Start Chat":
        st.write("Hello! I’m Chicillo, your personal assistant to help you recycle and make sustainable choices. How can I assist you today?")

        # Input area for user query
        user_input = st.text_input("Type your message:")

    # Output area for chatbot response
    if user_input:
        st.write('You asked:', user_input)
        
        # Create a placeholder for the stop button (so it's checked during typing)
        stop_placeholder = st.empty()

        with st.spinner("Thinking..."):
            # Generate response from the model
            response = llm.generate_response(prompt=str(user_input), max_tokens=256)

            # Define a button that can stop the generation
            stop = stop_placeholder.button("Stop Generation")

            # This lambda will return True if the button is pressed
            #stop_flag = lambda: stop_placeholder.button("Stop Generation")

            # Simulate typing effect with the ability to stop
            simulate_typing_effect(response)


        st.success("Done!")

with st.container():
    if menu == "FAQ":
        st.write("Here are some common questions you can ask!")

        # Display first 10 questions
        num_to_display = 10
        for index, row in faq_data.head(num_to_display).iterrows():
            with st.expander(row['question']):
                # Display question, materials, and steps inside one string with titles
                faq_content = f"**Materials**: {row['materials']}  \n**Steps**: {row['steps']}"
                st.write(faq_content)

        # Button to expand to show the remaining questions
        if st.button("Show All FAQ"):
            for index, row in faq_data.tail(len(faq_data) - num_to_display).iterrows():
                with st.expander(row['question']):
                    # Display question, materials, and steps inside one string with titles
                    faq_content = f"**Materials**: {row['materials']}  \n**Steps**: {row['steps']}"
                    st.write(faq_content)