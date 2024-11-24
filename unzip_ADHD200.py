import os
import gzip
import shutil

# Define the source and destination directories
source_dir = "C:/Users/ahmm9/OneDrive - ITU/ITU/Research_proj/Adhd200_preproc/NYU"  # Folder containing nested subdirectories
destination_dir = "C:/Users/ahmm9/OneDrive - ITU/ITU/Research_proj/Adhd200_preproc/NYU_preproc"  # Folder to store extracted files

# Ensure the destination folder exists
os.makedirs(destination_dir, exist_ok=True)

# Walk through all subdirectories in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file starts with 'sfnwmrda' and ends with '.gz'
        if file.startswith("sfnwmrda") and file.endswith(".gz"):
            file_path = os.path.join(root, file)  # Full path to the .gz file

            # Define the output path in the destination folder
            output_file_name = os.path.splitext(file)[0]  # Remove .gz extension
            output_file_path = os.path.join(destination_dir, output_file_name)

            # Unzip and save the file
            with gzip.open(file_path, 'rb') as gz_file:
                with open(output_file_path, 'wb') as extracted_file:
                    shutil.copyfileobj(gz_file, extracted_file)

            print(f"Extracted: {file_path} -> {output_file_path}")

print(f"All files have been extracted to {destination_dir}.")
