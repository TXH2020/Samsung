from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

import tensorflow as tf
assert tf.__version__.startswith('2')

import matplotlib.pyplot as plt
import numpy as np
data = DataLoader.from_folder(r'C:\Users\1001t\Downloads\surface_photos')
print("hi")
train_data, test_data = data.split(0.9)
model = image_classifier.create(train_data)
loss, accuracy = model.evaluate(test_data)
print("Loss=",loss,',accuracy=',accuracy)
model.export(export_dir='.')