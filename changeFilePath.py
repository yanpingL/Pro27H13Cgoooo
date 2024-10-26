import json

"""
change the filename to modify different json files
have already modified the relative path in train.json, val.json and test.json
this is the pathname changing script
the new files and this script will be update on GitHub
"""
# Read the JSON file
with open("val.json", "r") as file:
    data = json.load(file)

# Modify the image_path for each entry
for item in data:
    # Replace Windows-style backslashes with Linux-style forward slashes
    item["image_path"] = item["image_path"].replace("\\", "/")
    
    # Remove the F:/2024 T3/9444/project/ part of the path, keeping the part starting with 'dataset'
    item["image_path"] = item["image_path"].split('dataset/', 1)[-1]
    item["image_path"] = 'dataset/' + item["image_path"]

# Write the modified content back to a new file
with open("val_modified.json", "w") as file:
    json.dump(data, file, indent=4)

print("Paths have been successfully modified and saved as 'val_modified.json'")
