logger = 'Comet' #@param ['Comet', 'TensorBoard']
import comet_ml
comet_ml.init()
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model.MOD(train)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='../data/ship.yaml', device='0,1', task='detect', mode='train', epochs=500, imgsz=500, batch=-1)