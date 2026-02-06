from ultralytics import YOLO

# Load pretrained YOLOv8 nano model (you already have this file)
model = YOLO("yolov8n.pt")

# Train on your custom knife dataset
model.train(
    data="knife.v3i.yolov8/data.yaml",
    epochs=50,
    imgsz=640
)
