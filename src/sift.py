import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import json
import pickle
import time

def find_sift(img):
    """
    this method return sift descriptors for the image img

    arguments:

        ---> img is an opencv image in grayscale
    """
    sift = cv2.SIFT_create()
    features = sift.detect(img, None)
    list_features = [{"angle": feature.angle, "response": feature.response} for feature in features]
    

    return features, list_features

def apply_Lowe_test(matches, threshold):
    good = []
    try:
        for m, n in matches:
            # utiliser les valeur de m.distance et n.distance pour faire un test de Lowe
            # En ce moment, tous les matchs vont être retournés.
            if((m.distance/n.distance) < threshold):
                good.append(m)

    except ValueError:
        pass
    return good


def find_match_orb(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orb_img  = cv2.ORB_create(500) #create opencv orb object for the image to identify
    FLANN_INDEX_LSH = 6
    index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=50)
    flann_img = cv2.FlannBasedMatcher(indexParams=index_params, searchParams=search_params)
    #load the path of all the reference images
    list_path = os.listdir("src/images")
    #compute the keypoints for the image
    kp_img, des_img = orb_img.detectAndCompute(img, None)
    matches = []
    for path in list_path:
        if path == "cropped": continue
        abs_path = "src/images/"+path
        img_ref = cv2.imread(abs_path)
        img_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)
        #copute the keypoints for the reference images
        kp_ref, des_ref = orb_img.detectAndCompute(img_ref, None)
        #find the matches
        matches1 = flann_img.knnMatch(des_img, des_ref, k=2)
        matches.append(apply_Lowe_test(matches1, 0.7))
        # matches.append(apply_Lowe_test(matches1, 0.0001))
        score_matched = [len(x) for x in matches]
   

    test = dict(zip(list_path, score_matched)) 
    sorted_values = {k: v for k, v in sorted(test.items(), key=lambda item: item[1],reverse=True)}
    print(sorted_values)


def find_match_sift(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Initiate SIFT detector
    sift = cv2.SIFT_create()
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    #load the path of all the reference images
    list_path = os.listdir("src/images")
    matches = []
    kp1, des1 = sift.detectAndCompute(img,None)
    for path in list_path:
        if path == "cropped": continue
        abs_path = "src/images/"+path
        img_ref = cv2.imread(abs_path)
        img_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)
        kp2, des2 = sift.detectAndCompute(img_ref,None)
        matches_basic = bf.knnMatch(des1,des2,k=2)
        matches.append(apply_Lowe_test(matches_basic, 0.7))
        score_matched = [len(x) for x in matches]
   

    test = dict(zip(list_path, score_matched)) 
    sorted_values = {k: v for k, v in sorted(test.items(), key=lambda item: item[1],reverse=True)}
    print(sorted_values)

def generate_sift_descrpitors(folder_path):
    list_images = os.listdir("src/"+folder_path)
    sift = cv2.SIFT_create(1000)
    for image in list_images:
        print(image)
        img = cv2.imread("src/"+folder_path + "/" + image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kp, des = sift.detectAndCompute(img, None)
        # print(type(des))
        # sift_descriptors[image] = des.tolist()
        pickle_name = "src/sift_descriptors/sift_descriptor_"+image[:len(image)-4] +".pkl"
        with open(pickle_name, "wb") as file:
            pickle.dump(des, file)
    

def find_match_sift_from_pkl(img):
    """
    this method return the list of all the reference images from the most probable to the less one

    arguments: 

        -->img a bgr image from witch we want to find the match
    """
    start = time.time()
    #convert the image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     # Initiate SIFT detector
    sift = cv2.SIFT_create(1000)
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    #load the path of all the reference images
    list_path = os.listdir("src/sift_descriptors")
    matches = []
    kp1, des_test = sift.detectAndCompute(img,None)
    for des_path in list_path:
        with open("src/sift_descriptors/"+des_path[0:len(des_path)-4]+".pkl", "rb") as file:
            des_ref = pickle.load(file)
        matches_basic = bf.knnMatch(des_test,des_ref,k=2)
        matches.append(apply_Lowe_test(matches_basic, 0.7))
        score_matched = [len(x) for x in matches]
    
    test = dict(zip(list_path, score_matched)) 
    sorted_values = {k: v for k, v in sorted(test.items(), key=lambda item: item[1],reverse=True)}
    end = time.time()
    print(end-start)
    print(sorted_values)


