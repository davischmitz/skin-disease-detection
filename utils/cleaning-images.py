import os
import glob
import cv2

'''Return the image shape and its occurrences'''
def im_shape_occurance(dataPath: str) -> list:
	images_sizes = []

	all_files = glob.glob(os.path.join(dataPath, "*.jpg"))

	for file_name in all_files:
		im = cv2.imread(file_name)
		images_sizes.append(im.shape)	

	shapes = [[x, images_sizes.count(x)] for x in set(images_sizes)]

	return shapes

rootDir = os.path.abspath(os.curdir)

imagesPath = rootDir + '\data\image'

shape_list = im_shape_occurance(imagesPath)

for shape_i in shape_list:
	print(shape_i)