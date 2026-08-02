# Commit 8: Upgrade Face Detector ke YuNet (DNN)

## Apa yang dilakukan
- Menambahkan `src/face_detection_yunet.py` sebagai implementasi face detection 
  menggunakan model deep learning YuNet (`cv2.FaceDetectorYN`)
- Model `.onnx` disimpan di `src/models/face_detection_yunet_2023mar.onnx`
- Dibuat sebagai file terpisah untuk membandingkan langsung dengan Haar Cascade 
  (`face_detection.py`) sebelum diputuskan untuk menggantikan

## Kenapa upgrade ini dilakukan
Haar Cascade (`haarcascade_frontalface_default.xml`) hanya mampu mendeteksi wajah 
yang menghadap lurus ke kamera (frontal). Saat kepala dimiringkan atau menoleh 
sedikit, deteksi langsung gagal (kotak wajah hilang). Ini keterbatasan fundamental 
dari algoritma tersebut karena berbasis pola kontras statis, bukan pembelajaran 
fitur wajah yang lebih general.

## Apa yang dipelajari
- Perbedaan Haar Cascade (statistical, klasik) vs YuNet (deep learning/CNN modern)
- YuNet jauh lebih robust terhadap rotasi kepala, tilt, dan variasi pencahayaan
- Cara kerja `cv2.FaceDetectorYN`: perlu `setInputSize()` sesuai dimensi frame asli, 
  parameter `score_threshold` dan `nms_threshold` untuk mengatur sensitivitas deteksi
- Output YuNet berbeda dari Haar Cascade: mengembalikan `None` jika tidak ada wajah 
  terdeteksi (bukan list kosong), dan setiap deteksi menyertakan confidence score
- Sempat riset perbandingan dengan model lain (SCRFD) — SCRFD punya akurasi lebih 
  tinggi di kasus ekstrem (wajah kecil/ramai), tapi butuh implementasi manual 
  (anchor decoding, NMS) yang jauh lebih kompleks. YuNet dipilih karena built-in 
  di OpenCV dan cukup akurat untuk use case single-face real-time ini

## Kendala
---

## Cara menjalankan
```bash
python src/face_detection_yunet.py
```
Tekan `q` untuk keluar.