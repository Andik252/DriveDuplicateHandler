# Google Drive Duplicate File Cleaner

## Deskripsi

**Google Drive Duplicate File Cleaner** adalah program Python yang dirancang untuk mendeteksi dan menangani file duplikat di Google Drive berdasarkan **nama file**. Program ini membaca semua folder utama dan subfolder di My Drive, termasuk folder berbagi yang telah ditambahkan sebagai pintasan ke My Drive. 

**Fitur Utama**:
1. **Deteksi File Duplikat**: Mengidentifikasi file dengan nama yang sama di folder utama dan subfolder.
2. **Pemilihan File Terlama**: Dari file duplikat yang terdeteksi, program akan memilih satu file yang **terlama diunggah** untuk dipertahankan.
3. **Penghapusan dari Folder**: File lainnya akan **dikeluarkan dari folder** namun tetap tersedia di Google Drive Anda (tidak dihapus permanen).
4. **Kompatibilitas dengan Pintasan**: Program dapat membaca folder berbagi jika telah ditambahkan sebagai pintasan ke My Drive.

Proses ini memastikan setiap nama file hanya muncul sekali dalam setiap folder, menghindari duplikasi dan menjaga keteraturan Google Drive Anda.

## Cara Instalasi dan Penggunaan

### 1. **Kunjungi Google Colab**
Buka [Google Colab](https://colab.research.google.com/) untuk menjalankan program ini. Google Colab memungkinkan Anda menjalankan skrip Python langsung di cloud tanpa perlu pengaturan lokal.

### 2. **Unduh Skrip dengan cURL**
Jalankan perintah berikut di Google Colab untuk mengunduh skrip Python ini dari GitHub:  
```bash
!curl -O https://raw.githubusercontent.com/USERNAME/REPOSITORY/main/script.py
```
### 3. **Jalankan Program**
Setelah skrip diunduh, jalankan program menggunakan perintah berikut:  
```python
!python script.py
```

### 4. **Ikuti Langkah-langkah Berikut**
1. **Login ke Akun Google Drive**: Saat program meminta otentikasi, ikuti petunjuk untuk login.
2. **Pilih Folder untuk Dipindai**: Program akan menampilkan daftar folder utama dan pintasan di My Drive Anda. Pilih folder dengan mengetikkan nomor atau nama folder.
3. **Proses File Duplikat**: Program akan memindai folder dan subfolder, mendeteksi file duplikat berdasarkan nama, memilih file terlama untuk dipertahankan, dan mengeluarkan file lain dari folder.
4. **Unduh Laporan (Opsional)**: Setelah proses selesai, Anda dapat mengunduh laporan hasil scan sebagai file teks.

## Catatan Penting
