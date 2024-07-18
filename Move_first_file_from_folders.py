# python Move_first_file_from_folders.py

import os
import shutil

def move_first_file(source_folder, destination_folder):
  """
  The function moves the first file from the source folder to the destination folder.
  
  """
  # is path.exists ?
  if not os.path.exists(source_folder):
    raise Exception(f"source_folder '{source_folder}' is not exists.")

  if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

  # Get a list of files
  files = os.listdir(source_folder)

  if not files:
    return

  # First file
  first_file = files[0]

  path_first_file = os.path.join(source_folder, first_file)

  # Move file to
  target_path = os.path.join(destination_folder, first_file)
  shutil.move(path_first_file, target_path)

def main():
  
  source_folder = "C:\\USER...\\"
  destination_folder = "C:\\USER...\\MOVE_FILES"

  for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)
    move_first_file(folder_path, destination_folder)

if __name__ == "__main__":
  main()