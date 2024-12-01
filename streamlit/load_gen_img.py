import torch
from diffusers import StableDiffusionPipeline

import time

class ImageGenerator:
    def __init__(self, model_name="CompVis/stable-diffusion-v1-4"):
        # Login once
        

        # Load the pre-trained Stable Diffusion model
        self.pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")

    def generate_image(self, prompt):
        """
        Generates an image based on the input text prompt using Stable Diffusion.
        """
        '''time.sleep(3)'''
        image = self.pipe(prompt).images[0]
        return image