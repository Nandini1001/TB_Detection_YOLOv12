# Tuberculosis Detection 

This project is a web-based application that detects **Tuberculosis (TB)** from chest X-ray images using a trained YOLO deep learning model.  
The application allows users to upload an X-ray image and receive a prediction indicating whether the patient is **Healthy** or has **Tuberculosis**, along with the model's confidence score.

## Features

- Upload chest X-ray images through a web interface
- Automatic detection using a trained YOLO model
- Displays detected image with bounding box
- Shows prediction result (Healthy / Tuberculosis)
- Displays confidence score
- Color-coded result box:
  - Green for **Healthy**
  - Red for **Tuberculosis**
- Simple and user-friendly interface

## Technologies Used

- Python
- Flask
- Ultralytics YOLO
- OpenCV
- HTML
- CSS
- JavaScript

## Project Structure
```
TB-Detection-YOLO/
│
├── YOLO
|    ├── yolov12
│    └── Dataset
│    
├── .vscode
│    └── settings.json
|
├── app.py
│
├── best.pt
│
├── uploads/      (creted automatically)
│
├── results/      (creted automatically)
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

```

# About seetings.json
Access the settings.json file through google drive.
