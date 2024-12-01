import streamlit as st
import numpy as np
from load_llm import LLMGeneration

from load_gen_img import ImageGenerator
from huggingface_hub import login
#import threading
#import time

# Title of the app
st.title("chicuio")

# Input widgets
login('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')

input_ = st.text_input("what's your question?")
# Create an instance of the ImageGenerator class 
generator = ImageGenerator() 
gen_text = LLMGeneration()

if input:
    st.write(generator.generate_image(input))  
    st.write(gen_text.generate_response(input))
    st.write(f"Type of input: {type(input_)}")
    st.write(f"Your input is: {input_}")
