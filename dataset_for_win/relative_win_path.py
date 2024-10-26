import json
import os

# Define the list of files to be processed
files = ["test.json", "train.json", "val.json"]

# Iterate through each file
for file_name in files:
    file_path = file_name  # Since the files are in the same directory, just use the file name
    
    # Read the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Modify the image_path for each entry
    for item in data:
        # Remove the prefix (e.g., F:/2024 T3/9444/project/), keeping the part starting with 'dataset'
        item["image_path"] = item["image_path"].split('dataset\\', 1)[-1]
        item["image_path"] = 'dataset\\' + item["image_path"]
    
    # Overwrite the original file with modified content
    with open(file_path, "w") as modified_file:
        json.dump(data, modified_file, indent=4)
    
    print(f"Paths in {file_name} have been successfully modified and saved back to the original file.")
