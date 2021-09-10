"""

    Single Frame Inference with YOLOv5

"""
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
# # As URL
# img = 'https://ultralytics.com/images/zidane.jpg'
# # As File
img = 'imgs/living_room.jpg'

# Inference
results = model(img)

# Results
print(results.render())
print(results.show())