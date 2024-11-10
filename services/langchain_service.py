import os
from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

model = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.5
)


def summarize_text(input_text:str)->str:
    prompt=f"Summarize the following text:\n\n{input_text}"
    response=model.invoke(prompt)
    return response
