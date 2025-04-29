🧬 Lab Report Extraction API

A scalable and accurate Python-based FastAPI service to extract lab test names, values, and reference ranges from lab report images. This solution uses OCR and custom logic (no LLMs) to parse structured lab data for downstream processing and evaluation.

📌 Problem Statement
Objective: Extract all lab test names, their corresponding values, and reference ranges from lab report images and return the data in a structured JSON format.

Endpoint: POST /get-lab-tests

Constraints:

⚠️ Use of LLMs (e.g., GPT, Claude, Gemini, etc.) is strictly prohibited.

✅ Use only traditional OCR, pattern matching, and classical techniques.

🗃 Dataset
📥 Download the lab report image dataset here:

🚀 API Overview
POST /get-lab-tests

🧰 Tech Stack
🐍 Python 3.8+

⚡ FastAPI

🖼️ OpenCV / PIL

🔤 Tesseract OCR

🧠 Regex + Rule-Based Parsing

🛠 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/lab-report-extraction-api.git
cd lab-report-extraction-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload
🧪 Example Usage
bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/get-lab-tests" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path_to_image.jpg"
📁 Project Structure
bash
Copy
Edit
lab-report-extraction-api/
├── app/
│   ├── main.py              # FastAPI app
│   ├── ocr_utils.py         # Image preprocessing & OCR
│   ├── parser.py            # Lab test extraction logic
│   └── models.py            # Pydantic data models
├── test_images/             # Sample test images
├── requirements.txt
└── README.md
❗ Disclaimer
❌ No use of LLMs or generative models allowed.

🛠 Custom, explainable logic and traditional ML methods only.

✅ Solution complies with competition rules and constraints.

📄 License
This project is licensed under the MIT License.
