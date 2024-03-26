import os, shutil
from sklearn.model_selection import train_test_split

val_size = 0.1
test_size = 0.2

# 设置数据集名字
dataset = 'MAR20'


# jpg or png
postfix = 'jpg'

# 设置数据集的标注文件和图片文件的路径
imgpath = 'data/MAR20/JPEGImages'
txtpath = 'data/MAR20/Annotations/Oriented Bounding Boxes TXT/'

os.makedirs(f'data/{dataset}/images/train', exist_ok=True)
os.makedirs(f'data/{dataset}/images/val', exist_ok=True)
os.makedirs(f'data/{dataset}/images/test', exist_ok=True)
os.makedirs(f'data/{dataset}/labels/train', exist_ok=True)
os.makedirs(f'data/{dataset}/labels/val', exist_ok=True)
os.makedirs(f'data/{dataset}/labels/test', exist_ok=True)

listdir = [i for i in os.listdir(txtpath) if 'txt' in i]
train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')

for i in train:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'data/{dataset}/images/train/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'data/{dataset}/labels/train/{i}')

for i in val:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'data/{dataset}/images/val/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'data/{dataset}/labels/val/{i}')

for i in test:
    shutil.copy(f'{imgpath}/{i[:-4]}.{postfix}', f'data/{dataset}/images/test/{i[:-4]}.{postfix}')
    shutil.copy(f'{txtpath}/{i}', f'data/{dataset}/labels/test/{i}')

