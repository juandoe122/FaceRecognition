# Commit 1: Initial Project Setup

## Apa yang dilakukan
- Membuat repository GitHub baru
- Menyusun struktur folder: `dataset/`, `trainer/`, `src/`, `docs/`
- Menambahkan `.gitkeep` di folder `dataset/` dan `trainer/` (karena masih kosong, 
  dan Git tidak bisa men-track folder kosong)
- Menyesuaikan `.gitignore` agar isi `dataset/` dan `trainer/` tidak ikut ter-commit 
  (karena berisi data foto & model, bukan kode)
- Membuat `requirements.txt` (masih kosong, akan diisi di Commit 2)
- Memperbaiki typo di README

## Apa yang dipelajari
- Perbedaan folder tracked vs untracked di Git
- Kenapa data mentah (foto, model) sebaiknya tidak masuk version control
- Cara kerja `git status`, `git add`, `git commit`, `git push`
- Pentingnya `git config user.name` & `user.email` untuk identitas commit
- (tambahin sendiri kalau ada insight lain dari sesi ini)

## Kendala
- Sempat salah struktur folder (ada folder nested duplikat karena kesalahan saat clone)
- Sempat lupa set identitas Git (`user.name`/`user.email`) di laptop baru

## Struktur project saat ini
```
FaceRecognition/
├── dataset/
├── trainer/
├── src/
├── docs/
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```