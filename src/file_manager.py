import os
import hashlib


def get_all_files(folder_path):

    files = []

    for root, dirs, file_names in os.walk(folder_path):

        for file in file_names:

            full_path = os.path.join(root, file)
            files.append(full_path)

    return files


if __name__ == "__main__":

    folder = "data/healthcare_data"

    files = get_all_files(folder)

    print("Healthcare Files Found:")

    for f in files:
        print(f)

        import hashlib


def get_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:
            data = f.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()