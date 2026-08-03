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
PHOTOS_DIR = "enroll_photos"

os.makedirs("trainer", exist_ok=True)

if os.path.exists(DB_PATH):
    with open(DB_PATH, "rb") as f:
        face_database = pickle.load(f)
else:
    face_database = {}

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")

person_folders = [f for f in os.listdir(PHOTOS_DIR) if os.path.isdir(os.path.join(PHOTOS_DIR, f))]

if len(person_folders) == 0:
    print(f"No Folder found in enroll_photos'{PHOTOS_DIR}/'")
    exit()

print("=== Folder found in enroll_photos/ ===")
for i, name in enumerate(person_folders, start=1):
    print(f"{i}. {name}")
print(f"{len(person_folders) + 1}. Process ALL folders")

choice = input("\nChoose the folder number to process: ")

try:
    choice_num = int(choice)
except ValueError:
    print("Input is not valid, must be a number.")
    exit()

if choice_num == len(person_folders) + 1:
    selected_folders = person_folders
elif 1 <= choice_num <= len(person_folders):
    selected_folders = [person_folders[choice_num - 1]]
else:
    print("The number is invalid.")
    exit()

print(f"\nprocessing: {selected_folders}\n")

for person_name in selected_folders:
    person_path = os.path.join(PHOTOS_DIR, person_name)
    image_files = [f for f in os.listdir(person_path) if f.lower().endswith(VALID_EXTENSIONS)]

    print(f"--- Processing '{person_name}' ({len(image_files)} images) ---")

    features = []

    for filename in image_files:
        img_path = os.path.join(person_path, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"  [SKIP] '{filename}': failed to read (corrupt file/format not supported)")
            continue

        h, w = img.shape[:2]
        detector.setInputSize((w, h))

        _, faces = detector.detect(img)

        if faces is None or len(faces) == 0:
            print(f"  [SKIP] '{filename}': no face detected")
            continue

        if len(faces) > 1:
            print(f"  [SKIP] '{filename}': {len(faces)} faces detected, ambiguous (must be 1 face per image)")
            continue

        aligned_face = recognizer.alignCrop(img, faces[0])
        feature = recognizer.feature(aligned_face)
        features.append(feature)
        print(f"  [OK] '{filename}': face successfully extracted ({len(features)}/{len(image_files)})")

    if len(features) > 0:
        face_database[person_name] = features
        print(f"  -> '{person_name}' has {len(features)} valid samples\n")
    else:
        print(f"  -> '{person_name}' is NOT registered, no valid photos\n")

with open(DB_PATH, "wb") as f:
    pickle.dump(face_database, f)

print("database updated successfully.")