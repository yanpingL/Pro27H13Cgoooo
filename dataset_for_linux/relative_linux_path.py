import json

# List of files to process
file_names = ['test.json', 'train.json', 'val.json']

# Function to replace backslashes and overwrite the file
def convert_paths_in_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    # Replace \\ with /
    for item in data:
        item['image_path'] = item['image_path'].replace('\\', '/')
    
    # Overwrite the original file
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
    print(f"File {file_name} has been successfully converted and saved.")

# Process each file
for file_name in file_names:
    convert_paths_in_file(file_name)



