# -*- coding: utf-8 -*-


# import module 
from pdf2image import convert_from_path
import sys
import os
from PIL import Image

def convert(path):
    print(path)
    # Store Pdf with convert_from_path function 
    images = convert_from_path(os.getcwd()+'\\Faza_1\\'+path, poppler_path = os.getcwd() + "\\Faza_1\\poppler-20.11.0\\bin") 
    n = 1
    for img in images: 
        name = "img_" + str(n) + ".jpg"
        img.save(os.getcwd() +"/Faza_1/prim/" + name, 'JPEG')
        n += 1
    
def in_half():
    fisiere = os.listdir(os.getcwd() +"/Faza_1/prim/")
    for i in fisiere:
        original = Image.open(os.getcwd() +"/Faza_1/prim/"+i)
        
        width, height = original.size   # Get dimensions
        left = 0
        top = height/2
        right = width
        bottom = height
        
        cropped = original.crop((left, top, right, bottom))
        cropped.save(os.getcwd() +"/Faza_1/secund/" + i + "_1.jpg")
        
        width, height = original.size   # Get dimensions
        left = 0
        top = 0
        right = width
        bottom = height/2
        
        cropped = original.crop((left, top, right, bottom))
        cropped.save(os.getcwd() +"/Faza_1/secund/" + i + "_2.jpg")
    
def main(name):
    convert(name)
    in_half()
    
if __name__ == "__main__":
    main(sys.argv[1])