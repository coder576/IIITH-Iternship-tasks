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
![Confusion Matrix](<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/bd0652ab-ec6c-445f-847a-47debc961687" />

)

### Normalized Confusion Matrix
![Normalized Confusion Matrix](<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/49765161-e70c-4f37-bc79-ae0f84ed354e" />

)

### Precision, Recall, and F1-score Curves
![P Curve](<img width="2250" height="1500" alt="P_curve" src="https://github.com/user-attachments/assets/3723e229-ee97-41f3-af83-6712945e54c2" />

)  
![R Curve](<img width="2250" height="1500" alt="R_curve" src="https://github.com/user-attachments/assets/bc08f23e-e939-4213-8044-5a396edf3b93" />

)  
![F1 Curve](<img width="2250" height="1500" alt="F1_curve" src="https://github.com/user-attachments/assets/7118916a-2817-44d4-b608-825b7e7d670d" />

)  

### PR Curve
![PR Curve](<img width="2250" height="1500" alt="PR_curve" src="https://github.com/user-attachments/assets/f5a96183-f186-401e-b16d-5a8d1c439f9e" />

)

### Dataset Labels
![labels](https://github.com/user-attachments/assets/56c04431-2ab8-45eb-ba9e-5b59a3c6d225)


---

📌 *This task covers the complete pipeline: data collection, annotation, training, evaluation, and results interpretation for multi-class object detection.*
