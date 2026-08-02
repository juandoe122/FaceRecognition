# Commit 2: Install OpenCV Environment

## Apa yang dilakukan
- Membuat virtual environment (`venv`) untuk isolasi dependencies
- Install `opencv-contrib-python`, `numpy`, `pillow`
- Generate `requirements.txt` dengan `pip freeze`

## Apa yang dipelajari
- Kenapa virtual environment penting (isolasi dependency antar project)
- Kenapa pakai `opencv-contrib-python` bukan `opencv-python` biasa 
  (butuh modul `cv2.face` untuk LBPH face recognizer nanti)
- Perbandingan singkat algoritma face recognition: LBPH vs deep learning 
  (`face_recognition`/dlib) — memilih LBPH dulu untuk fase belajar fundamental
- Masalah encoding UTF-16 vs UTF-8 saat redirect output di PowerShell

## Kendala
- `pip freeze > requirements.txt` di PowerShell menghasilkan file corrupt 
  (byte NUL di antara karakter) karena default encoding PowerShell adalah UTF-16.
  Solusi: pakai `Out-File -Encoding utf8` 

## Library terinstall
- opencv-contrib-python==5.0.0.93
- numpy==2.5.1
- pillow==12.3.0