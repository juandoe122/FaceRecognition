# Commit 6: Train Face Recognition

## Apa yang dilakukan
- Membuat script `src/train_model.py` untuk melatih model LBPH menggunakan dataset foto wajah
- Membaca semua foto dari `dataset/`, mengekstrak ID dari nama file
- Melatih `cv2.face.LBPHFaceRecognizer` dengan pasangan (gambar wajah, ID)
- Menyimpan hasil model terlatih ke `trainer/trainer.yml`

## Apa yang dipelajari
- Proses training LBPH: setiap foto dianalisis pola teksturnya, dipetakan ke sebuah 
  ID, lalu "dihafal" dalam bentuk model
- Perbedaan antara data mentah (foto di `dataset/`) dan hasil model (`trainer.yml`) 
  — model adalah representasi hasil belajar, bukan salinan foto itu sendiri
- List comprehension di Python untuk filter file berdasarkan ekstensi
- Parsing nama file untuk ekstraksi metadata (ID) menggunakan `.split('.')`
- Kenapa hasil training (`trainer.yml`) tidak perlu di-commit ke git — karena bisa 
  di-generate ulang dari dataset kapan saja

## Kendala
- (isi sesuai pengalaman kamu)

## Cara menjalankan
```bash
python src/train_model.py
```
Pastikan folder `dataset/` sudah berisi foto (hasil dari Commit 5) sebelum menjalankan ini.