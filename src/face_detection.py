import cv2

face_cascade = cv2.CascadeClassifier('src/cascades/haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: File cascade tidak ditemukan atau gagal di-load")
    exit()

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

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()