import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "X:\JuFo2023\DATA\Aepfel"
CATIGORIES = ["Aepfel"]

for catigory in CATIGORIES:
    path = os.path.join(DATADIR,catigory)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_COLOR)


IMG_SIZE = 75 
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))


training_data = []

def create_training_data():
    for catigory in CATIGORIES:
        path = os.path.join(DATADIR,catigory)
        class_num = CATIGORIES.index(catigory)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_COLOR)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
create_training_data()

print(len(training_data))