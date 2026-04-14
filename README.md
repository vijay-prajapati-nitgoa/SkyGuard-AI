# 🛰️ SkyGuard AI – Aerial Object Classification System

## 📌 Overview
SkyGuard AI is a deep learning-based system that classifies aerial images into:

- 🐦 Bird  
- 🚁 Drone  

This system helps in:
- ✈️ Airport safety (bird strike prevention)
- 🛡️ Security & defense surveillance
- 🌿 Wildlife monitoring

---

## 🚀 Features
-  Binary Image Classification (Bird vs Drone)
- Transfer Learning using MobileNetV2
-  Real-time prediction using Streamlit
-  Confidence score display
-  Clean and user-friendly UI

---

## 🛠️ Tech Stack
- Python  
- TensorFlow / Keras  
- Streamlit  
- NumPy  
- OpenCV  
- Scikit-learn  

---

## 📂 Dataset


train/
valid/
test/


- Images resized to **224 × 224**
- Pixel values normalized to **[0,1]**

---

## 🧠 Model Architecture

### 🔹 Custom CNN
- Conv Layers (32, 64, 128 filters)
- MaxPooling layers
- Dense + Dropout
- Output: Sigmoid

### 🔹 Transfer Learning (Best Model)
- MobileNetV2 (pretrained)
- Faster training
- Better accuracy

---

## 📊 Results
- 🎯 Training Accuracy: ~96–98%
- 🎯 Validation Accuracy: ~80%
- ✔ Good generalization
- ✔ Real-time prediction working

---

## 🌐 Deployment

Run the app:

```bash
streamlit run app.py
💡 How it works:
Upload image
Model processes it
Output shows:
🐦 Bird
🚁 Drone
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

Used:

classification_report(y_true, y_pred)

Metrics:

Accuracy
Precision
Recall
F1-score
⚠️ YOLOv8 (Optional)
Explored YOLOv8 for object detection
Requires bounding box annotations
Current dataset is classification-based
🔮 Future Work
Add YOLO detection
Improve dataset
Real-time video detection
Cloud deployment
👨‍💻 Author

Vijay Prajapati
Electrical Engineering – NIT Goa
