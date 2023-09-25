import os
import shutil

# Specify the source folder containing your files
source_folder = r"C://Users//Gavin//Desktop//Python"  # Replace with your source folder path

# Create subfolders for organizing the files
for i in range(1, 50):  # Create 5 subfolders (1-5)
    subfolder_name = f'Group_{i}'  # You can change the naming pattern if desired
    subfolder_path = os.path.join(source_folder, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)

# List the files in the source folder
file_list = os.listdir(source_folder)

# Iterate through the files and move them to subfolders
for i, filename in enumerate(file_list):
    source_file_path = os.path.join(source_folder, filename)
    destination_subfolder = i // 10  # Group files in sets of 10
    destination_folder = os.path.join(source_folder, f'Group_{destination_subfolder + 1}')
    destination_file_path = os.path.join(destination_folder, filename)
    shutil.move(source_file_path, destination_file_path)
    print(f'Moved {filename} to {destination_folder}')

print("Files organized into groups of 10.")
