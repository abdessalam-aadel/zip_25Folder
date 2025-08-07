import os
import zipfile

# Set the source folder where the folders to be archived are located
source_folder = r"C:\your_path_here"

# Initialize counters
folder_counter = 0
archive_counter = 1
folder_list = []

# Loop through each folder in the source folder
for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)

    # Only consider directories (folders)
    if os.path.isdir(folder_path):
        folder_list.append(folder_path)
        folder_counter += 1

    # If 25 folders have been added, create a new zip file
    if folder_counter >= 25:
        zip_filename = os.path.join(source_folder, f"{archive_counter}.zip")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder in folder_list:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_folder)
                        zipf.write(file_path, arcname)
        
        # Reset for the next batch of 25 folders
        archive_counter += 1
        folder_counter = 0
        folder_list = []

# If there are remaining folders (less than 25), archive them too
if folder_list:
    zip_filename = os.path.join(source_folder, f"{archive_counter}.zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folder_list:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_folder)
                    zipf.write(file_path, arcname)

print("Done!")
