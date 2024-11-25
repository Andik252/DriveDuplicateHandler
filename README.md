# Google Drive Duplicate File Remover

## Deskripsi
Program ini dirancang untuk **mendeteksi file duplikat di Google Drive berdasarkan nama file**. Program ini memindai **semua folder** di **My Drive**, termasuk folder yang di-share atau yang dipindahkan sebagai shortcut ke My Drive. Setelah mendeteksi file duplikat, program akan memilih **file yang terlama diupload** dan **mengeluarkan file lainnya dari folder** (tetapi file tersebut tetap ada di Google Drive pengguna, hanya tidak ada lagi di folder tersebut).

### Fitur Utama:
- Mendeteksi **file duplikat berdasarkan nama file** di seluruh folder dan subfolder di Google Drive.
- Mengidentifikasi folder yang dibagikan dan folder pintasan yang dipindahkan ke My Drive.
- **Mengeluarkan file duplikat dari folder** dan hanya menyisakan **1 file yang terlama diupload** (file yang dikeluarkan tetap ada di Google Drive).
- Menyediakan opsi untuk mengunduh hasil deteksi duplikat dalam file teks.

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
- **Hati-hati dengan Pengeluaran File**: File yang dikeluarkan dari folder tetap ada di Google Drive Anda, hanya saja tidak lagi berada di folder yang dipilih. Pastikan Anda telah memeriksa file yang ingin diproses sebelum menjalankan skrip.
- **Pembatasan API Google Drive**: Google Drive API memiliki pembatasan jumlah permintaan per detik. Jika Anda memiliki banyak file untuk diproses, pastikan untuk menangani rate limiting sesuai dengan kebijakan API.
