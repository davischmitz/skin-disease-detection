# functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc
import os

# used to return all file paths that match a specific pattern
import glob

# opencv-python, solve computer vision problems
import cv2

# import pytorch as pyt
from PIL import Image, ImageOps

# pacote de álgebra linear, faz manipulações de vetores e etc
import numpy as np

''' Resize and apply grayscale to the image vector 'images_df' stored on the directory 'path' '''
def process_image(path: str, images_df: object) -> list:
	processed = []

	for img_name in images_df:
		img = cv2.imread(path + str(img_name)+'.jpg')
		resized_image = cv2.resize(img, (200, 150))
		img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
		
		ph = np.ones((img.shape[0], img.shape[1], 1), dtype='uint8')
		ph[:,:,0] = img
		processed.append(ph)

	return processed

''' Save the processed images 'processed_imgs' with the names 'images_name_df' in the directory 'path' '''
def save_image(path: str, images_name_df: object, processed_imgs: object):
	for img_name, processed_img in zip(images_name_df, processed_imgs):
		cv2.imwrite(path + str(img_name) + '.jpg', processed_img)
