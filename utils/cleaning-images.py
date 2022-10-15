import os
import glob
import cv2
from PIL import Image

'''Return the image shape and its occurrences'''
def im_shape_occurance(dataPath: str) -> list:
	images_sizes = []

	all_files = glob.glob(os.path.join(dataPath, "*.jpg"))

	for file_name in all_files:
		im = cv2.imread(file_name)
		images_sizes.append(im.shape)	

	shapes = [[x, images_sizes.count(x)] for x in set(images_sizes)]

	return shapes

'''Find the duplicate images and return only the different images'''
def im_comparator(dataPath: str) -> list:
	unique_images = []
	all_files = glob.glob(os.path.join(dataPath, "*.jpg"))
	for count, file_name in enumerate(all_files):
		img = Image.open(file_name)
		img = list(img.getdata())
		if img not in unique_images:
			unique_images.append(img) 
	
		else:
			print (f'redundant image {count}')

	return unique_images

rootDir = os.path.abspath(os.curdir)

imagesPath = rootDir + '\data\original'

shape_list = im_shape_occurance(imagesPath)

for shape_i in shape_list:
	print(shape_i)

similarity_list = im_comparator(imagesPath)

print(f'different images: {len(similarity_list)}')