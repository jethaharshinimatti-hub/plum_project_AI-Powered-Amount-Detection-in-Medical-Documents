from fastapi import FastAPI, UploadFile, File
import easyocr
import re
import cv2
import numpy as np

app = FastAPI()

reader = easyocr.Reader(['en'])

def classify_amounts(text):
    amounts = []

    total_match = re.search(r"total[:\s]*.*?(\d+)", text, re.I)
    paid_match = re.search(r"paid[:\s]*.*?(\d+)", text, re.I)
    due_match = re.search(r"due[:\s]*.*?(\d+)", text, re.I)

    if total_match:
        amounts.append({
            "type": "total_bill",
            "value": int(total_match.group(1)),
            "source": total_match.group(0)
        })

    if paid_match:
        amounts.append({
            "type": "paid",
            "value": int(paid_match.group(1)),
            "source": paid_match.group(0)
        })

    if due_match:
        amounts.append({
            "type": "due",
            "value": int(due_match.group(1)),
            "source": due_match.group(0)
        })

    return amounts


@app.post("/extract")
async def extract_amounts(file: UploadFile = File(...)):

    contents = await file.read()

    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    ocr_result = reader.readtext(img, detail=0)

    text = " ".join(ocr_result)

    amounts = classify_amounts(text)

    return {
        "currency": "INR",
        "amounts": amounts,
        "status": "ok",
        "raw_text": text
    }
