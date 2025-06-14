import os
import cv2
from ultralytics import YOLO

# Paths
input_folder = "D:/YOLO Project/frames"
processed_folder = "D:/YOLO Project/segmented_frames"
output_video_path = "D:/YOLO Project/output_video_segmented.mp4"
model_path = "yolov8n-seg.pt"  # path to your YOLOv8 segmentation model

# Create folder for processed frames
os.makedirs(processed_folder, exist_ok=True)

# Load YOLOv8 segmentation model
model = YOLO(model_path)

# Get list of frame files
frame_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

# Process each frame
for filename in frame_files:
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    # Run segmentation inference on the frame
    results = model(img)

    # results[0].masks.xy or results[0].masks.data contains masks
    # For visualization, use results[0].plot() which overlays masks and boxes on image
    
    # Get overlay image with masks drawn
    segmented_img = results[0].plot()

    # Save the segmented/overlayed frame
    save_path = os.path.join(processed_folder, filename)
    cv2.imwrite(save_path, segmented_img)
    print(f"Processed and saved: {filename}")

# Stitch frames into a video
first_frame = cv2.imread(os.path.join(processed_folder, frame_files[0]))
height, width, layers = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  # Adjust to your original video's FPS

out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

for filename in frame_files:
    frame = cv2.imread(os.path.join(processed_folder, filename))
    out.write(frame)

out.release()
print(f"\n🎉 Done! Segmented video saved at: {output_video_path}")

