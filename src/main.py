import cv2
import os
import sift
import json
import numpy as np
from matplotlib import pyplot as plt

#get the filename of every image
images_paths  = os.listdir("src/images")
# #build empty list to contains all the features of the images 
# features = {}
# features_sum = {}
# for im_path in images_paths:
#     print(im_path)
#     img = cv2.imread("src/images/"+im_path)
#     grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     feature, list_features = sift.find_sift(grayscale)
#     grayscale = cv2.drawKeypoints(grayscale, feature, grayscale)
#     cv2.imwrite("src/sifted_images/"+im_path, grayscale)
#     features[im_path] = list_features

# with open("src/sift_features.json", "w") as file:
#     json.dump(features, file)

# images_paths_bis = images_paths
# cropped_path = os.listdir("src/images/cropped")
# ####test du matching des images
# for cropped in cropped_path:
#     #select randomly an image
#     index = np.random.randint(len(images_paths_bis))
#     print(cropped)
#     img_test = cv2.imread("src/images/cropped/"+cropped)
#     print("src/images/cropped/"+cropped)
#     #on retire cette image de la liste afin de ne plus la reprendre
#     del images_paths_bis[index]
#     sift.find_match_orb(img_test)
#     print("#############")
#     sift.find_match_sift(img_test)
#     print("_______________________________________________________")
        

# sift.generate_sift_descrpitors("images_desjardin")
# print(features)
images_list = os.listdir("src/images_desjardin")
for image in images_list[0:5]:
    print("--------------------------------------")
    img = cv2.imread("src/images_desjardin/"+image)
    sift.find_match_sift_from_pkl(img)