import cv2
import os
import sift
import json
import numpy as np
from matplotlib import pyplot as plt
import color_signature

#get the filename of every image
# images_paths  = os.listdir("src/images")
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
# images_list = os.listdir("src/image_test_bon")
# for image in images_list:
#     print("--------------------------------------")
#     print(image)
#     img = cv2.imread("src/image_test_bon/"+image)
#     print(color_signature.compute_color_signature(img))
#     matches = sift.find_match_sift_from_pkl(img)
#     #print la repartition de couleur pour les dix premières valeurs
#     best_match = list(matches.items())[0:5]
#     pkl_name, pkl_score = [x[0] for x in best_match], [x[1] for x in best_match]
#     im_name = []
#     means = []
#     for name in pkl_name:
#         splitted = name.split("_")
#         image_name = splitted[2] + "_" + splitted[3][:len(splitted[3])-4] + ".jpg"
#         image = cv2.imread("src/images_desjardin/"+image_name)
#         means.append(color_signature.compute_color_signature(image))
#     # print(pkl_name)
#     # print(pkl_score)
#     for i in range(len(pkl_name)):
#         print([pkl_name[i], pkl_score[i], means[i]])

# img = cv2.imread("src\images_desjardin\IMG_1279.jpg")
# color_signature.compute_color_signature(img)
# color_signature.store_mean_values("src/images_desjardin")