import os
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename

from src.ocr_processor import process_document_with_gemini_ocr
from src.document_classifier import process_and_classify_document
from src.storage import store_document
from src.summarizer import generate_summary
from src.metrics_tracker import MetricsTracker


class DocumentController:
    """Controller class for handling document processing operations"""
    
    @staticmethod
    def process_document():
        """
        Main endpoint for processing uploaded documents.
        Handles file upload, OCR, classification, storage, and summarization.
        """
        # Validate file upload
        validation_response = DocumentController._validate_file_upload()
        if validation_response:
            return validation_response
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        try:
            # Save uploaded file
            file.save(filepath)
            
            # Initialize metrics tracker
            metrics_tracker = MetricsTracker()
            
            # Process document through pipeline
            result = DocumentController._process_document_pipeline(filepath, metrics_tracker)
            
            return jsonify(result), 200
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500
        finally:
            # Clean up uploaded file
            DocumentController._cleanup_file(filepath)
    
    @staticmethod
    def _validate_file_upload():
        """
        Validate the uploaded file.
        Returns error response if validation fails, None if valid.
        """
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        return None
    
    @staticmethod
    def _process_document_pipeline(filepath, metrics_tracker):
        """
        Execute the complete document processing pipeline.
        
        Args:
            filepath (str): Path to the uploaded file
            metrics_tracker (MetricsTracker): Metrics tracking instance
            
        Returns:
            dict: Processing results including text, classification, summary, etc.
        """
        # Step 1: OCR and quality assessment
        text, quality = process_document_with_gemini_ocr(filepath)
        metrics_tracker.increment_llm_calls()
        metrics_tracker.set_ocr_quality(quality)
        
        # Step 2: Document classification
        classification = process_and_classify_document(text)
        metrics_tracker.increment_llm_calls()
        
        # Step 3: Store document
        storage_path = store_document(filepath, text, classification)
        
        # Step 4: Generate summary
        summary = generate_summary(text)
        metrics_tracker.increment_llm_calls()
        
        return {
            "message": "Document processed successfully!",
            "extracted_text": text,
            "classification": classification,
            "summary": summary,
            "storage_path": storage_path,
            "metrics": metrics_tracker.get_metrics()
        }
    
    @staticmethod
    def _cleanup_file(filepath):
        """
        Clean up the uploaded file after processing.
        
        Args:
            filepath (str): Path to the file to be deleted
        """
        if os.path.exists(filepath):
            os.remove(filepath)


def register_routes(app):
    """
    Register all application routes with the Flask app.
    
    Args:
        app (Flask): Flask application instance
    """
    app.add_url_rule(
        '/process_document',
        'process_document',
        DocumentController.process_document,
        methods=['POST']
    )