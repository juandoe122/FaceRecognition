import pickle
import os

DB_PATH = "trainer/face_database.pkl"

def load_database():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)
    return {}

def save_database(db):
    with open(DB_PATH, "wb") as f:
        pickle.dump(db, f)

def list_people(db):
    if not db:
        print("Database kosong.")
        return
    print(f"\nTotal orang terdaftar: {len(db)}")
    for name, features in db.items():
        print(f"  - {name} ({len(features)} sampel)")

def delete_person(db, name):
    if name in db:
        del db[name]
        save_database(db)
        print(f"'{name}' berhasil dihapus dari database.")
    else:
        print(f"'{name}' tidak ditemukan di database.")

if __name__ == "__main__":
    db = load_database()

    print("=== Kelola Database Wajah ===")
    print("1. Lihat daftar orang terdaftar")
    print("2. Hapus orang tertentu")
    print("3. Hapus SEMUA data (reset database)")

    choice = input("Pilih menu (1/2/3): ")

    if choice == "1":
        list_people(db)

    elif choice == "2":
        list_people(db)
        name_to_delete = input("\nMasukkan nama yang mau dihapus: ")
        delete_person(db, name_to_delete)

    elif choice == "3":
        confirm = input("Yakin mau hapus SEMUA data? (ketik 'ya' untuk konfirmasi): ")
        if confirm.lower() == "ya":
            save_database({})
            print("Database berhasil direset.")
        else:
            print("Dibatalkan.")

    else:
        print("Pilihan tidak valid.")