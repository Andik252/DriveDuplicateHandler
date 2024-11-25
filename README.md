# Google Drive Duplicate File Remover

## Deskripsi  
Program ini **mendeteksi file duplikat berdasarkan nama file** di **My Drive** dan subfoldernya. Program memilih **file yang terlama diupload** dan **mengeluarkan file duplikat dari folder**, namun file yang dikeluarkan tetap ada di Google Drive pengguna.

### Fitur Utama:
- Deteksi duplikat berdasarkan **nama file** di seluruh folder.
- Mengidentifikasi folder berbagi dan pintasan di My Drive.
- **Mengeluarkan file duplikat** dan hanya menyisakan **file yang terlama diupload**.
- Opsi untuk mengunduh hasil deteksi dalam file teks.

## Cara Instalasi dan Menjalankan Program

1. **Unduh Skrip Python**  
   Jalankan perintah berikut:  
   ```bash  
   curl -O https://raw.githubusercontent.com/username/repository-name/refs/heads/main/script.py  
   ```

2. **Jalankan Program**  
   Setelah mengunduh skrip, jalankan dengan perintah:  
   ```bash  
   python script.py  
   ```

3. **Autentikasi Google**  
   Program akan meminta autentikasi Google untuk mengakses Google Drive Anda.

4. **Pilih Folder**  
   Pilih folder yang ingin diproses dengan memasukkan nomor atau nama folder yang muncul setelah autentikasi.

5. **Proses Duplikat**  
   Program akan memindai dan memilih **file yang terlama diupload** dan **mengeluarkan file lainnya** dari folder (file tetap ada di Drive).

6. **Unduh Hasil**  
   Anda akan diberikan opsi untuk mengunduh hasil deteksi duplikat dalam file teks.

## Catatan Penting

1. **File yang Dikeluarkan dari Folder**:  
   - File tidak dihapus, hanya **dikeluarkan dari folder** dan tetap ada di Google Drive.
   - Jika Anda adalah pengunggah, file akan muncul di My Drive Anda.  
   - Untuk file yang diunggah oleh orang lain, file mungkin tidak muncul di My Drive Anda dan akan kembali ke pengunggah asli.

2. **Persiapkan Struktur Folder**:  
   - Program akan memindai semua folder dan subfolder, termasuk folder pintasan.
   - Jika ingin memindai folder tertentu, buat pintasan folder ke My Drive.

3. **Uji Program Terlebih Dahulu**:  
   - Cobalah program pada folder percobaan sebelum digunakan pada folder asli untuk menghindari kesalahan.
