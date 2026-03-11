import os


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