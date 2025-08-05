
import os
import sys
import time
from PIL import Image, ImageDraw, ImageFont # type: ignore

from ocr_processor import process_document_with_gemini_ocr
from document_classifier import classify_document
from storage import store_document
from summarizer import generate_summary
from metrics_tracker import MetricsTracker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main(file_path):
    """
    Main function to process an insurance claim document.
    """
    metrics_tracker = MetricsTracker()

    try:
        # Step 1: OCR and quality assessment
        text, quality = process_document_with_gemini_ocr(file_path)
        metrics_tracker.set_ocr_quality(quality)

        # Step 2: Document classification
        classification = classify_document(text)

        # Step 3: Store document
        storage_path = store_document(file_path, text, classification)

        # Step 4: Generate summary
        summary = generate_summary(text)
        metrics_tracker.increment_llm_calls()  # Assuming one call for summarization

        # Final output
        print("Claim Processed Successfully!")
        print(f"Stored at: {storage_path}")
        print("\nSummary:")
        print(summary)

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

    finally:
        print("\nMetrics:")
        print(metrics_tracker.get_metrics())

if __name__ == "__main__":
    # Ensure the API key is set in the environment
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        sys.exit(1)

    # Give the server a moment to start
    time.sleep(3)

    # Create a dummy document for testing
    document_dir = os.path.join(os.path.dirname(__file__), "../documents")
    if not os.path.exists(document_dir):
        os.makedirs(document_dir)

    file_path = os.path.join(document_dir, "sample_claim.jpg")

    # Create a blank image
    img = Image.new('RGB', (800, 200), color = 'white')
    d = ImageDraw.Draw(img)

    # Add text to the image
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()
    
    text = "This is a detailed medical report from the central hospital.\n" \
           "The patient, John Doe, was admitted with a severe personal injury to his left leg.\n" \
           "The unfortunate accident happened during a morning walk on the 15th of March."
    d.text((10,10), text, fill=(0,0,0), font=font)

    img.save(file_path)

    main(file_path)


