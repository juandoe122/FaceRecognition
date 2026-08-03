# Face Recognition Attendance System

A learning project in Computer Vision & OpenCV — built step by step as a portfolio 
piece, with each stage documented as a development journal (see the `docs/` folder).

## 🚧 Status
**Prototype v0.2 — Face Recognition Core (YuNet + SFace): DONE ✅**

Attendance logging, Excel export, GUI, a relational database, and login are not yet 
built — planned for the next development phase.

## 🎯 Features
- [x] Webcam capture
- [x] Face detection — Haar Cascade *(legacy)* → **YuNet (deep learning)**
- [x] Face recognition — LBPH *(legacy)* → **SFace (deep learning embedding)**
- [x] Face enrollment (a few samples per person, instead of hundreds of photos)
- [x] Face database management (view, delete, reset)
- [x] Realtime face recognition with name and confidence score display

## 🧠 Current Architecture
| Component | Model | Type |
|---|---|---|
| Face Detection | YuNet | Pre-trained CNN (built into OpenCV) |
| Face Recognition | SFace | Pre-trained CNN, outputs a 128-d embedding |
| Data storage | `face_database.pkl` | Feature vectors per person (no photos stored) |

> This project originally started with **Haar Cascade + LBPH** (see `src/legacy/`), 
> then was upgraded to **YuNet + SFace** after discovering Haar Cascade's limitations 
> in detecting tilted/turned faces. The full history is documented in `docs/`.

## 🛠️ Tech Stack
- Python
- OpenCV (`opencv-contrib-python`)
- NumPy, Pillow
- Models: YuNet & SFace (OpenCV Zoo, ONNX format)
