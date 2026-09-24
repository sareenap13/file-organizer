from pathlib import Path

folder_input = input("Enter folder to organize: ")
folder = Path(folder_input)

file_type = {
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".heic": "Images",
    ".csv": "Data",
    ".docx": "Documents",
    ".md": "Documents",
    ".xlsx": "Data",
    ".dmg": "Installers",
    ".exe": "Installers",
    ".html": "Web",
    ".mp4": "Videos"
}

def get_destination_folder(file, file_type):
    folder_name = file_type.get(file.suffix.lower(), "Other")
    return folder_name

def get_unique_filename(file, destination):
    destination_file = destination / file.name
    counter = 0

    while destination_file.exists():
        counter += 1
        destination_file = destination / (file.stem + "_" + str(counter) + file.suffix)

    return destination_file

def organize_file(file, folder, file_type):
    folder_name = get_destination_folder(file, file_type)
    destination = folder / folder_name
    destination.mkdir(exist_ok = True)
    destination_file = get_unique_filename(file, destination)
    file.rename(destination_file)

def organize_folder(folder, file_type):
    count_files = 0
    count_folders = {}
    for file in folder.iterdir():
        if file.is_file():
            organize_file(file, folder, file_type)
            count_files += 1
            folder_name = get_destination_folder(file, file_type)
            if folder_name in count_folders:
                count_folders[folder_name] = count_folders[folder_name] + 1
            else:
                count_folders[folder_name] = 1
    return count_files, count_folders

if __name__ == "__main__":
    if folder.exists() & folder.is_dir():
        count_files, count_folders = organize_folder(folder, file_type)
        print(f"Organized {count_files} files.")
        for key, value in count_folders.items():
            print(f"{key}: {value}")
    else:
        print("Folder does not exist.")
        