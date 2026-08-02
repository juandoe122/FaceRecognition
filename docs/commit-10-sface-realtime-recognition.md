# Commit 10: Realtime Face Recognition dengan SFace

## Apa yang dilakukan
- Membuat `src/recognize_sface.py` yang menggabungkan YuNet (detection) + SFace (recognition)
- Wajah yang terdeteksi di-align, diekstrak feature vector-nya, lalu dibandingkan 
  dengan seluruh database menggunakan cosine similarity
- Kotak hijau untuk wajah dikenali, kotak merah untuk "Unknown"
- Skor cosine similarity ditampilkan realtime di atas kotak wajah

## Apa yang dipelajari
- Alur lengkap pipeline modern: detect (YuNet) → align → extract feature (SFace) → 
  compare (cosine similarity) → keputusan identitas
- `recognizer.match()` dengan `FR_COSINE` mengukur kemiripan dua feature vector; 
  threshold standar 0.363 sesuai rekomendasi OpenCV
- Strategi membandingkan wajah baru ke seluruh sampel tersimpan per orang, mengambil 
  skor tertinggi sebagai representasi kemiripan
- Kotak deteksi tetap stabil meskipun kepala menoleh/miring, berkat YuNet — 
  menyelesaikan masalah yang dialami dengan Haar Cascade sebelumnya
- Kompleksitas pencarian (nested loop membandingkan ke semua sampel) masih sederhana 
  dan cukup untuk skala kecil, namun perlu dioptimasi jika jumlah orang terdaftar 
  bertambah banyak di kemudian hari

## Kendala
---

## Cara menjalankan
```bash
python src/recognize_sface.py
```
Pastikan sudah ada minimal 1 orang terdaftar lewat `enroll_face.py` sebelum menjalankan ini.