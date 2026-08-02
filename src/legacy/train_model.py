import cv2
import numpy as np
import os

dataset_path = "dataset"
trainer_path = "trainer"

os.makedirs(trainer_path, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()

face_samples = []
face_ids = []

image_files = [f for f in os.listdir(dataset_path) if f.endswith('.jpg')]

print(f"Ditemukan {len(image_files)} foto di dataset. Memulai training...")

for filename in image_files:
    img_path = os.path.join(dataset_path, filename)

    gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    face_id = int(filename.split('.')[1])

    face_samples.append(gray_img)
    face_ids.append(face_id)

recognizer.train(face_samples, np.array(face_ids))

recognizer.save(f"{trainer_path}/trainer.yml")

print(f"Training selesai! Model disimpan di '{trainer_path}/trainer.yml'")
print(f"Total {len(np.unique(face_ids))} orang, {len(face_samples)} foto digunakan.")