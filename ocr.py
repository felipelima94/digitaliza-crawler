# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
# crud image
from CrudImage import CrudImage

# pytesseract.pytesseract.tesseract_cmd = "D:\\femax\\Desktop\\a\\pytesseract-master\\src"

# tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR"
# tessedata_dir_config = '--tessedata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Image", gray) // mostra imagem inicial ao carregar

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
filename = "{address}/{name}.png".format(address = "./temp", name = os.getpid())
cv2.imwrite(filename, gray)

newFileName = args["image"].split('/')[-1].split('.')[0]

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
#text = text.encode('utf-8')

# Create file txt
arqui = open('./text/'+newFileName+'.txt', 'w')
arqui.write(text)
arqui.close()

# save image in folder images
fileNameImage = "{address}/{name}".format(address = "./images", name = args["image"].split('/')[-1])
cv2.imwrite(fileNameImage, image)

os.remove(filename)
# print(text)

crud = CrudImage()
filename = args["image"].split('/')[-1]
getIndex = crud.insert(filename, text)
print(getIndex)

# show the output images
# cv2.imshow("Image", image)

#cv2.imshow("Output", gray) #// mostra imagem final apos processamento
cv2.waitKey(0)
