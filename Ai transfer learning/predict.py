#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:30:43 2019

@author: Mxolisi
"""

from keras.models import load_model
import cv2
import numpy as np

model = load_model('/Users/Mxolisi/Documents/LabWork/newPull/Programmatic-edit/Ai transfer learning/firsttry.h5') #Loads the model

#compiles the model
model.compile(loss='binary_crossentropy', 
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('wmachine.jpeg') #reads image from a directory using OpenCV
img = cv2.resize(img,(320,240))
img = np.reshape(img,[1,320,240,3])

#Predicts image from the trained model's dataset
classes = model.predict_classes(img)

print(classes)
