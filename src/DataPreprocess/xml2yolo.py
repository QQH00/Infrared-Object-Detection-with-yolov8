import os
import xml.etree.ElementTree as ET

# 定义输入输出路径
input_dir = '/home/huangqinlong/Workspace/ultralytics/data/MAR20/Annotations/Oriented Bounding Boxes'
output_dir = '/home/huangqinlong/Workspace/ultralytics/data/MAR20/Annotations/txt'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

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
        width = float(size.find('width').text)
        height = float(size.find('height').text)

        if width == 0 or height == 0:
            print(f"文件 {xml_file} 的宽度或高度为零，已跳过处理。")
            continue

        # 为每个XML文件创建一个对应的TXT文件
        base_filename = os.path.splitext(xml_file)[0]
        txt_path = os.path.join(output_dir, base_filename + '.txt')

        with open(txt_path, 'w') as txt_file:
            # 从XML中提取对象信息
            for obj in root.iter('object'):
                # 获取类别名称并转换为类别编号
                name = obj.find('name').text
                category = int(name[1:])  # 假设名称格式始终是"A"后跟数字

                # 提取并归一化坐标
                robndbox = obj.find('robndbox')
                x_left_top = float(robndbox.find('x_left_top').text) / width
                y_left_top = float(robndbox.find('y_left_top').text) / height
                x_right_top = float(robndbox.find('x_right_top').text) / width
                y_right_top = float(robndbox.find('y_right_top').text) / height
                x_right_bottom = float(robndbox.find('x_right_bottom').text) / width
                y_right_bottom = float(robndbox.find('y_right_bottom').text) / height
                x_left_bottom = float(robndbox.find('x_left_bottom').text) / width
                y_left_bottom = float(robndbox.find('y_left_bottom').text) / height

                # 将提取的数据格式化为文本格式
                annotation_text = f"{category} {x_left_top:.6f} {y_left_top:.6f} {x_right_top:.6f} {y_right_top:.6f} " \
                                  f"{x_right_bottom:.6f} {y_right_bottom:.6f} {x_left_bottom:.6f} {y_left_bottom:.6f}\n"

                # 写入文件
                txt_file.write(annotation_text)

print("所有XML文件已转换完成。")