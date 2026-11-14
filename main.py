import hashlib
import pathlib

def calculate_hash(filename):
    file = pathlib.Path(filename)

    if not file.is_file():
        print("File does not exist.")
        return

    sha256 = hashlib.sha256()

    with file.open("rb") as data:
        for chunk in iter(lambda: data.read(4096), b""):
            sha256.update(chunk)

    print("File:", filename)
    print("SHA256:", sha256.hexdigest())


calculate_hash("sample.txt")
