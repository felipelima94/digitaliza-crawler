# API Python

##Intall tesseract
#####On Ubuntu
	$ apt-get install tesseract-ocr-por

##Instalar pip
#####pip3 On Ubuntu
	$ apt-get install python3-pip

##Install OpenCV
https://github.com/jazzsaxmafia/video_to_sequence/issues/3
#####On Ubuntu
	$ apt-get install python-opencv
#####Python
	> pip3 install opencv-python

###Install Pytesseract
	> pip3 install pytesseract
	
###Install Pillow
	> pip3 install pillow

###Install Nltk
	> pip3 install nltk
	> python -m nltk.downloader all

###Install pyfpdf: FPDF for Python
	> pip3 install fpdf
	
##Exemple of use
	> python3 tess --image 'img1, ...' --name 'filename'
Return `id` of file

Command | Values
--------|-------
--image| list of address of images separated with `,` comma and between apostrophe
|exemple `--image 'img-src1, img-src2, ...'`
|
--name | File name to be saved
|
Return | The return is the ID `(int)` of inserted file in database
