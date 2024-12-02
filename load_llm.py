from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login


class LLMGeneration:
    def __init__(self, model_path: str ="meta-llama/Llama-3.2-1B"):
        """
        Initialize the model and tokenizer.
        :param model_path: The path to the saved model directory.
        """

        self.token = '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'
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path,use_auth_token=self.token, device_map="auto", torch_dtype="auto")
        self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
        #self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #self.model.to(self.device)
        self.pipe = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer, max_new_tokens=400, temperature=0.3, top_p=0.9)


    def generate_response(self, prompt: str, max_length: int = 1024, do_sample: bool = True, top_k: int = 50, top_p: float = 0.95):
        """
        Generate a response from the model given an input prompt.
        :param prompt: The input text prompt for the model.
        :param max_length: The maximum length of the generated text.
        :param do_sample: Whether or not to sample the next token.
        :param top_k: The number of highest probability vocabulary tokens to keep for top-k filtering.
        :param top_p: The cumulative probability of parameter highest probability tokens to keep for nucleus sampling.
        :return: The generated response as a string.
        """
        input_ids = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **input_ids, 
            max_length=max_length, 
            do_sample=do_sample, 
            top_k=top_k, 
            top_p=top_p,
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

