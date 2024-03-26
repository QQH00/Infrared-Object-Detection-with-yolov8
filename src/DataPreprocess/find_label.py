import os
import xml.etree.ElementTree as ET

# 设定Annotations目录的路径
annotations_dir = "/home/huangqinlong/Workspace/ultralytics/data/MAR20/Annotations/Oriented Bounding Boxes"

# 初始化一个空列表，用于存储所有解析出的数字值
numbers = []

# 遍历Annotations目录下的所有xml文件
for filename in os.listdir(annotations_dir):
    if filename.endswith('.xml'):
        # 构建文件的完整路径
        file_path = os.path.join(annotations_dir, filename)

        # 解析XML文件
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 遍历所有的object元素
        for obj in root.findall('object'):
            # 获取name元素的文本值
            name = obj.find('name').text
            # 假设name的格式总是"A"后跟数字，提取数字部分
            if name.startswith('A'):
                number = int(name[1:])  # 提取数字部分并转换为整数
                numbers.append(number)

# 找到数字的最大值
max_number = max(numbers) if numbers else None

# 打印最大的数字值
print(f"The maximum number value after 'A' is: {max_number}")