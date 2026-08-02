# Commit 3: Webcam Capture

## Apa yang dilakukan
- Membuat script `src/webcam_test.py` untuk membuka webcam dan menampilkan live feed
- Menggunakan `cv2.VideoCapture()` untuk akses webcam, loop `while True` untuk membaca frame terus-menerus
- Program bisa dihentikan dengan aman menggunakan tombol 'q'

## Apa yang dipelajari
- Video = kumpulan frame (gambar diam) yang ditampilkan berurutan, ditampilkan cepat 
  sehingga terlihat seperti gerakan
- Fungsi `cap.read()` mengembalikan dua nilai: status berhasil/tidak (`ret`) dan 
  gambar frame itu sendiri (`frame`)
- Pentingnya `cap.release()` dan `cv2.destroyAllWindows()` untuk melepas resource 
  webcam setelah selesai dipakai
- Kenapa harus keluar program lewat tombol keyboard ('q'), bukan klik tombol X 
  di window — supaya `cap.release()` benar-benar terpanggil dan webcam gak 
  "tersangkut" dipakai program
- Hanya 1 aplikasi yang bisa mengakses webcam dalam satu waktu — kalau ada aplikasi 
  lain (Zoom, Teams, dll) yang masih pegang kamera, OpenCV gagal membaca frame

## Kendala
Sempat dapat error "Gagal membaca frame dari webcam" (MSMF error di terminal). 
Setelah dicek, penyebabnya kamera sedang dipakai oleh aplikasi lain di background. 
Setelah aplikasi itu ditutup, script berhasil jalan normal tanpa perlu mengubah kode.

## Cara menjalankan
```bash
python src/webcam_test.py
```
Tekan `q` untuk keluar dari program.