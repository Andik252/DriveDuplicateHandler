# Google Drive Duplicate File Remover  

## Deskripsi  
Program ini **mendeteksi file duplikat di Google Drive berdasarkan nama file**. Program memindai **semua folder** di **My Drive**, termasuk folder yang di-share atau yang dipindahkan sebagai shortcut. Setelah mendeteksi duplikat, hanya **file yang terlama diupload** yang akan tetap di folder, sementara file lainnya akan **dikeluarkan dari folder** (tetap ada di Google Drive).  

### Fitur Utama:  
- Mendeteksi duplikat berdasarkan **nama file** di seluruh folder dan subfolder.  
- Mengidentifikasi folder yang dibagikan dan pintasan yang dipindahkan ke My Drive.  
- Mengeluarkan duplikat dari folder, menyisakan **1 file yang terlama diupload** (file tetap ada di Google Drive).  
- Menyediakan opsi untuk mengunduh hasil dalam file teks.  

## Cara Instalasi dan Menjalankan Program  

### 1. Unduh Skrip Python  
Jalankan perintah berikut untuk mengunduh skrip Python:  
```bash  
curl -O https://raw.githubusercontent.com/username/repository-name/refs/heads/main/script.py  
```  

### 2. Jalankan Program  
Setelah mengunduh skrip, jalankan program dengan perintah:  
```bash  
python script.py  
```  

### 3. Autentikasi Google  
Login ke akun Google untuk memberi izin akses ke Google Drive Anda.  

### 4. Pilih Folder untuk Proses Duplikat  
Program akan menampilkan daftar folder My Drive. Pilih folder untuk diproses dengan memasukkan nomor atau nama folder.  

### 5. Proses Deteksi Duplikat  
Program akan memindai folder dan subfolder. Duplikat yang ditemukan akan dipilih berdasarkan file **terlama diupload**, dan file lainnya akan dikeluarkan dari folder (tetap di Drive).  

### 6. Unduh Hasil  
Setelah selesai, Anda dapat mengunduh hasil deteksi dalam file teks.  

## Catatan Penting  

1. **File yang Dikeluarkan dari Folder**:  
   - File **tidak dihapus**, hanya **dikeluarkan dari folder**.  
   - File tetap ada di My Drive, dan jika Anda pengunggahnya, akan muncul di halaman utama My Drive.  
   - Untuk file yang diunggah orang lain, file mungkin tidak muncul di My Drive Anda dan kembali ke pengunggah asli.  

2. **Persiapkan Struktur Folder**:  
   - Program memindai seluruh folder dan subfolder, termasuk folder berbagi dan pintasan.  
   - Jika hanya ingin memindai folder tertentu, buat pintasan folder ke My Drive sebelum menjalankan program.  

3. **Uji Program Terlebih Dahulu**:  
   - Uji program pada folder percobaan untuk memastikan hasilnya sesuai harapan.  
