# Insurance Claim Processor

This project is an automated insurance claim processing system that leverages a Retrieval-Augmented Generation (RAG) pipeline for document classification. The system is designed to streamline the handling of insurance claims by accurately classifying documents, providing reasoning for its classifications, and indicating a confidence level for each prediction.

## Features

- **Automated Document Classification:** Utilizes a RAG pipeline to classify insurance claim documents.
- **Reasoning and Confidence Levels:** Provides detailed reasoning for each classification and a confidence score to ensure accuracy.
- **Frontend Interface:** A user-friendly interface for uploading and managing insurance claims.
- **Scalable Architecture:** Built with a modular design to allow for future expansion and integration.

## Project Structure

```
/mnt/c/CompetitiveProgramming3.0/ForWindflowAI/
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── ...
│   ├── package.json
│   └── ...
├── insurance_claim_processor/
│   ├── src/
│   │   ├── document_classifier.py
│   │   ├── ocr_processor.py
│   │   └── ...
│   ├── app.py
│   ├── controller.py
│   └── requirements.txt
├── notebooks/
│   ├── test_RAG_pipeline.ipynb
│   └── ...
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js and npm

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/insurance-claim-processor.git
   cd insurance-claim-processor
   ```

2. **Set up the backend:**
   ```bash
   cd insurance_claim_processor
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up the frontend:**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start the backend server:**
   ```bash
   cd insurance_claim_processor
   source venv/bin/activate
   python app.py
   ```

2. **Start the frontend development server:**
   ```bash
   cd ../frontend
   npm run dev
   ```

## Usage

1. Open your browser and navigate to `http://localhost:5173`.
2. Upload an insurance claim document through the frontend interface.
3. The system will process the document, classify it, and display the classification, reasoning, and confidence level.

## RAG Pipeline

The core of this project is the RAG pipeline, which is used for document classification. This pipeline enhances the classification process by:

1. **Retrieving Relevant Information:** The RAG model retrieves relevant information from a knowledge base to inform its classification.
2. **Generating Reasoning:** The model generates a detailed explanation for its classification, which helps to ensure transparency and accuracy.
3. **Providing Confidence Levels:** A confidence level is provided for each classification, which allows for a better understanding of the model's certainty.

This approach ensures that the document classification is not only accurate but also transparent and reliable.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
