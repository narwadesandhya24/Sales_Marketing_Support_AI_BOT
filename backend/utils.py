import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")  # this should now be set
)
