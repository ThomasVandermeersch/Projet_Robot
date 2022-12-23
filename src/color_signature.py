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

def compare_color_signature(mean_test, mean_ref, tolerence):
    """
    cette méthode retourne true si les deux moyennes sont suffisement proche
    false sinon
    """
    count = 0
    for i in range(len(mean_ref)):
        if mean_test[i] <= (mean_ref[i] + 15) and mean_test[i] >= (mean_ref[i] - 15):
            count += 1

    if count == len(mean_test)-1:
        return True
    else:
        return False
    