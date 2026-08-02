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
os.makedirs("trainer", exist_ok=True)

if os.path.exists(DB_PATH):
    with open(DB_PATH, "rb") as f:
        face_database = pickle.load(f)
else:
    face_database = {}

person_name = input("Masukkan nama orang yang mau didaftarkan: ")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
detector.setInputSize((frame_width, frame_height))

TARGET_SAMPLES = 5
collected_features = []

print(f"\nMulai enrollment untuk '{person_name}'")
print("Hadapkan wajah ke kamera. Tekan SPASI untuk ambil sampel, 'q' untuk berhenti.\n")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Gagal membaca frame dari webcam")
        break

    _, faces = detector.detect(frame)

    if faces is not None and len(faces) > 0:
        face = faces[0]
        x, y, w, h = face[0:4].astype(int)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f"Sampel terkumpul: {len(collected_features)}/{TARGET_SAMPLES}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Enrollment", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord(' ') and faces is not None and len(faces) > 0:
        aligned_face = recognizer.alignCrop(frame, faces[0])
        feature = recognizer.feature(aligned_face)
        collected_features.append(feature)
        print(f"Sampel {len(collected_features)} diambil.")

        if len(collected_features) >= TARGET_SAMPLES:
            print("Sampel cukup, enrollment selesai.")
            break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if len(collected_features) > 0:
    face_database[person_name] = collected_features
    with open(DB_PATH, "wb") as f:
        pickle.dump(face_database, f)
    print(f"\n'{person_name}' berhasil didaftarkan dengan {len(collected_features)} sampel.")
else:
    print("\nTidak ada sampel yang diambil, enrollment dibatalkan.")