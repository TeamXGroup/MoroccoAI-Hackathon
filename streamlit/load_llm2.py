import torch
from llama_cpp import Llama

class LLMGeneration:
    def __init__(self, model_path: str ="AliGuinga/recyclingllm-01-Q8_0-GGUF"):
        """
        Initialize the model and tokenizer.
        :param model_path: The path to the saved model directory.
        """
        self.model = Llama.from_pretrained(
                    repo_id="AliGuinga/recyclingllm-01-Q8_0-GGUF",  # Replace with your model's repo name
                    filename="recyclingllm-01-q8_0.gguf")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

def generate_response(self, prompt: str, max_tokens: int = 500, temperature: float = 0.7):
    """
    Generate a response from the model given an input prompt.
    
    :param prompt: The input text prompt for the model.
    :param max_tokens: The maximum length of the generated text.
    :param temperature: Sampling temperature; lower values make the model more deterministic.
    :return: The generated response as a string.
    """
    if self.model is None:
        raise ValueError("Model is not loaded. Please check the model path or loading process.")
    
    response = self.model.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,  # Limit the number of tokens generated
        temperature=temperature  # Control randomness in responses
    )
    
    # Assuming the response object has a 'choices' field with the generated content
    return response['choices'][0]['message']['content']