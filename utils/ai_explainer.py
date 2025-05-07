import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)


def explain_code(code_snippet):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Explain this code snippet:\n{code_snippet}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI explanation error: {str(e)}"


def generate_summary(code):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = (
            f"Summarize what the following binary code does at a high level:\n\n{code}"
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI explanation error: {str(e)}"
