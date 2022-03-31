from pathlib import Path
import argparse
 
parser = argparse.ArgumentParser(description="Find file in file system")
 
parser.add_argument(
    "file_name", nargs="?", help="File name (can use wildcards such as *)",
    default=None
)
parser.add_argument(
    "folder", nargs="?", help="Folder (default: current)",
    default=None
)
 
arguments = parser.parse_args()
 
use_arguments_file_name = True if arguments.file_name is not None else False
use_arguments_folder = True if arguments.folder is not None else False
 
# Validation of file name
if use_arguments_file_name:
    file_name = arguments.file_name
else:
    while True:
        file_name = input("Filename: ")
 
        if file_name == "":
            print("Invalid file name")
            continue
        break
 
# Processing of the folder argument
folder = "."
if use_arguments_folder:
    folder = arguments.folder
else:
    folder_answer = input("Folder path (leave empty for the current folder): ")
    if folder_answer:
        folder = folder_answer
 
for path in Path(folder).rglob(file_name):
    print(path.absolute())