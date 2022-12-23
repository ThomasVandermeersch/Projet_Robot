import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import json

def compute_color_signature(img):
    img = cv2.imread(img)
    b, g, r = cv2.split(img)
    b_mean, g_mean, r_mean = b.mean(), g.mean(), r.mean()
    return [b_mean, g_mean, r_mean]

def store_mean_values(images_folder):
    images = os.listdir(images_folder)
    means_dict = {}
    for image in images:
        print(images_folder+"/"+image)
        means_dict[image] = compute_color_signature(images_folder+"/"+image)
    with open("src/means.json", "w") as file:
            json.dump(means_dict, file, indent = 4)