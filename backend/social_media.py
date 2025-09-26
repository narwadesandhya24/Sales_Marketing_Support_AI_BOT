from backend.utils import client

class SocialMediaCreator:
    def __init__(self):
        pass  # using Hugging Face API now

    def generate_captions(self, prompt: str, n: int = 3):
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:nebius",
            messages=[
                {"role": "system", "content": "You are a creative social media marketer."},
                {"role": "user", "content": f"Generate {n} catchy social media captions for: {prompt}"}
            ],
        )
        return completion.choices[0].message.content.strip().split("\n")[:n]

    def generate_ideas(self, topic: str, n: int = 5):
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:nebius",
            messages=[
                {"role": "system", "content": "You are a creative marketing strategist."},
                {"role": "user", "content": f"List {n} creative social media content ideas for: {topic}"}
            ],
        )
        return completion.choices[0].message.content.strip().split("\n")[:n]
