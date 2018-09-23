import argparse
from fpdf import FPDF
from PIL import Image
# from Connection import Connection
from CrudImage import CrudImage
from Crud import Crud

ap = argparse.ArgumentParser()
ap.add_argument("-g", "--get", type=str,
	help="Inform the select")
ap.add_argument("-f", "--find",
    help="Inform the select")
ap.add_argument("-i", "--image",
    help="path to input image to be OCR'd")
args = vars(ap.parse_args())

def main():
    print("Main")
    
    if args["get"] == "all":
        images = Crud().getAll("tess")
    else:
        images = Crud().findById("tess", args["find"])

    print("Id: {id}".format(id = images[0]))
    print("File Name: {filename}".format(filename = images[1]))
    print("Text: {text}".format(text = images[2]))
    print("\n//  --  //  --------  //  --------   //  -------  // --  //\n")

def convert2PDF(image):
    img = Image.open(image)
    pdf = FPDF()
    # compression is not yet supported in py3k version
    pdf.compress = False
    pdf.add_page('L')
    pdf.image('images/imagens-de-amor-textos-romanticos-8.jpg', x = 0, y = 0, w = 298, h = 0)
    pdf.add_page('P')
    pdf.image('images/ex02.jpg', x = 0, y = 0, w = 210, h = 0)

    pdf.add_page()
    pdf.image(image, 0, 0)
    
    pdf.output('py3k.pdf', 'F')

# convert2PDF(args["image"])
files = args['image'].split(',')
for file in files:
    file = file.strip()
    print(file)