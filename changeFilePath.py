import json

# 读取 JSON 文件
with open("val.json", "r") as file:
    data = json.load(file)

# 修改每个条目中的 image_path
for item in data:
    # 替换 Windows 风格的路径分隔符为 Linux 风格
    item["image_path"] = item["image_path"].replace("\\", "/")
    
    # 去除路径中 F:/2024 T3/9444/project/ 的部分，保留 dataset 开头
    item["image_path"] = item["image_path"].split('dataset/', 1)[-1]
    item["image_path"] = 'dataset/' + item["image_path"]

# 将修改后的内容写回到文件
with open("val_modified.json", "w") as file:
    json.dump(data, file, indent=4)

print("路径已成功修改并保存为 'val_modified.json'")
