import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

face_cascade = cv2.CascadeClassifier('src/cascades/haarcascade_frontalface_default.xml')

names = {
    1: "rafly",
}

CONFIDENCE_THRESHOLD = 70

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak bisa membuka webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Gagal membaca frame dari webcam")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]

        id_pred, confidence = recognizer.predict(face_roi)

        if confidence < CONFIDENCE_THRESHOLD:
            name = names.get(id_pred, "Unknown")
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        label = f"{name} ({round(confidence, 1)})"
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()