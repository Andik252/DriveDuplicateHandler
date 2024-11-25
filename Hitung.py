from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.colab import files

auth.authenticate_user()
service = build('drive', 'v3')

# Menambahkan kategori jenis file (foto, video, dll)
PHOTO_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp', 'gif', 'bmp'}
VIDEO_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv', 'flv'}

def list_files_in_folder_recursive(folder_id):
    """Mendaftarkan semua file dalam folder dan subfolder secara rekursif, dengan pagination."""
    files = []
    folders = [folder_id]
    
    while folders:
        current_folder_id = folders.pop()
        page_token = None  # Untuk pagination
        while True:
            try:
                response = service.files().list(
                    q=f"'{current_folder_id}' in parents and trashed=false",
                    fields="nextPageToken, files(id, name, mimeType, parents)",
                    pageSize=1000,
                    pageToken=page_token
                ).execute()

                items_in_folder = response.get('files', [])
                
                for item in items_in_folder:
                    if item['mimeType'] == 'application/vnd.google-apps.folder':
                        folders.append(item['id'])
                    else:
                        files.append(item)
                
                page_token = response.get('nextPageToken')
                if not page_token:
                    break
            except HttpError as error:
                print(f"Terjadi kesalahan saat membaca folder {current_folder_id}: {error}")
                break

    return files

def categorize_files(files):
    """Mengelompokkan file berdasarkan jenis MIME (Foto, Video, dll)."""
    categorized_files = {
        'Foto': [],
        'Video': [],
        'Lainnya': []  # Menampung file selain foto dan video
    }
    
    for file in files:
        ext = file['name'].split('.')[-1].lower()  # Mengambil ekstensi file
        if ext in PHOTO_EXTENSIONS:
            categorized_files['Foto'].append(file)
        elif ext in VIDEO_EXTENSIONS:
            categorized_files['Video'].append(file)
        else:
            categorized_files['Lainnya'].append(file)
    
    return categorized_files

def print_file_counts(categorized_files):
    """Menampilkan hasil penghitungan file per kategori tanpa nama file."""
    output = ""
    for category, files in categorized_files.items():
        output += f"Jenis File {category}\n"
        output += f"Total ada : {len(files)} {category}\n"
        output += "-------------------------\n"
    return output

def list_main_and_shortcut_folders_in_my_drive(exclude_folders):
    """Mendaftarkan semua folder utama dan pintasan di My Drive, kecuali folder yang dikecualikan."""
    try:
        results = service.files().list(
            q="(mimeType='application/vnd.google-apps.folder' or mimeType='application/vnd.google-apps.shortcut') "
              "and trashed=false and 'root' in parents",
            fields="files(id, name, mimeType, shortcutDetails)", pageSize=100).execute()
        
        folders = [
            folder for folder in results.get('files', [])
            if folder['name'] not in exclude_folders
        ]
        
        print("Folder utama (dan pintasan) di My Drive Anda:")
        for i, folder in enumerate(folders, start=1):
            print(f"{i}. {folder['name']}")
        return folders
    except HttpError as error:
        print(f'Terjadi kesalahan: {error}')
        return []

def main_program():
    """Fungsi utama untuk menjalankan program."""
    exclude_folders = ["Colab Notebooks"]
    folders = list_main_and_shortcut_folders_in_my_drive(exclude_folders)
    folder_input = input("\nMasukkan nomor atau nama folder (pintasan) untuk menghitung jumlah file: ")

    selected_folder = None

    selected_folder = next((f for f in folders if f['name'].lower() == folder_input.lower()), None)

    if not selected_folder and folder_input.isdigit():
        folder_index = int(folder_input) - 1
        if 0 <= folder_index < len(folders):
            selected_folder = folders[folder_index]

    if selected_folder:
        shortcut_target_id = selected_folder['shortcutDetails']['targetId'] if selected_folder['mimeType'] == 'application/vnd.google-apps.shortcut' else selected_folder['id']
        all_files = list_files_in_folder_recursive(shortcut_target_id)
        categorized_files = categorize_files(all_files)
        output = print_file_counts(categorized_files)
        print(output)
    else:
        print("Folder tidak ditemukan. Pastikan nama atau nomor folder yang Anda masukkan benar.")

if __name__ == "__main__":
    try:
        main_program()
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\nTerjadi error tak terduga: {e}")
