from openai import OpenAI
from config import base_url, api_key, gemini_model



gemini_client = OpenAI(
    base_url = base_url,
    api_key = api_key
)

def get_response(messages):
    response = gemini_client.chat.completions.create(model = gemini_model, messages = messages)
    assistant_response = response.choices[0].message.content
    return assistant_response
