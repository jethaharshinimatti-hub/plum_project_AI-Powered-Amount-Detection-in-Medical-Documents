# AI-Powered Amount Detection in Medical Documents

## Overview

This project extracts financial amounts from medical bills and receipts using OCR and classifies them into categories such as Total Bill, Paid Amount, and Due Amount.

The system accepts image uploads, extracts text using OCR, identifies monetary values, classifies them based on context, and returns structured JSON output.

## Features

- OCR-based text extraction from medical bills
- Amount detection using regex
- Classification of amounts (Total, Paid, Due)
- JSON API response
- FastAPI backend
- Swagger API documentation

## Tech Stack

- Python
- FastAPI
- EasyOCR
- OpenCV
- NumPy

## Project Structure

```text
medical-amount-detector/
│
├── main.py
├── requirements.txt
├── README.md
├── sample_images/
└── uploads/
```

## Installation

### Clone Repository

```bash
git clone <your-github-repo-link>
cd medical-amount-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

## API Documentation

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST /extract

Upload a medical bill image.

#### Sample Response

```json
{
  "currency": "INR",
  "amounts": [
    {
      "type": "total_bill",
      "value": 1200,
      "source": "Total: INR 1200"
    },
    {
      "type": "paid",
      "value": 1000,
      "source": "Paid: 1000"
    },
    {
      "type": "due",
      "value": 200,
      "source": "Due: 200"
    }
  ],
  "status": "ok"
}
```

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/extract" \
-F "file=@bill.jpg"
```

## Future Improvements

- OCR error correction
- Support for multiple currencies
- Confidence scoring
- Better amount classification
- Cloud deployment

## Author

M Jetha Harshini
B.Tech Electrical Engineering
IIT Madras
