import os
import shutil

# Get folder path from user
source = input("Enter folder path: ")

# File categories
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

# Read all files in the folder
for file in os.listdir(source):
    path = os.path.join(source, file)

    # Check if it is a file
    if os.path.isfile(path):
        ext = os.path.splitext(file)[1].lower()

        # Move file to matching folder
        for folder, extensions in folders.items():
            if ext in extensions:
                destination = os.path.join(source, folder)

                # Create folder if it does not exist
                os.makedirs(destination, exist_ok=True)

                # Move the file
                shutil.move(path, os.path.join(destination, file))
                break

print("Files Organized Successfully!")