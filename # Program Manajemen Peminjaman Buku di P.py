# Program Manajemen Peminjaman Buku di Perpustakaan
# Dibuat untuk memenuhi tugas: sistem manajemen sederhana perpustakaan sekolah

# Tetapkan biaya peminjaman per hari (Rp 2000)
BIAYA_PER_HARI = 2000
# Tetapkan batas maksimum hari peminjaman
BATAS_HARI = 30

# Variabel untuk menyimpan total biaya semua buku
total_biaya_semua = 0

print("=== Sistem Peminjaman Buku Perpustakaan ===")

# Meminta jumlah buku yang ingin dipinjam
jumlah_buku = int(input("Masukkan jumlah buku yang ingin dipinjam: "))

# Perulangan untuk setiap buku
for i in range(jumlah_buku):
    print(f"\n--- Data Buku ke-{i+1} ---")
    
    # Input judul buku
    judul_buku = input("Masukkan judul buku: ")
    # Input nama peminjam
    nama_peminjam = input("Masukkan nama peminjam: ")
    
    # Validasi agar jumlah hari harus angka positif
    while True:
        try:
            hari = int(input("Masukkan jumlah hari peminjaman: "))
            if hari <= 0:
                print("⚠ Jumlah hari harus angka positif! Silakan coba lagi.")
                continue
            break
        except ValueError:
            print("⚠ Input tidak valid! Masukkan angka yang benar.")
    
    # Cek apakah melebihi batas hari
    if hari > BATAS_HARI:
        print(f"⚠ Jumlah hari peminjaman tidak boleh lebih dari {BATAS_HARI} hari!")
        hari = BATAS_HARI  # otomatis dibatasi ke maksimum
    
    # Hitung total biaya peminjaman buku ini
    total_biaya = hari * BIAYA_PER_HARI
    total_biaya_semua += total_biaya  # tambahkan ke total semua buku
    
    # Tampilkan hasil peminjaman
    print("\n=== Rincian Peminjaman ===")
    print(f"Judul Buku     : {judul_buku}")
    print(f"Nama Peminjam  : {nama_peminjam}")
    print(f"Lama Peminjaman: {hari} hari")
    print(f"Total Biaya    : Rp {total_biaya:,}")  # format angka pakai koma

# Tampilkan total keseluruhan biaya semua buku
print("\n=== Total Biaya Semua Buku ===")
print(f"Total Biaya Keseluruhan: Rp {total_biaya_semua:,}")
print("=== Terima kasih sudah menggunakan sistem ini! ===")
