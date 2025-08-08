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
![Confusion Matrix](<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/4dc7ef06-3af8-41cc-bc7b-de058785d0aa" />
)

### Normalized Confusion Matrix
![Normalized Confusion Matrix](<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/6a7a375e-133c-4cee-a6fa-e6d8cdbe4045" />
)

### Precision, Recall, and F1-score Curves
![P Curve](<img width="2250" height="1500" alt="P_curve" src="https://github.com/user-attachments/assets/3723e229-ee97-41f3-af83-6712945e54c2" />

)  
![R Curve](<img width="2250" height="1500" alt="R_curve" src="https://github.com/user-attachments/assets/bc08f23e-e939-4213-8044-5a396edf3b93" />

)  
![F1 Curve](<img width="2250" height="1500" alt="F1_curve" src="https://github.com/user-attachments/assets/141e7bba-1905-45a7-8ed5-f27c2f9c3d80" />
)  

### PR Curve
![PR Curve](<img width="2250" height="1500" alt="PR_curve" src="https://github.com/user-attachments/assets/090dbc79-5cfa-42e2-827b-3eca1649e185" />
)

### Dataset Labels
![labels](https://github.com/user-attachments/assets/56c04431-2ab8-45eb-ba9e-5b59a3c6d225)


---

📌 *This task covers the complete pipeline: data collection, annotation, training, evaluation, and results interpretation for multi-class object detection.*
