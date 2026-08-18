import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def make_llm(temperature=0.3, max_tokens=2048):
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="nvidia/nemotron-3.5-lightning:free",
        temperature=temperature,
        max_tokens=max_tokens,
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "multi-agent-coding"
        }
    )