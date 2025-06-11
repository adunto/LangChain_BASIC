from langchain_openai import ChatOpenAI
import csv
from dotenv import load_dotenv
import os

load_dotenv()

def getModel():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    model = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        base_url="https://api.groq.com/openai/v1",  # Groq API 엔드포인트
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.7
    )
    return model