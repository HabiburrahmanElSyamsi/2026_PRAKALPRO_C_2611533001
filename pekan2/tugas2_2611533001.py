from typing import Final

BATAS_LULUS: Final = 76.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3001 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3001 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3001 = int(input("Masukkan Umur : "))
nilai_3001 = float(input("Masukkan Skor Tes Awal : "))

alamat_3001 = """Komplek Graha Sang Pakar,
Kecamatan Padang Timur,
Kota Padang"""

id_token_3001 = 100 + 3j

lulus_3001 = nilai_3001 >= BATAS_LULUS

print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_3001, "| Tipe:", type(nama_3001))
print("Jenis Kelamin :", jenis_kelamin_3001, "| Tipe:", type(jenis_kelamin_3001))
print("Alamat Domisili:")
print(alamat_3001, "| Tipe:", type(alamat_3001))
print("Umur :", umur_3001, "tahun | Tipe:", type(umur_3001))
print("Skor Tes Awal :", nilai_3001, "| Tipe:", type(nilai_3001))
print("ID Token Sinyal:", id_token_3001, "| Tipe:", type(id_token_3001))

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_3001, "| Tipe:", type(lulus_3001))