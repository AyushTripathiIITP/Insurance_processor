import os
import google.generativeai as genai # type: ignore
import re
from typing import Dict
import time
from .metrics_tracker import metrics_tracker

def classify_document_using_LLM(text: str) -> Dict[str, str]:
    """
    Uses Gemini AI to classify documents with high accuracy.
    Returns classification with confidence score and reasoning.
    """
    start_time = time.time()
    try:
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        classification_prompt = f"""
        You are an expert document classifier analyze the following document text and classify it into one of these three categories:
        1. medical_records - Medical reports, lab results, prescriptions, hospital records, doctor notes, medical bills, health insurance documents
        2. personal_injury - Accident reports, injury claims, insurance claims related to accidents, legal documents about injuries, workers compensation
        3. others - Any document that doesn't fit the above categories
        
        Document text:
        {text[:2000]}
        
        Please respond in the following format:
        Classification: [category]
        Confidence: [0-100]
        Reasoning: [brief explanation of why this classification was chosen]
        """
        
        response = model.generate_content(classification_prompt)
        result = parse_ai_classification(response.text)
        
        latency = time.time() - start_time
        metrics_tracker.classification.update(
            classification=result['classification'],
            confidence=result['confidence'],
            latency=latency
        )
        
        return result
        
    except Exception as e:
        latency = time.time() - start_time
        metrics_tracker.classification.update(
            classification='error',
            confidence=0,
            latency=latency
        )
        return f"AI classification failed: {e}"
        

def parse_ai_classification(response_text: str) -> Dict[str, any]:
    """
    Parses the AI response to extract classification details.
    """
    try:
        classification = "Others"  # default
        confidence = 50  # default
        reasoning = "Unable to parse AI response"
        
        # Extract classification
        class_match = re.search(r'Classification:\s*(\w+)', response_text, re.IGNORECASE)
        if class_match:
            classification = class_match.group(1).lower()
        
        # Extract confidence
        conf_match = re.search(r'Confidence:\s*(\d+)', response_text)
        if conf_match:
            confidence = int(conf_match.group(1))
        
        # Extract reasoning
        reason_match = re.search(r'Reasoning:\s*(.+?)(?:\n|$)', response_text, re.IGNORECASE)
        if reason_match:
            reasoning = reason_match.group(1).strip()

        print(f"AI Classification Result: {classification}, Confidence: {confidence}, Reasoning: {reasoning}")

        return {
            "classification": classification,
            "confidence": confidence,
            "reasoning": reasoning,
        }
        
    except Exception as e:
        print(f"Error parsing AI response: {e}")
        return {
            "classification": "others",
            "confidence": 30,
            "reasoning": f"Error parsing response: {str(e)}",
            "method": "error"
        }

def classify_document_detailed(text: str) -> Dict[str, str]:
    """
    Enhanced classification function that returns detailed results.
    """
    return classify_document_using_LLM(text)
    
def process_and_classify_document(text: str) -> Dict[str, str]:
    """
    Complete pipeline: Classification
    """
    try:
        # Classify the document
        classification_result = classify_document_detailed(text)
        
        print(f"Document: {metrics_tracker.get_metrics()}")
        return classification_result["classification"]
        
    except Exception as e:
        print(f"Document processing failed: {e}")
        raise
