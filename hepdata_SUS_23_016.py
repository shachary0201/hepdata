import tarfile
import os

# Name of the folder containing all your files
#submission_folder = "Submission"  # change this to your folder name
#submission_folder = "Submission_test"  # change this to your folder name
#submission_folder = "Submission_test_pushed1"  # change this to your folder name
submission_folder = "Submission_test_pushed3_bill"  # change this to your folder name

# Name of the tarball to create
output_tarball = "submission_SUS_23_016.tar.gz"

def add_files_to_tar(tar, folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Add file preserving relative paths inside the tarball
            tar.add(file_path, arcname=os.path.relpath(file_path, folder))

with tarfile.open(output_tarball, "w:gz") as tar:
    add_files_to_tar(tar, submission_folder)

print(f"Tarball '{output_tarball}' created successfully!")
