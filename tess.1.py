# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
from fpdf import FPDF
import random
import datetime
import pytesseract
import argparse
import cv2
import os
import os.path
# crud image
from CrudImage import CrudImage
from Crawler import Crawler


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, default="text2",
	help="name to save file")
ap.add_argument("-i", "--image", required=True, default='images/documento-de-posio-oficial-2012-1-728.jpg, images/ex02.jpg',
	help="path to input image to be OCR'd")
ap.add_argument("-s", "--storage", type=str,
	help="location where to move the files")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

pdf = FPDF()
storage = args['storage']
images = args['image'].split(",")
text = str(datetime.datetime.now())+"\n"
for src in images:
	src = src.strip()
	# print(src)
	if len(src) <= 1:
		break

	# img =Image.open(src)
	# img.show()
	# load the example image and convert it to grayscale
	image = cv2.imread(src)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# check to see if we should apply thresholding to preprocess the
	# image
	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# make a check to see if median blurring should be done to remove
	# noise
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	# filename = "{address}/{name}.png".format(address = "./temp", name = os.getpid())
	filename = "{address}/{name}.png".format(address = '/var/www/html/temp/', name = (random.randint(0,5000)))
	cv2.imwrite(filename, gray)

	newFileName = src.split('/')[-1].split('.')[0]

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	tempImage = Image.open(filename)
	# print(filename)
	text += pytesseract.image_to_string(tempImage)
	#text = text.encode('utf-8')

	width, height = tempImage.size
	if width > height:
		pdf.add_page("L")
		size = 298
	else:
		pdf.add_page("P")
		size = 210
	pdf.image(filename, x = 0, y = 0, w = 210)

	# save image in folder images
	# fileNameImage = "{address}/{name}".format(address = "./images", name = src.split('/')[-1])
	# cv2.imwrite(fileNameImage, image)

	os.remove(filename)

	cv2.waitKey(0)

filename = args["name"]
counter = 1
newFileName = filename
while(os.path.exists(storage+''+newFileName)):
	newFileName = filename+'('+counter+')'
	counter += 1

pdfFileName = storage+''+newFileName+'.pdf'
pdf.output(pdfFileName, 'F')

# Create file txt
newFileName = filename
while(os.path.exists(storage+''+newFileName)):
	newFileName = filename+'('+counter+')'
	counter += 1
arqui = open(storage+''+newFileName+'.txt', 'w')
arqui.write(text)
arqui.close()

# crud = CrudImage()
# filename = pdfFileName.split('/')[-1]
# getIndex = Crawler().insetDocument(filename, text)
print('Ok')
