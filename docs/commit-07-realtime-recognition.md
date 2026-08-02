# Commit 7: Realtime Face Recognition

## Apa yang dilakukan
- Membuat script `src/recognize.py` yang menggabungkan deteksi wajah + model LBPH terlatih
- Program membaca webcam, mendeteksi wajah, memprediksi identitas menggunakan `trainer.yml`
- Menampilkan nama dan skor confidence secara realtime di atas kotak wajah
- Wajah dengan confidence di atas threshold ditampilkan sebagai "Unknown"

## Apa yang dipelajari
- Alur inference lengkap: detect → crop → predict → map ID ke nama
- `recognizer.predict()` mengembalikan ID prediksi dan confidence score (jarak, 
  bukan persentase — semakin kecil semakin mirip)
- Pentingnya threshold untuk menangani wajah yang tidak dikenal (mencegah model 
  "maksa" menebak salah satu ID yang ada di dataset)
- Penggunaan dictionary Python (`.get()` dengan default value) untuk mapping ID ke nama

## Hasil observasi
- Confidence score untuk wajah sendiri (menghadap kamera jelas): sekitar [ISI ANGKA KAMU]
- Threshold yang digunakan: 70

## Kendala
---

## Cara menjalankan
```bash
python src/recognize.py
```
Pastikan `trainer/trainer.yml` sudah ada (hasil Commit 6), dan sesuaikan dictionary 
`names` dengan ID & nama yang digunakan saat Dataset Collection.