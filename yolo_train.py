from ultralytics import YOLO

# load model
model = YOLO("yolov8n.pt")

# train model
model.train(
    data=r"C:\Users\praja\OneDrive\Desktop\python jupyter vs\ariel  project3\data.yaml",
    epochs=20,
    imgsz=640
)