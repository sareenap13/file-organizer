from pathlib import Path
from file_organizer import get_destination_folder, get_unique_filename

file_type = {
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".csv": "Data"
}

# test cases for get_destination_folder
assert get_destination_folder(Path("resume.pdf"), file_type) == "PDFs"
assert get_destination_folder(Path("resume.PDF"), file_type) == "PDFs"
assert get_destination_folder(Path("notes.txt"), file_type) == "Other"

# test cases for get_unique_fileneame
destination = Path("file-organizer/test_downloads/PDFs")
assert get_unique_filename(
    Path("new_resume.pdf"),
    destination
) == destination / "new_resume.pdf"

assert get_unique_filename(
    Path("resume.pdf"),
    destination
) == destination / "resume_2.pdf"

assert get_unique_filename(
    Path("resume.pdf"),
    destination
) == destination / "resume_2.pdf"

assert get_destination_folder(
    Path("something.html"),
    destination
) == "Web"