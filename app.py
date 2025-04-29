from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import cv2
import numpy as np
import io
import re

app = FastAPI()


def preprocess_image(image):
    img_array = np.array(image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return gray


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def extract_lab_data_rule_based(text):
    lines = text.split('\n')
    lab_data = []
    for line in lines:
        match = re.search(r"([A-Za-z\s]+)\s*([\d.]+)\s*(?:([-.\d]+)-([-.\d]+))?", line)
        if match:
            test_name = match.group(1).strip()
            value = float(match.group(2)) if match.group(2) else None
            lower_range = float(match.group(3)) if match.group(3) else None
            upper_range = float(match.group(4)) if match.group(4) else None
            lab_data.append({
                "test_name": test_name,
                "value": value,
                "bio_reference_range": f"{lower_range}-{upper_range}" if lower_range is not None and upper_range is not None else None
            })
    return lab_data


def calculate_out_of_range(value, reference_range):
    if value is None or reference_range is None:
        return None
    try:
        lower, upper = map(float, reference_range.split('-'))
        return not(lower <= value <= upper)
    except ValueError:
        return None

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File()):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        gray_image = preprocess_image(image)
        text = pytesseract.image_to_string(gray_image)
        lab_data = extract_lab_data_rule_based(text)

      

        for entry in lab_data:
            entry["lab_test_out_of_range"] = calculate_out_of_range(entry["value"], entry["bio_reference_range"])

        return JSONResponse(content={
            "lab_tests": lab_data,
            "is_success": True
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

