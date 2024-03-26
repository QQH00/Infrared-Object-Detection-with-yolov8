logger = 'Comet' #@param ['Comet', 'TensorBoard']
import comet_ml
comet_ml.init()
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-obb.yaml')  # build a new model from YAML
model = YOLO('yolov8n-obb.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n-obb.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='../data/MAR20/MAR20.yaml', device='0,1', task='detect', mode='train', epochs=500, imgsz=800, batch=-1)