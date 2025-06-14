from ultralytics import YOLO

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

# Run segmentation on the image
results = model("https://ultralytics.com/images/bus.jpg")

# Loop through results to display or save
for result in results:
    result.show()   # To display
    result.save(filename='output.jpg')  # Optional: to save the image
