import cv2 as cv
import numpy as np
import os, os.path

def read_img(file):
    return cv.imread(file)
    
def get_file_list():
    file_list = []
    for root, dirs, files in os.walk('./Dataset'):
	    for file in files:
		    file_list.append(os.path.join(root,file))