from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel
import os

def get_llm() -> BaseChatModel:
    load_dotenv()

    model_name = os.getenv("MODEL_NAME", "qwen2.5")
    

    llm =  ChatOllama(
        model=model_name,
        temperature=0
    )
    return llm
