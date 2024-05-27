from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model("image3.jpg", show=True)
cv2.waitKey(0)