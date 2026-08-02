import cv2
import pickle
import os

detector = cv2.FaceDetectorYN.create(
    model="src/models/face_detection_yunet_2023mar.onnx",
    config="",
    input_size=(320, 320),
    score_threshold=0.7,
    nms_threshold=0.3,
    top_k=5000
)

recognizer = cv2.FaceRecognizerSF.create(
    model="src/models/face_recognition_sface_2021dec.onnx",
    config=""
)

DB_PATH = "trainer/face_database.pkl"

if not os.path.exists(DB_PATH):
    print("Error: Database wajah belum ada. Jalankan enroll_face.py dulu.")
    exit()

with open(DB_PATH, "rb") as f:
    face_database = pickle.load(f)

if len(face_database) == 0:
    print("Error: Database kosong. Jalankan enroll_face.py dulu.")
    exit()

COSINE_THRESHOLD = 0.363

def recognize_face(feature):
    best_match_name = "Unknown"
    best_match_score = 0

    for name, stored_features in face_database.items():
        for stored_feature in stored_features:
            score = recognizer.match(feature, stored_feature, cv2.FaceRecognizerSF_FR_COSINE)

            if score > best_match_score:
                best_match_score = score
                best_match_name = name

    if best_match_score < COSINE_THRESHOLD:
        return "Unknown", best_match_score

    return best_match_name, best_match_score

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
detector.setInputSize((frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Gagal membaca frame dari webcam")
        break

    _, faces = detector.detect(frame)

    if faces is not None:
        for face in faces:
            x, y, w, h = face[0:4].astype(int)

            aligned_face = recognizer.alignCrop(frame, face)
            feature = recognizer.feature(aligned_face)

            name, score = recognize_face(feature)

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

            label = f"{name} ({score:.2f})"
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Face Recognition (SFace)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()