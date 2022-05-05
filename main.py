import sys
import os

if __name__ == "__main__":
    script1='python3 '+os.getcwd()+'\\Faza_1\\pdf_to_photos.py '+sys.argv[1]
    print(script1)
    os.system(script1)
    print("Faze 1 done")
    for i in os.listdir(os.getcwd()+'\\Faza_1\\secund'):
        image_name=os.getcwd()+"\\Faza_1\\secund\\"+i
        script2='python3 '+os.getcwd()+'\\Faze_2\\ocr.py '+image_name
        os.system(script2)