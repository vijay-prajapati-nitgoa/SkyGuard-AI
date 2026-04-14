SkyGuard AI – Aerial Object Classification System
 Overview

SkyGuard AI is a deep learning-based system that classifies aerial images into Bird 🐦 or Drone 🚁.

This project helps in:

✈️ Airport safety (bird strike prevention)
🛡️ Security & defense surveillance
🌿 Wildlife monitoring
🚀 Features
 Binary image classification (Bird vs Drone)
 Transfer Learning using MobileNetV2
 Real-time prediction using Streamlit
 Confidence score display
 Clean and user-friendly UI
 Tech Stack
Python
TensorFlow / Keras
Streamlit
NumPy
OpenCV
Scikit-learn
📂 Dataset
Binary classification dataset:
Bird 🐦
Drone 🚁
📁 Structure:
train/
valid/
test/
Images are resized to 224×224
Pixel values normalized to [0,1]
 Model Architecture
🔹 Custom CNN
Convolution layers (32, 64, 128 filters)
MaxPooling layers
Dense layers + Dropout
Output: Sigmoid (binary classification)
🔹 Transfer Learning (Best Model)
MobileNetV2 (pretrained)
Faster training + better accuracy
📊 Results
 Training Accuracy: ~96–98%
Validation Accuracy: ~80%
Good generalization
Correct real-time predictions
🌐 Deployment (Streamlit App)

Run the application:

streamlit run app.py
 How it works:
Upload an image
Model processes it
Output shows:
Bird 🐦
Drone 🚁
Confidence score
📁 Project Structure
SkyGuard-AI/
│
├── train/
├── valid/
├── test/
├── models/
│   └── transfer_model.h5
│
├── app.py
├── train_cnn.py
├── train_transfer.py
├── evaluate.py
├── utils.py
├── yolo_train.py (optional)
├── requirements.txt
└── README.md
📈 Model Evaluation

Evaluation performed using:

classification_report(y_true, y_pred)

Metrics:

Accuracy
Precision
Recall
F1-score
⚠️ YOLOv8 (Optional)
YOLOv8 was explored for object detection
Requires bounding box annotations (.txt labels)
Current dataset is classification-based

 Hence, YOLO is included as future enhancement

🎯 Applications
✈️ Airport bird detection
🛡️ Drone surveillance
🌿 Wildlife research
🚁 Airspace monitoring
🔮 Future Work
Add YOLOv8 object detection
Improve dataset with bounding boxes
Real-time video detection
Deploy on cloud (AWS/Heroku)
 Author

Vijay Prajapati
Electrical Engineering – NIT Goa

 Acknowledgment

This project was developed as part of an internship in Deep Learning & Computer Vision.
