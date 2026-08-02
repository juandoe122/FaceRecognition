# Commit 4: Face Detection

## Apa yang dilakukan
- Membuat script `src/face_detection.py` untuk mendeteksi wajah secara realtime dari webcam
- Menggunakan Haar Cascade Classifier (`haarcascade_frontalface_default.xml`) bawaan OpenCV
- Menggambar kotak biru di sekitar wajah yang terdeteksi

## Apa yang dipelajari
- Haar Cascade adalah pre-trained model klasik computer vision (bukan deep learning) 
  yang mengenali wajah berdasarkan pola kontras terang-gelap
- Konsep "inference" (memakai model yang sudah dilatih) vs "training" (melatih model dari nol)
- Kenapa gambar perlu di-convert ke grayscale sebelum deteksi (Haar Cascade tidak 
  memakai informasi warna, hanya kontras)
- Parameter `detectMultiScale`: scaleFactor, minNeighbors, minSize dan pengaruhnya 
  terhadap akurasi deteksi
- OpenCV menggunakan format warna BGR, bukan RGB

## Kendala
- OpenCV versi 5.0.0 yang terinstall ternyata tidak menyertakan file-file Haar Cascade 
  di folder `cv2.data.haarcascades` (folder tersebut kosong, hanya berisi `__init__.py`). 
  Solusi: download manual file `haarcascade_frontalface_default.xml` dari repository 
  resmi OpenCV di GitHub, simpan di `src/cascades/`, lalu load menggunakan path lokal.
- Sempat menjalankan script menggunakan Python interpreter global (bukan dari venv) 
  lewat tombol Run VS Code, menyebabkan `AttributeError`. Solusi: jalankan manual 
  lewat terminal dengan venv aktif.

## Cara menjalankan
```bash
python src/face_detection.py
```
Tekan `q` untuk keluar.