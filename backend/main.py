from fastapi import FastAPI
from pydantic import BaseModel
from .recommender import Recommender
from .support_bot import SupportBot
from .social_media import SocialMediaCreator

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sales, Marketing & Support API is running", "endpoints": ["/support", "/recommend", "/social"]}

recommender = Recommender("data/products.json")
support_bot = SupportBot("data/faq.csv")
sm_creator = SocialMediaCreator()

class Query(BaseModel):
    text: str

@app.post("/recommend")
def recommend(q: dict):
    print("Received query:", q)
    res = recommender.recommend(q["text"])
    print("Returning:", res)
    return res


@app.post("/support")
def support(q: Query):
    return support_bot.answer(q.text)

@app.post("/social")
def social(q: Query):
    return {
        "captions": sm_creator.generate_captions(q.text),
        "ideas": sm_creator.generate_ideas(q.text),
    }
