# Commit 5: Dataset Collection

## Apa yang dilakukan
- Membuat script `src/dataset_collection.py` untuk mengambil foto wajah dari webcam
- Wajah yang terdeteksi di-crop, dikonversi ke grayscale, lalu disimpan ke folder `dataset/`
- Format nama file: `User.<id>.<nomor_foto>.jpg` untuk membedakan tiap orang
- Program otomatis berhenti setelah 100 foto (atau tekan 'q' untuk berhenti manual)

## Apa yang dipelajari
- Konsep dataset dalam machine learning: butuh banyak variasi contoh (pose, sudut, 
  ekspresi) supaya model belajar mengenali "range" wajah seseorang, bukan cuma 1 pose statis
- Teknik cropping gambar menggunakan NumPy array slicing (`gray[y:y+h, x:x+w]`)
- Pentingnya sistem penamaan file yang konsisten untuk menandai kepemilikan data (ID per orang)
- Kenapa folder `dataset/` sengaja di-ignore dari git (data personal, tidak boleh 
  masuk repository publik)

## Kendala
---

## Cara menjalankan
```bash
python src/dataset_collection.py
```
Ikuti instruksi di terminal untuk memasukkan ID dan nama, lalu gerakkan kepala 
perlahan ke berbagai sudut selama proses capture.