import cv2
from matplotlib import pyplot as plt
import numpy as np

def compute_color_signature(img):
    b, g, r = cv2.split(img)
    b_mean, g_mean, r_mean = b.mean(), g.mean(), r.mean()