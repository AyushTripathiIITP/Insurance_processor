
def classify_document(text):
    """
    Classifies the document based on keywords.
    """
    text = text.lower()
    if "medical" in text or "hospital" in text:
        return "Medical Records"
    elif "injury" in text or "accident" in text:
        return "Personal Injury"
    else:
        return "Other"
