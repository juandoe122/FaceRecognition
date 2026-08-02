import cv2
import os

face_cascade = cv2.CascadeClassifier('src/cascades/haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: File cascade tidak ditemukan atau gagal di-load")
    exit()

face_id = input("Masukkan ID user (angka, contoh: 1): ")
face_name = input("Masukkan nama user (untuk referensi kamu sendiri): ")

os.makedirs("dataset", exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam")
    exit()

print(f"\nMulai mengambil foto untuk {face_name} (ID: {face_id})")
print("Lihat ke kamera dari berbagai sudut. Tekan 'q' untuk berhenti lebih awal.\n")

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Gagal membaca frame dari webcam")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        count += 1

        face_img = gray[y:y + h, x:x + w]

        filename = f"dataset/User.{face_id}.{count}.jpg"
        cv2.imwrite(filename, face_img)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, f"Foto: {count}/100", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Dataset Collection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif count >= 100:
        print("\nSelesai! 100 foto berhasil diambil.")
        break

cap.release()
cv2.destroyAllWindows()