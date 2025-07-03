import requests
import os
from PIL import Image
from io import BytesIO

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def generate_logo(idea):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": f"{idea} logo, minimal, vector, white background",
        "options": {"wait_for_model": True}
    }
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    response = requests.post(url, headers=headers, json=payload)
    return Image.open(BytesIO(response.content))
