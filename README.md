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
```python
	> pip3 install pillow
```

###Install Nltk
```python
	> pip3 install nltk
	> python -m nltk.downloader all
```
###Install pyfpdf: FPDF for Python
```python
	> pip3 install fpdf
```
####Exemple of use
```python
	> python3 tess --image 'img1, ...' --name 'filename'
```
Return `id` of file