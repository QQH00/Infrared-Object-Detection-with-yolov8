import os
import glob
import xml.etree.ElementTree as ET

# 设置数据集路径
annotations_path = '../../data/MAR20/Annotations/Oriented Bounding Boxes/'
output_path = '../../data/MAR20/Annotations/Oriented Bounding Boxes TXT/'

# 确保输出路径存在
os.makedirs(output_path, exist_ok=True)

# 类别映射
class_mapping = {f'A{i}': i-1 for i in range(1, 21)}

# 解析XML文件并提取边界框信息
def convert_annotation(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    with open(output_file, 'w') as f:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in class_mapping:
                continue
            cls_id = class_mapping[cls]
            xmlbox = obj.find('robndbox')
            points = ['x_left_top', 'y_left_top', 'x_right_top', 'y_right_top', 'x_right_bottom', 'y_right_bottom', 'x_left_bottom', 'y_left_bottom']
            b = (float(xmlbox.find(p).text) for p in points)
            # Write to txt file
            f.write(str(cls_id) + " " + " ".join(['{:.6f}'.format(x/w if i%2 == 0 else x/h) for i, x in enumerate(b)]) + '\n')

# 转换所有XML文件
for xml_file in glob.glob(annotations_path + '/*.xml'):
    output_file = output_path + os.path.basename(xml_file)[:-4] + '.txt'
    convert_annotation(xml_file, output_file)

print("Conversion completed!")