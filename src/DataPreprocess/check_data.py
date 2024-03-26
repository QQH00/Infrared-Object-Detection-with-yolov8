import os

# 图片和标签文件夹的路径
images_dir = "/home/huangqinlong/Workspace/ultralytics/data/MAR20/images/test"
labels_dir = "/home/huangqinlong/Workspace/ultralytics/data/MAR20/labels/test"
# 获取标签目录下所有的.txt文件
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# 遍历所有标签文件，检查是否有相应的.jpg图片文件
for label_file in label_files:
    # 构建对应的.jpg文件名
    image_file = f"{os.path.splitext(label_file)[0]}.jpg"

    # 构建图片文件的完整路径
    image_file_path = os.path.join(images_dir, image_file)


    # 检查标签文件是否存在
    if not os.path.isfile(image_file_path):
        print(f"Label file for image {image_file} is missing.")