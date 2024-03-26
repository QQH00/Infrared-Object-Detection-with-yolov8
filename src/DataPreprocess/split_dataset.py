import os, shutil
from sklearn.model_selection import train_test_split

val_size = 0.1
test_size = 0.2
postfix = 'jpg'
imgpath = '../../data/MAR20/JPEGImages'
txtpath = '../../data/MAR20/Annotations/Oriented Bounding Boxes TXT/'

os.makedirs('../../data/MAR20/images/train', exist_ok=True)
os.makedirs('../../data/MAR20/images/val', exist_ok=True)
os.makedirs('../../data/MAR20/images/test', exist_ok=True)
os.makedirs('../../data/MAR20/labels/train', exist_ok=True)
os.makedirs('../../data/MAR20/labels/val', exist_ok=True)
os.makedirs('../../data/MAR20/labels/test', exist_ok=True)

listdir = [i for i in os.listdir(txtpath) if 'txt' in i]
train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')

for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '../../data/MAR20/images/train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '../../data/MAR20/labels/train/{}'.format(i))

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '../../data/MAR20/images/val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '../../data/MAR20/labels/val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '../../data/MAR20/images/test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '../../data/MAR20/labels/test/{}'.format(i))
:
