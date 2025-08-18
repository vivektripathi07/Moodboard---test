import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-2.5-flash"

def expand_prompt(user_input, answers, reference_format):
    system_instruction = (
        "You are an expert creative strategist and prompt engineer. "
        "You take labels and their responses and generate prompts which prompts for building moodboard."
        "and expand them into a polished, structured professional prompt for AI image generation."
        "You use content from labels (service, sub-service, style, application and project breif) and get context for the moodboard"
        "Use the following reference format as a guide: \n" + reference_format + "But dont exactly repeat whats written."
    )
    model = genai.GenerativeModel(model_name=MODEL, system_instruction=system_instruction)
    response = model.generate_content(f"Labels:{user_input} \nValues: {answers}")
    return response.text.strip()

def call_api(prompt_val):
    url = "https://ai-collab.openai.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01"
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt_val,
        "size": "1024x1024",
        "n": 1
    }

    response = requests.post(url, headers=headers, json=data)

    return response





