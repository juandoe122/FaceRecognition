# Commit 11: Batch Enrollment dari File Gambar

## Apa yang dilakukan
- Menambahkan `src/enroll_from_images.py` untuk mendaftarkan wajah dari file foto 
  (bukan hanya webcam), dikelompokkan berdasarkan nama folder di `enroll_photos/`
- Menambahkan menu interaktif untuk memilih folder mana yang ingin diproses 
  (satu orang tertentu atau semua sekaligus)
- Menambahkan validasi per foto: skip jika file gagal dibaca, tidak ada wajah 
  terdeteksi, atau ada lebih dari satu wajah (ambigu)
- Menaikkan jumlah sampel enrollment webcam dari 5 menjadi 20 (`TARGET_SAMPLES` 
  di `enroll_face.py`) untuk meningkatkan robustness pengenalan

## Apa yang dipelajari
- YuNet dan SFace tidak peduli sumber gambar (webcam vs file) karena keduanya 
  sama-sama diproses sebagai array NumPy setelah dibaca
- Perbedaan penting antara webcam dan file gambar: ukuran frame webcam konsisten 
  (`setInputSize()` cukup sekali), sedangkan file gambar bisa berbeda ukuran 
  sehingga `setInputSize()` harus dipanggil ulang per file
- Pentingnya validasi input saat memproses data dari luar (file rusak, tanpa 
  wajah, atau ambigu/banyak wajah) menggunakan `continue` untuk skip tanpa 
  menghentikan keseluruhan proses
- `enumerate(list, start=1)` untuk membuat menu bernomor secara dinamis
- Perbedaan `*` vs `**` di `.gitignore`: `*` hanya mencakup isi level pertama 
  folder, sedangkan `**` menembus semua subfolder di dalamnya — penting untuk 
  folder dengan struktur bersarang seperti `enroll_photos/<nama>/<foto>.jpg`

## Kendala
---

## Cara menjalankan
```bash
python src/enroll_from_images.py
```
Siapkan foto di `enroll_photos/<nama_orang>/`, satu folder per orang, sebelum menjalankan.