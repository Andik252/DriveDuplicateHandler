# Google Drive Duplicate File Remover

## Deskripsi
Program ini dirancang untuk **mendeteksi file duplikat di Google Drive berdasarkan nama file**. Program ini memindai **semua folder** di **My Drive**, termasuk folder yang di-share atau yang dipindahkan sebagai shortcut ke My Drive. Setelah mendeteksi file duplikat, program akan memilih **file yang terlama diupload** dan **mengeluarkan file lainnya dari folder** (tetapi file tersebut tetap ada di Google Drive pengguna, hanya tidak ada lagi di folder tersebut).

## Cara Instalasi dan Menjalankan Program

### 1. Unduh Skrip Python
Untuk mengunduh skrip Python, jalankan perintah berikut:
```bash
curl -O https://raw.githubusercontent.com/username/repository-name/refs/heads/main/script.py
```

### 2. Jalankan Program
Setelah mengunduh skrip, jalankan program dengan perintah:
```bash
python script.py
```

### 3. Autentikasi Google
Program ini memerlukan autentikasi Google untuk mengakses Google Drive Anda. Program akan meminta Anda untuk login ke akun Google Anda untuk memberikan izin akses.

### 4. Pilih Folder untuk Proses Duplikat
Setelah autentikasi, program akan menampilkan daftar folder di My Drive Anda. Pilih folder untuk diproses dengan memasukkan nomor atau nama folder yang ingin Anda periksa.

### 5. Proses Deteksi Duplikat
Program akan memindai folder dan subfolder untuk mendeteksi file dengan nama yang sama. Jika ada lebih dari satu file duplikat, program akan memilih **file yang terlama diupload** dan **mengeluarkan file lainnya dari folder** (file yang dikeluarkan tetap ada di Google Drive).

### 6. Unduh Hasil
Setelah proses selesai, Anda akan diberikan opsi untuk mengunduh hasil deteksi duplikat dalam bentuk file teks.

## Catatan Penting

1. **File yang Dikeluarkan dari Folder**:  
   - File yang terdeteksi duplikat **tidak akan dihapus**, tetapi hanya **dikeluarkan dari folder**.  
   - File tersebut tetap berada di My Drive Anda. Jika Anda adalah pengunggahnya, file akan muncul di halaman utama My Drive.  
   - Untuk file yang diunggah oleh orang lain atau berasal dari folder berbagi, file mungkin tidak muncul di My Drive Anda dan akan kembali ke My Drive pengunggah asli.  

2. **Persiapkan Struktur Folder**:  
   - Program akan memindai seluruh folder dan subfolder di My Drive, termasuk folder berbagi yang dipindahkan sebagai pintasan.  
   - Jika hanya ingin memindai folder tertentu, buat pintasan folder tersebut ke My Drive sebelum menjalankan program.  

3. **Uji Program Terlebih Dahulu**:  
   - Sebelum digunakan pada folder asli, uji program dengan folder percobaan untuk memastikan hasilnya sesuai dengan harapan. Ini mencegah kesalahan pada file yang penting.  
