# Google Drive Duplicate File Remover

## Deskripsi
Program ini **mendeteksi file duplikat berdasarkan nama file** di Google Drive Anda. Program akan memindai semua folder di **My Drive**, termasuk folder yang di-share dan dipindahkan ke **My Drive** sebagai shortcut. Skrip ini membaca seluruh folder dan subfolder secara rekursif untuk mencari file dengan nama yang sama.

Setelah mendeteksi file duplikat, program hanya akan menyisakan **satu file yang terlama di-upload**, dan file lainnya akan **dikeluarkan dari folder**. Penting untuk dicatat bahwa file yang dikeluarkan dari folder akan tetap ada di Google Drive Anda, hanya saja tidak lagi ada di folder yang dipilih.

### Fitur Utama:
- Mendeteksi file duplikat berdasarkan nama file.
- Memindai seluruh folder dan subfolder di Google Drive.
- Mendukung folder pintasan yang dipindahkan ke My Drive.
- Mengeluarkan file duplikat dari folder, menyisakan hanya satu file (yang terlama di-upload).
- Memberikan opsi untuk mengunduh hasil output dalam file teks.

## Cara Instalasi dan Menjalankan Program

### 1. Ambil Skrip Python
Unduh skrip Python `script.py` langsung dari repositori GitHub dengan menggunakan URL raw:
```bash
wget https://raw.githubusercontent.com/username/repository-name/main/script.py
```

### 2. Jalankan Program
Setelah skrip diunduh, jalankan program dengan perintah berikut:
```bash
python script.py
```

Program akan meminta Anda untuk mengautentikasi akun Google Anda dan memilih folder dari daftar folder yang ada di Google Drive.

### 3. Pilih Folder
Setelah program berjalan, Anda akan melihat daftar folder di Google Drive Anda. Pilih folder yang ingin Anda periksa dengan memasukkan nama atau nomor folder.

### 4. Proses Deteksi Duplikat
Program akan memindai folder yang dipilih dan mencari file duplikat berdasarkan nama file. File yang terdeteksi sebagai duplikat akan dikeluarkan dari folder, dan hanya satu file yang terlama di-upload yang akan tetap ada di dalam folder.

### 5. Unduh Hasil Output
Setelah proses selesai, program akan memberikan informasi tentang file yang dikeluarkan. Anda akan diberi pilihan untuk mengunduh hasilnya dalam file teks.

## Catatan Penting
- **Hati-hati dengan Penghapusan**: Program tidak benar-benar menghapus file dari Google Drive. File duplikat akan **dikeluarkan dari folder**, tetapi file tersebut akan tetap ada di Google Drive Anda.
- **Pembatasan API Google Drive**: Perhatikan bahwa Google Drive API memiliki batasan pada jumlah permintaan per detik. Jika Anda memiliki banyak file untuk diproses, Anda mungkin akan mengalami pembatasan tersebut.
- **Penggunaan Folder Pintasan**: Program ini juga dapat memindai folder yang dipindahkan ke My Drive sebagai shortcut dan mengakses target dari pintasan tersebut.
