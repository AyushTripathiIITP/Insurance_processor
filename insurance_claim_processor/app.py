import os
import sys
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS # type: ignore

# Add the parent directory to the sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ocr_processor import process_document_with_gemini_ocr
from src.document_classifier import classify_document
from src.storage import store_document
from src.summarizer import generate_summary
from src.metrics_tracker import MetricsTracker

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/process_document', methods=['POST'])
def process_document_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        metrics_tracker = MetricsTracker()
        try:
            # Step 1: OCR and quality assessment
            text, quality = process_document_with_gemini_ocr(filepath)
            metrics_tracker.set_ocr_quality(quality)

            # Step 2: Document classification
            classification = classify_document(text)

            # Step 3: Store document
            storage_path = store_document(filepath, text, classification)

            # Step 4: Generate summary
            summary = generate_summary(text)
            metrics_tracker.increment_llm_calls()

            return jsonify({
                "message": "Document processed successfully!",
                "extracted_text": text,
                "classification": classification,
                "summary": summary,
                "storage_path": storage_path,
                "metrics": metrics_tracker.get_metrics()
            }), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500
        finally:
            # Clean up the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)

if __name__ == '__main__':
    # Ensure GOOGLE_API_KEY is set
    if "GOOGLE_API_KEY" not in os.environ:
        print("Error: GOOGLE_API_KEY environment variable not set. Please set it before running the server.")
        sys.exit(1)
    app.run(debug=True, port=5001)
