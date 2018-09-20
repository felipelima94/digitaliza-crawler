import argparse
# from Connection import Connection
from CrudImage import CrudImage
from Crud import Crud

ap = argparse.ArgumentParser()
ap.add_argument("-g", "--get", type=str,
	help="Inform the select")
ap.add_argument("-f", "--find",
    help="Inform the select")
args = vars(ap.parse_args())

def main():
    print("Main")
    
    if args["get"] == "all":
        images = Crud().getAll("tess")
    else:
        images = Crud().findOne("tess", args["find"])

    for x in images:
        print("Id: {id}".format(id = x[0]))
        print("File Name: {filename}".format(filename = x[1]))
        print("Text: {text}".format(text = x[2]))
        print("\n//  --  //  --------  //  --------   //  -------  // --  //\n")

main()
