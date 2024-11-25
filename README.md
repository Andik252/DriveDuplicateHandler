# Google Drive Duplicate File Remover

## Deskripsi
Program ini dirancang untuk mendeteksi dan menghapus file duplikat di Google Drive berdasarkan nama file. Program ini memindai **semua folder** yang ada di **My Drive**, termasuk folder yang di-share dan dipindahkan ke **My Drive** sebagai shortcut. Program akan memindai folder utama dan subfolder secara rekursif untuk mencari file yang memiliki nama yang sama. 

Setelah mendeteksi file duplikat, program akan memilih hanya **1 file yang terlama di-upload** dan mengeluarkan file lainnya dari folder tersebut. Ini dilakukan untuk menghindari adanya beberapa file duplikat dengan nama yang sama di dalam satu folder atau subfolder. Program juga menyediakan opsi bagi pengguna untuk mengunduh hasil outputnya dalam bentuk file teks.

### Fitur Utama:
- Mendeteksi file duplikat di seluruh folder dan subfolder di Google Drive.
- Mengidentifikasi folder yang dipindahkan sebagai shortcut ke My Drive.
- Menghapus duplikat berdasarkan nama file, hanya menyisakan satu file (yang terlama diupload).
- Mendukung folder yang dibagikan dan folder pintasan.
- Menyediakan opsi untuk mengunduh hasil deteksi duplikat dalam file teks.

## Cara Instalasi

### 1. Clone Repositori
Clone repositori ini ke dalam direktori lokal Anda:
```bash
git clone https://github.com/username/repository-name.git
```

### 2. Instalasi Dependensi
Skrip ini memerlukan beberapa pustaka Python, seperti `google-auth`, `google-api-python-client`, dan `google-colab`. Instal dependensi tersebut dengan menjalankan perintah berikut:
```bash
pip install --upgrade google-auth google-api-python-client google-colab
```

### 3. Autentikasi Google
Program ini membutuhkan autentikasi Google untuk mengakses Google Drive Anda. Pastikan Anda sudah memiliki akses ke Google Drive dan dapat mengautentikasi melalui akun Google Anda. Program ini menggunakan `google.colab.auth` untuk autentikasi.

### 4. Menyiapkan dan Menjalankan Program
Setelah dependensi diinstal dan autentikasi selesai, Anda bisa menjalankan skrip dengan langkah berikut:
```bash
python script.py
```

Program akan meminta Anda untuk memilih folder dari daftar folder yang ada di My Drive. Pilih folder yang ingin Anda periksa untuk file duplikat, dan program akan mulai memindai dan mengelola file duplikat.

## Cara Kerja Program

1. **Mendapatkan Daftar Folder**: Program pertama-tama akan mendaftar semua folder dan pintasan di My Drive, kecuali folder yang dikecualikan (seperti "Colab Notebooks").
   
2. **Memindai Folder dan Subfolder**: Setelah memilih folder, program akan memindai folder utama dan seluruh subfolder secara rekursif untuk mencari file dengan nama yang sama.

3. **Mendeteksi File Duplikat**: Program kemudian akan mengidentifikasi file duplikat berdasarkan nama. Jika ada lebih dari satu file dengan nama yang sama, program akan memilih file yang terlama diupload dan mengeluarkan file lainnya dari folder.

4. **Menghapus Duplikat**: File yang terdeteksi sebagai duplikat selain file yang terlama akan dipindahkan keluar dari folder yang dipilih.

5. **Menyimpan Hasil dan Unduh**: Setelah proses selesai, program akan menunjukkan hasil dan memberikan opsi untuk mengunduh file teks yang berisi hasil dari proses penghapusan file duplikat.

## Cara Menjalankan Program

1. **Jalankan Program**:
   Setelah mengikuti langkah instalasi, jalankan skrip dengan:
   ```bash
   python script.py
   ```

2. **Autentikasi dan Pilih Folder**:
   - Program akan meminta Anda untuk memilih folder dari daftar folder di Google Drive.
   - Masukkan nomor atau nama folder yang ingin Anda proses.

3. **Proses Deteksi Duplikat**:
   - Program akan memindai folder dan subfolder untuk mendeteksi file duplikat berdasarkan nama.
   - File yang duplikat akan dikeluarkan dari folder dan hanya menyisakan file yang terlama diupload.

4. **Unduh Hasil Output**:
   - Setelah proses selesai, Anda akan diberi pilihan untuk mengunduh hasilnya dalam bentuk file teks yang berisi informasi file yang dikeluarkan.

## Catatan Penting
- **Hati-hati dengan Penghapusan**: Skrip ini akan menghapus file duplikat yang ditemukan. Pastikan untuk memeriksa dengan cermat file yang ada di folder sebelum menjalankan skrip.
- **Pembatasan API Google Drive**: API Google Drive memiliki batasan permintaan per detik. Jika Anda memiliki banyak file untuk diproses, pastikan untuk menangani rate limiting sesuai dengan kebijakan API.
- **Penggunaan Folder Pintasan**: Program ini juga dapat memindai folder yang dipindahkan ke My Drive sebagai shortcut dan mengakses target dari pintasan tersebut.
