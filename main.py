# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:38:45 2023

@author: Jakub
"""

from tensorflow.keras.datasets import mnist
import numpy as np
from NeuralNetwork import NeuralNetwork

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

new_X_train = X_train.reshape(*X_train.shape[:1], -1)
new_X_test = X_test.reshape(*X_test.shape[:1], -1)
X_train = np.transpose(new_X_train) / 255
X_test = np.transpose(new_X_test) / 255

model = NeuralNetwork()

### FITTING THE MODEl
model.fit(X_train, Y_train, 0.7, 500)

### MAKING PREDICTIONS
predictions = model.predict(X_test)
print(predictions)

### VISUALISING PREDICTIONS
model.visualise_predictions(X_test, predictions, Y_test, n_examples = 10)