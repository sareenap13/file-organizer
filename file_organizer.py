from pathlib import Path

folder = Path("test_downloads")
file_type = {
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".csv": "Data",
    ".docx": "Documents",
    ".xlsx": "Data",
    ".dmg": "Installers",
    ".exe": "Installers"
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
    for file in folder.iterdir():
        if file.is_file():
            organize_file(file, folder, file_type)

organize_folder(folder, file_type)