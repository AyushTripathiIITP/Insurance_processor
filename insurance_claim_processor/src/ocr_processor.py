import os
import google.generativeai as genai # type: ignore

def process_document_with_gemini_ocr(file_path):
    """
    Processes a document using Gemini for OCR.
    """
    try:
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')

        with open(file_path, 'rb') as f:
            image_data = f.read()

        image_parts = [
            {
                "mime_type": "image/jpeg",  # Adjust if needed
                "data": image_data
            }
        ]

        response = model.generate_content([
            "Extract text from this image.",
            image_parts[0]
        ])

        text = response.text

        quality = assess_quality(text)
        if quality < 45:
            raise ValueError(f"Document quality is too low: {quality}%")

        print(f"OCR results:\n{text}\nQuality: {quality}%")
        return text, quality

    except Exception as e:
        print(f"OCR processing failed: {e}")
        raise

def assess_quality(text):
    """
    Calculates a quality score for the OCR text.
    This is a simple heuristic based on character count and word length.
    """
    if not text.strip():
        return 0

    words = text.split()
    if not words:
        return 0

    avg_word_length = sum(len(word) for word in words) / len(words)
    quality = min(100, int(avg_word_length * 10))
    return quality
