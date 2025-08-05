
import os
import google.generativeai as genai



def generate_summary(text):
    """
    Generates a summary of the document using the Gemini API.
    """
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Summarize the following insurance claim document:\n\n{text}")
        return response.text
    except Exception as e:
        return f"Error generating summary: {e}"
