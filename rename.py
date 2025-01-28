import os

def rename_png_files(folder_path, base_name):
    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Get all .png files in the folder, sorted by creation time
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    png_files.sort(key=lambda f: os.path.getctime(os.path.join(folder_path, f)))

    if not png_files:
        print("No .png files found in the directory.")
        return

    # Rename the files with the new format
    for idx, file_name in enumerate(png_files, start=1):
        new_name = f"{base_name}_{idx}.png"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

    print("Renaming complete.")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing .png files: ").strip()
    base_name = input("Enter the base name for the files (e.g., 'header'): ").strip()
    rename_png_files(folder_path, base_name)
