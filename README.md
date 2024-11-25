# Google Drive Duplicate File Remover

## Deskripsi
Program ini dirancang untuk mendeteksi dan mengelola file duplikat di Google Drive Anda berdasarkan nama file. Program ini akan:

1. **Membaca Semua Folder di My Drive**: Skrip ini memindai semua folder yang ada di akun Google Drive Anda, termasuk folder utama dan pintasan ke folder berbagi (sharing folders) yang ditambahkan ke My Drive.
   
2. **Mendeteksi File Duplikat**: Program akan memeriksa setiap folder dan subfolder untuk menemukan file dengan nama yang sama (duplikat). File yang dianggap duplikat akan dikelompokkan berdasarkan nama file.

3. **Menangani Duplikat**: Dari setiap kelompok file duplikat, hanya satu file yang akan dipertahankan. Program memilih file yang terlama diupload dan mengeluarkan file lainnya dari folder.

4. **Membaca Folder dan Subfolder**: Program secara rekursif akan membaca folder dan subfolder dalam Google Drive untuk mendeteksi duplikat, memastikan tidak ada file duplikat yang terlewat.

5. **Mengeluarkan File dari Folder**: Setelah mendeteksi file duplikat, program akan mengeluarkan file yang tidak dipilih dari folder, sehingga hanya satu file yang tersisa di folder tersebut.

## Cara Instalasi

1. **Persiapkan Google Colab**:
   - Program ini dirancang untuk dijalankan di Google Colab. Pastikan Anda memiliki akun Google dan dapat mengakses Google Colab.

2. **Clone Repositori**:
   Clone repositori ini ke dalam Google Colab atau mesin lokal Anda:
   ```bash
   git clone https://github.com/Username/Google-Drive-Duplicate-File-Remover.git
   ```

3. **Install Dependensi**:
   Skrip ini menggunakan `google-auth` dan `google-api-python-client` untuk berinteraksi dengan Google Drive API. Pastikan untuk menginstal dependensi berikut di Google Colab:
   ```python
   !pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

4. **Jalankan Skrip**:
   Setelah menginstal dependensi, Anda dapat menjalankan skrip di Google Colab. Cukup pastikan bahwa Anda telah mengautentikasi akun Google Anda dengan benar menggunakan `auth.authenticate_user()`.

## Cara Menjalankan Program

1. **Autentikasi Akun Google**:
   - Program ini memerlukan autentikasi untuk mengakses Google Drive Anda. Di Colab, Anda akan diminta untuk login dan memberikan izin akses.

2. **Pilih Folder untuk Diperiksa**:
   - Setelah autentikasi berhasil, program akan menampilkan daftar folder utama di Google Drive Anda. Pilih folder yang ingin Anda periksa untuk duplikat dengan memasukkan nama atau nomor folder.

3. **Proses Duplikat**:
   - Program akan memindai folder yang dipilih dan semua subfoldernya untuk mencari file duplikat berdasarkan nama. Setelah itu, program akan memilih satu file yang terlama diupload dan mengeluarkan file lainnya.

4. **Mengunduh Hasil**:
   - Setelah proses selesai, Anda akan diberikan opsi untuk mengunduh hasilnya dalam bentuk file teks yang berisi laporan tentang file yang dipertahankan dan yang dikeluarkan.

## Catatan Penting

- **Hati-Hati dengan Penghapusan**: Program ini akan mengeluarkan file dari folder Anda. Pastikan Anda telah memeriksa file duplikat sebelum menjalankan program, karena file yang dikeluarkan tidak dapat dikembalikan.
  
- **Rate Limiting Google API**: Google API memiliki batasan permintaan. Jika Anda memiliki banyak file untuk diproses, Anda mungkin akan mengalami pembatasan dalam jumlah permintaan yang dapat dilakukan dalam waktu tertentu.

- **Pintasan Folder**: Program ini juga dapat mendeteksi dan memindai folder pintasan yang mengarah ke folder berbagi. Pastikan Anda tidak melewatkan folder berbagi yang Anda akses melalui pintasan.

## Struktur Program
1. **list_files_in_folder_recursive**: Fungsi ini untuk memindai folder dan subfolder secara rekursif dan mendeteksi semua file.
2. **find_duplicate_files**: Mengelompokkan file berdasarkan nama untuk menemukan duplikat.
3. **remove_file_from_folder**: Mengeluarkan file dari folder jika terdeteksi sebagai duplikat.
4. **write_output_to_file**: Menulis hasil proses ke file teks.
5. **prompt_for_download**: Meminta pengguna untuk mengunduh hasil output.
6. **main_program**: Fungsi utama yang menjalankan seluruh proses.

## Penanganan Error

- Jika terjadi kesalahan selama proses, program akan menangani exception dan mencetak pesan error yang sesuai. Pastikan untuk memeriksa log output jika terjadi masalah.

---

**Sumber Daya Tambahan**:
- [Google Drive API Documentation](https://developers.google.com/drive)
- [Google Colab Documentation](https://colab.research.google.com)
```
