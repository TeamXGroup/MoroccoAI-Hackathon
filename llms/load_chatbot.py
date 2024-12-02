from chat_with_multiple_llms import LLMChatbot



# 1. Create the chatbot object
chatbot = LLMChatbot(json_file="llms_list.json")

# 2. Load the model by name
chatbot.load_model(name="GPT-J")  # Load the model with the name "GPT-J"

# 3. Chat with the model
response = chatbot.chat("Hello, how are you today?")
print(response)
