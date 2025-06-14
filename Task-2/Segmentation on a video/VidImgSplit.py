import cv2
import os

# --- CONFIG ---
video_path = "D:/YOLO Project/input.mp4"   # Your input video path
output_folder = "D:/YOLO Project/frames"         # Folder to save extracted frames
frame_interval = 5  # Save every 5th frame (adjust as needed)

# --- PREPARE FOLDER ---
os.makedirs(output_folder, exist_ok=True)

# --- OPEN VIDEO ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError("❌ Could not open video file: " + video_path)

frame_count = 0
saved_count = 0

# --- FRAME LOOP ---
while True:
    success, frame = cap.read()
    if not success:
        break  # End of video

    if frame_count % frame_interval == 0:
        filename = f"frame_{saved_count:04d}.jpg"
        filepath = os.path.join(output_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"✅ Saved {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"\n🎉 Done! Saved {saved_count} frames in: {output_folder}")
