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


## Result of Testing 

   ```
         --- Processing: AHD-0425-PA-0007561_JITENDRA TRIVEDI DS_28-04-2025_1019-21_AM.pdf_page_9.png ---
      OCR processing failed: Document quality is too low: 42%
      {
      "error": "An error occurred: Document quality is too low: 42%"
      }

      --- Processing: AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_4.png ---
      {
      "message": "Document processed successfully!",
      "extracted_text": "Here's a text version of the image:\n\n**016**\n\n**SHREE DIAGNOSTIC CENTRE**\nTime: 8:00 am to 8:00 pm  Sunday - 8:00 to 12:00 noon\n\n**FULLY COMPUTERISED PATHOLOGICAL LABORATORY**\nSHREE HOSPITAL, Ganesh Baug,\nMurbad Road, Kalyan (W).\n\n**Patient:** *[Redacted]*\n**Dr.:** Dr. BHAVESH CHAUHAN MD\n**Sample Id:** 10437984\n**& Time:** 11:04:45\n**Report Release Time:** 12:52:39\n\n**CRP REPORT**\n\n**Test**                                     **Result**              **Unit**             **Biological Ref. Range**\nC-Reactive Protein (CRP)                  : 267.8 [H]             mg/L                0-5 mg/L\nMethod: Immunoturbidimetric\n\nAdults                                      : < 5 mg/L\nNew born up to 3 weeks                    : < 4.1 mg/L\nInfants and children                       : < 2.8 mg/L\n\nSpecimen: Serum\nEquipment: Biosystems BA200\n\n---- End Of Report ----\n\n**NABL M(EL)T LABS** *(logo)*\n\n*[signatures]*\n\n**Atul S. Vadhavkar**\nB. Sc. (Micro), D.M.L.T.\n\n**Dr. A. J. Ranadive**\nM.D. (Pathology)",
      "classification": "medical_records",
      "summary": "This document is a C-Reactive Protein (CRP) blood test report from Shree Diagnostic Centre for patient [redacted], ordered by Dr. Bhavesh Chauhan.  The test, performed on a Biosystems BA200 machine, shows a CRP level of 267.8 mg/L, significantly higher than the normal adult range of 0-5 mg/L.  The high CRP level is indicated by \"[H]\". The report is signed by Atul S. Vadhavkar and Dr. A. J. Ranadive.\n",
      "storage_path": "c:\\CompetitiveProgramming3.0\\ForWindflowAI\\notebooks\\dataset\\../output\\AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_4.png.json",
      "metrics": {
         "ocr_quality": 96.93,
         "llm_api_calls": 6,
         "overall_accuracy": 0.8645,
         "total_classifications": 41,
         "average_latency": 0.909,
         "medical_records_count": 9,
         "medical_records_avg_confidence": 99.28
      }
      }

      --- Processing: AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_7.png ---
      {
      "message": "Document processed successfully!",
      "extracted_text": "--- OCR Start ---\nAtul S. Vadhavkar\nB.Sc. (Micro). D.M.L.T.\nSHREE\nDIAGNOSTIC\nCENTRE\nTime: 8:00 am to 8:00 pm Sunday - 8:00 to 12:00 noon\nFULLY\nCOMPUTERISED\nPATHOLOGICAL\nLABORATORY\nSHREE HOSPITAL, Gan\nMurbad Road, Kalyan (W).\nDr.\n: Dr. BHAVESH CHAUHAN MD\n: Shree Hospital IPD\n& Time\n:\n12:47:26\nSample Id\n: 10436879\nReport Release Time\n:\n13:42:13\nCOMPLETE BLOOD COUNT\nTest\nResult\nUnit\nBiological Ref. Range\nHaemoglobin\n:\n9.10 [L]\ngm/dl\n13.0-17.0 gm/dl\nTotal R.B.C. Count\n:\n3.19 [L]\nmill/cmm\n4.5-5.5 mill/cmm\nHaematocrit (PCV/HCT)\n:\n27.20 [L]\n%\n40.0-50.0%\nMean Corpuscular Volume (M.C.V.)\n:\n85.30\nfl\n83.0-95.0 fl\nMean Corpuscular Hb (M.C.H.)\n:\n28.50\nPg\n27.0-32.0 Pg\nMean Corpuscular Hb Conc (M.C.H.C.) :\n33.50\ng/dl\n31.5-34.5 g/dl\n{#} Red cell Distribution Width (R.D.W.- :\n16.5 [H]\n%\n11.6-14.6%\nCV)\nTotal W.B.C. Count\n:\n10560 [H]\n/ul\n4000-10000/ul\nDIFFERENTIAL COUNT:\nNeutrophils\n:\n87.7 [H]\n%\n40-70%\nLymphocytes\n:\n5.9 [L]\n%\n20-40%\nEosinophils\n:\n0.7 [L]\n%\n1-6%\n5.5\n%\n2-10%\n:\n0.2\n%\n0-1%\nMonocytes\nBasophils\nPLATELETS\nPlatelet Count\n:\n370\n/uL\n{#} MPV\n:\n9.4\nfL\n{#} IMMATURE PLATELET FRACTION:\n2.90\n%\n150-450/uL\n6.78-13.46 fL\n0-5%\nABSOLUTE COUNTS\nNeutrophils (abs)\nLymphocytes (abs)\nEosinophils (abs)\nMonocytes (abs)\nBasophils (abs)\n:\n9261.12 [H]\n/uL\n1575-8800/uL\n:\n623.04 [L]\n/uL\n1125-4950/uL\n:\n73.92\n/uL\n0-400/uL\n:\n580.80\n/uL\n0-1000/uL\n:\n21.12\n/uL\n0-100/uL\nSpecimen: EDTA whole blood\nEquipment: Mindray BC-700\nMethod: HB-Colorimetric, WBC-Flowcytometry by laser, RBC & PLT-Elecrical Impedance, HCT, MCV, MCH, MCHC, RDW,MPV-Calculated\nBlood Peripheral Smear-RBC-WBC-PLT Morphology-Manual Method staining (Romanowsky) Field Stain and Microscopy.\n**CBC done on fully autoamted Five Part Haematology Analyser.\nAccuracy of platelet count depends on blood collection and anticoagulation.\nNote: # This Parameter is not under NABL scope.\nNABL\nM(EL)T\nLABS\nEnd Of Report\nSt. D. Vallar\nP\n1 of 4\nAtul S. Vadhavkar\nB. Sc. (Micro), D.M.L.T.\nDr. A. J. Ranadive\nM.D. (Pathology)\n--- OCR End ---",
      "classification": "medical_records",
      "summary": "This is a complete blood count (CBC) report for Atul S. Vadhavkar, performed at Shree Diagnostic Centre.  Several values are outside the normal reference range, indicating potential issues: Hemoglobin (9.10 gm/dl), Total RBC Count (3.19 mill/cmm), Hematocrit (27.20%), Lymphocytes (5.9%), and  Platelet count (370/uL) are all low.  Conversely, Red cell Distribution Width (16.5%), Total WBC Count (10560/ul), Neutrophils (87.7%), and Neutrophils (abs) (9261.12/uL) are all high.  The report notes that several parameters are not under NABL (National Accreditation Board for Testing and Calibration Laboratories) scope. The test was performed using a Mindray BC-700 automated hematology analyzer, with some manual microscopy also included.  The accuracy of the platelet count is noted to depend on blood collection and anticoagulation.\n",
      "storage_path": "c:\\CompetitiveProgramming3.0\\ForWindflowAI\\notebooks\\dataset\\../output\\AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_7.png.json",
      "metrics": {
         "ocr_quality": 98.82,
         "llm_api_calls": 2,
         "overall_accuracy": 0.1914,
         "total_classifications": 40,
         "average_latency": 2.812,
         "medical_records_count": 15,
         "medical_records_avg_confidence": 98.72
      }
      }

      --- Processing: AHD-0425-PA-0008061_E-mahendrasinghdischargecard_250427_1114@E.pdf_page_13.png ---
      {
      "message": "Document processed successfully!",
      "extracted_text": "---\n**Test Report**\n\n**SHREE DIAGNOSTIC CLINICAL LABORATORY**\n24 HOURS PATHOLOGY SERVICE | DIGITAL X-RAY\n\nK.P. Patil Building,\nNear Shivaji Maharaj Statue,\nMohopada, Tal. Khalapur,\nDist. Raigad - 410 222.\n\nMob: 93726 96384\n\nPatient ID:  27012\nGender: Male\nReport Print Time: 27-Apr-2025 10:18 AM\n\n**Complete Blood Count**\n\n**Test** | **Result** | **Unit** | **Reference Range**\n------- | -------- | -------- | --------\nHemoglobin | 11.6 | gm/dl | 13.0-17.0\nPacked Cell Volume (HCT) | 45.2 | % | 40-50\nR.B.C. Count | 5.10 | mill/cmm | 4.5 - 5.5\nMean Cell Volume(MCV) | 88.6 | fl | 83-101\nMean Cell Hemoglobin(MCH) | 22.7 | pg | 27-33\nMean Cell Hb Conc(MCHC) | 25.7 | % | 32-38\nTotal WBC Count | 9200 | cells/cumm | 4000-11000\nDifferential % WBCs count\nNeutrophils | 66 | % | 50-70\nLymphocytes | 24 | % | 20-40\nEosinophils | 4 | % | 1-6\nMonocytes | 06 | % | 0-10\nAbsolute Differential Count:\nAbsolute Neutrophils Count | 6072 | /cumm | 2000-7000\nAbsolute Lymphocytes Count | 2208 | /cumm | 1000-3000\nAbsolute Monocytes Count | 552 | /cumm | 200-1000\nAbsolute Eosinophils Count, AEC | 368 | /cumm | 20-500\nPlatelet Count | 398000 | cells/cumm | 20-500\n\nEND OF REPORT\n\nDr.Swapnil V.Sirmukaddam\nM.D. (Pathology)\n\n*These are only Laboratory & Technical Test Results.*  *These are not Medical Diagnostic Result in any case and purpose.*\n*Unexpected result should be confirmed with fresh specimen.* Laboratory Test result should be interpreted in correlation with clinical finding\n\n---",
      "classification": "medical_records",
      "summary": "This is a complete blood count (CBC) report for a male patient (ID 27012) from Shree Diagnostic Clinical Laboratory, dated April 27, 2025.  The report shows that the patient's hemoglobin level (11.6 gm/dl) is slightly below the reference range, while other values, such as hematocrit, RBC count, and WBC count, fall within or near the normal ranges.  Platelet count is also within the normal range.  The differential white blood cell count shows slightly elevated eosinophils (368/cumm), while other counts are within the normal range.  The report explicitly states that these results are laboratory findings and should be interpreted in conjunction with clinical findings by a physician.  The results should be confirmed if unexpected.\n",
      "storage_path": "c:\\CompetitiveProgramming3.0\\ForWindflowAI\\notebooks\\dataset\\../output\\AHD-0425-PA-0008061_E-mahendrasinghdischargecard_250427_1114@E.pdf_page_13.png.json",
      "metrics": {
         "ocr_quality": 94.41,
         "llm_api_calls": 2,
         "overall_accuracy": 0.5576,
         "total_classifications": 38,
         "average_latency": 2.913,
         "medical_records_count": 4,
         "medical_records_avg_confidence": 70.63
      }
      }

      --- Processing: AHD-0425-PA-0008061_E-mahendrasinghdischargecard_250427_1114@E.pdf_page_27.png ---
      {
      "message": "Document processed successfully!",
      "extracted_text": "Test Report\nSHREE DIAGNOSTIC\nCLINICAL LABORATORY\n24 HOURS PATHOLOGY SERVICE | DIGITAL X-RAY\nK.P. Patil Building,\nNear Shivaji Maharaj Statue,\nMohopada, Tal. Khalapur,\nDist. Raigad - 410 222.\nMob: 93726 96384\nPatient ID : 230425003\nBy Doctor : Dr. Ramesh Mhatre\nClient\nSample No\nComplete Blood Count (CBC)\nTest\nBLOOD COUNT (CBC)\nHemoglobin\n12.1 gm/dl 13.0-17.0\nPhotometry\nPacked Cell Volume (HCT)\n42.5 % 40-50\nCalculated\nR.B.C. Count\n4.90 mill/cmm 4.5-5.5\nElectrical Impedence\nMean Cell Volume(MCV)\n86.7 fl 83-101\nCalculated\nMean Cell Hemoglobin (MCH)\n24.7 pg 27-33\nCalculated\nMean Cell Hb Conc(MCHC)\n28.5 % 32-38\nCalculated\nTotal WBC Count\n13600 cells/cumm 4000-11000\nFlow Cytometry\nDifferential % WBCs count\nNeutrophils\n66 % 50-70\nFCM/ Microscopy\nLymphocytes\n24 % 20-40\nFCM/ Microscopy\nEosinophils\n4 % 1-6\nFCM/ Microscopy\nMonocytes\n06 % 0-10\nFCM/ Microscopy\nAbsolute Differential Count:\nAbsolute Neutrophils Count\n8976 / cumm 2000-7000\nAbsolute Lymphocytes Count\n3264 / cumm 1000-3000\nAbsolute Monocytes Count\n816 / cumm 200-1000\nAbsolute Eosinophils Count, AEC\n544 / cumm 20-500\nPlatelet Count\n502000 cells/cumm\nElectrical Impedence\nEND OF REPORT\nScan to Validate\nPage 1 of 5\nThese are only Laboratory & Technical Test Results.\nUnexpected result should be confirmed with fresh specimen.\nDr.Swapnil V.Sirmukaddam\nM.D. (Pathology)\nThese are not Medical Diagnostic Result in any case and purpose.\nLaboratory Test result should be interpreted in correlation with clinical finding.\n27",
      "classification": "medical_records",
      "summary": "This is a complete blood count (CBC) report for patient ID 230425003, ordered by Dr. Ramesh Mhatre.  Several values are slightly outside the normal range, including hemoglobin (12.1 gm/dl), total WBC count (13600 cells/cumm), and absolute eosinophil count (544/cumm).  All other values are within or near the normal range.  The report emphasizes that these results are for laboratory and technical purposes only and should be interpreted in conjunction with clinical findings.  A physician's interpretation is required for diagnosis.\n",
      "storage_path": "c:\\CompetitiveProgramming3.0\\ForWindflowAI\\notebooks\\dataset\\../output\\AHD-0425-PA-0008061_E-mahendrasinghdischargecard_250427_1114@E.pdf_page_27.png.json",
      "metrics": {
         "ocr_quality": 88.16,
         "llm_api_calls": 6,
         "overall_accuracy": 0.2781,
         "total_classifications": 28,
         "average_latency": 4.366,
         "medical_records_count": 12,
         "medical_records_avg_confidence": 85.66
      }
      }
   ```
## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
