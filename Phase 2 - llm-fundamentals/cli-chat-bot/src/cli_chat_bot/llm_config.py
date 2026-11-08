import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = os.environ.get("LLM_BASE_URL","http://localhost:11434/v1")
API_KEY = os.environ.get("LLM_API_KEY","ollama")
MODEL = os.environ.get("LLM_MODEL","qwen3:4b")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)