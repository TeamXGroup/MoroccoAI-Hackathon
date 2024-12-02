import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMChatbot:
    """
    A chatbot class to interact with different LLMs (Language Learning Models).
    
    Usage:
    - Use a JSON file containing the models' names and links to import the model of your choice.
    - You can select a model either by its index or by its name in the list.
    
    Requirements:
    - transformers library
    - torch library
    """
    
    def __init__(self, json_file):
        """
        Initializes the LLMChatbot class with the path to the JSON file containing model names and links.
        :param json_file: The path to the JSON file that holds the models' names and Hugging Face links.
        """
        self.json_file = json_file
        self.models = self.load_models_from_json()
        self.model = None
        self.tokenizer = None

    def load_models_from_json(self):
        """
        Loads the models from the provided JSON file.
        :return: List of models with names and links.
        """
        with open(self.json_file, 'r') as f:
            return json.load(f)
    
    def load_model(self, name=None):
        """
        Loads the model based on its name.
        :param name: The name of the model (case insensitive).
        """
        if name is None:
            raise ValueError("Model name must be provided.")
        
        model_info = next((m for m in self.models if m['name'].lower() == name.lower()), None)
        if model_info is None:
            raise ValueError(f"Model with name '{name}' not found.")
        
        model_name = model_info['link']
        print(f"Loading model: {model_name}")
        
        # Load the model and tokenizer
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def chat(self, prompt, max_length=100):
        """
        Interact with the loaded model using a prompt.
        :param prompt: The text prompt to send to the model.
        :param max_length: The maximum length of the response.
        :return: The generated response from the model.
        """
        if self.model is None or self.tokenizer is None:
            raise ValueError("Model and tokenizer must be loaded before chatting.")
        
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return response


