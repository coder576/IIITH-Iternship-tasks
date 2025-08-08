# 🧠 Task 4 – Custom Object Detection using YOLOv8

This project demonstrates a **custom object detection model** built with **YOLOv8n** to detect **10 object classes** from a video recorded in my living room.

---

## 📂 Classes
- Door  
- Curtain  
- Tube light  
- PhotoFrame  
- TV  
- Phone  
- Table  
- Sofa  
- Glasses  
- Laptop  

---

## 📋 Process
1. **Video to Images** – Extracted frames from the recorded video.  
2. **Annotation** – Labeled images using [Makesense.ai](https://www.makesense.ai/) in YOLO format.  
3. **Dataset Organization** – Split into `train` and `val` folders; configured `data.yaml`.  
4. **Model Training** – Trained YOLOv8n on the custom dataset.  
5. **Evaluation** – Used PR curves, confusion matrices, and performance metrics.

---

## 📊 Results
- **mAP@0.5**: `0.547`  
- Strong precision for **Door**, **Tube light**, **Glasses**.  
- Visual performance metrics below are generated from `runs/train/`:

### Confusion Matrix
![Confusion Matrix](confusion_matrix.png)

### Normalized Confusion Matrix
![Normalized Confusion Matrix](confusion_matrix_normalized.png)

### Precision, Recall, and F1-score Curves
![P Curve](P_curve.png)  
![R Curve](R_curve.png)  
![F1 Curve](F1_curve.png)  

### PR Curve
![PR Curve](PR_curve.png)

### Dataset Labels
![Labels](labels.jpg)

---

📌 *This task covers the complete pipeline: data collection, annotation, training, evaluation, and results interpretation for multi-class object detection.*
