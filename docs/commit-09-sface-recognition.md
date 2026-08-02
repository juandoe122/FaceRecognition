# Commit 9: Upgrade Face Recognition ke SFace

## Apa yang dilakukan
- Menambahkan `src/enroll_face.py` untuk mendaftarkan wajah baru menggunakan SFace 
  (menggantikan pendekatan LBPH lama yang butuh ~100 foto per orang)
- Menambahkan `src/manage_database.py` untuk mengelola database wajah (lihat daftar, 
  hapus orang tertentu, reset database)
- Model `face_recognition_sface_2021dec.onnx` disimpan di `src/models/`
- Data enrollment disimpan sebagai feature vector (bukan foto) di `trainer/face_database.pkl`

## Kenapa upgrade ini dilakukan
LBPH memerlukan banyak foto (~100) per orang dan akurasinya terbatas terhadap variasi 
pose/pencahayaan. SFace adalah model deep learning yang jauh lebih akurat, hanya 
memerlukan beberapa sampel foto per orang, dan didesain untuk bekerja langsung dengan 
YuNet (memakai landmark wajah dari YuNet untuk proses alignment).

## Apa yang dipelajari
- Perbedaan paradigma "training model klasifikasi" (LBPH) vs "membandingkan feature 
  vector / embedding" (SFace) — dikenal sebagai pendekatan few-shot recognition
- Fungsi `alignCrop()`: meluruskan wajah berdasarkan 5 titik landmark sebelum ekstraksi 
  fitur, penting untuk akurasi SFace
- Fungsi `feature()`: mengekstrak representasi numerik (128-dimensi) dari wajah yang 
  sudah di-align
- Penggunaan `pickle` untuk menyimpan dan memuat struktur data Python (dictionary berisi 
  array NumPy) ke/dari file
- Mendesain "database" sederhana sendiri dari nol (load, save, delete) menggunakan dictionary
- SFace tidak menyimpan foto asli, hanya representasi numerik — lebih ramah privasi 
  dibanding pendekatan dataset foto sebelumnya

## Kendala
---

## Cara menjalankan
```bash
# Mendaftarkan wajah baru
python src/enroll_face.py

# Melihat/menghapus data terdaftar
python src/manage_database.py
```