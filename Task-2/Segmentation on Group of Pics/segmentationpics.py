from ultralytics import YOLO
import os

# Load the segmentation model
model = YOLO("yolov8n-seg.pt")  # Make sure the model file is in this folder

# Input and output paths
folder_path = "D:/YOLO Project/images"
output_path = "D:/YOLO Project/output"

# Make output folder if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Process all image files
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

for file in image_files:
    img_path = os.path.join(folder_path, file)
    print("Processing:", img_path)
    
    # Run segmentation and save results to 'output/seg_results'
    results = model(img_path, save=True, project=output_path, name="seg_results", exist_ok=True)
