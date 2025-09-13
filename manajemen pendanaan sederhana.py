judul= input("Masukkan Judul Buku: ") #input data 
nama= input("Masukkan Nama Peminjam: ") #'
hari= int(input("Berapa Hari Peminjaman?: ")) #input tipe data integer

harga= 2000 #variable untuk harga peminjaman per harinya
biaya= hari*harga #ini rumus perhitungan biaya total 

print("\n=== Rincian Peminjaman ===") #Tampilan output seperti struk peminjaman bukunya
print(f"Judul Buku     : {judul}")
print(f"Nama Peminjam  : {nama}")
print(f"Lama Peminjaman: {hari} hari")
print(f"Total Biaya    : Rp {biaya:,}")
print("\n==========================")