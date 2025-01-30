import os

def rename_files(folder_path, base_name):
    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Get all files in the folder, sorted by creation time
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=lambda f: os.path.getctime(os.path.join(folder_path, f)))

    if not files:
        print("No files found in the directory.")
        return

    # Rename the files with the new format
    for idx, file_name in enumerate(files, start=1):
        file_extension = os.path.splitext(file_name)[1]  # Extract file extension
        new_name = f"{base_name}_{idx}{file_extension}"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

    print("Renaming complete.")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing files: ").strip()
    base_name = input("Enter the base name for the files: ").strip()
    rename_files(folder_path, base_name)
