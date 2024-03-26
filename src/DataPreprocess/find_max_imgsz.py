import os
import xml.etree.ElementTree as ET

# 定义输入路径
input_dir = "data/MAR20/Annotations/Oriented Bounding Boxes"

# 初始化最大宽度和高度
max_width = 0
max_height = 0

# 遍历输入目录下的所有XML文件
for xml_file in os.listdir(input_dir):
    if xml_file.endswith('.xml'):
        # 完整的文件路径
        xml_path = os.path.join(input_dir, xml_file)

        # 解析XML文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 获取图像尺寸
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # 更新最大宽度和高度
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height

# 输出最大的宽度和高度
print(f"最大宽度: {max_width}")
print(f"最大高度: {max_height}")