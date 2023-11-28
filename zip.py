import zipfile
import pathlib


def make_archive(filepath, destination):
    """
    Create a zip file in the destination using given filepath
    arcname extracts only the name of the file and not entire filepath
    """
    destination_path = pathlib.Path(destination, "file.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for file in filepath:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)


# Only execute if zip.py is executed directly
if __name__ == "__main__":
    make_archive(filepath=["../files/a.txt"], destination="test")
