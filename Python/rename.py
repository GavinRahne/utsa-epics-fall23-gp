import os

folder_path = r"C:\\Users\\Gavin\\Desktop\\Python"

def rename_images_sequentially(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
   
    # Filter out only image files (you can customize the extensions)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
   
    # Sort the image files to maintain order
    image_files.sort()
   
    # Rename the image files sequentially
    for index, old_name in enumerate(image_files):
        extension = os.path.splitext(old_name)[1]
        new_name = f"Gavin_{index + 1}{extension}.jpg"
       
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
       
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

rename_images_sequentially(folder_path)