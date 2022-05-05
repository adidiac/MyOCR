from turtle import pen
import json
import cv2 
import pytesseract
from PIL import Image
import pickle
import sys
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
def get_text(name,h_init,h_final,width_init,width_final):
    number=1
    im = Image.open(name)
    pixelMap = im.load()
    img = Image.new( im.mode, (1700,1100))
    pixelsNew = img.load()
    for i in range(width_init,width_final):
        for j in range(h_init,h_final):
            pixelsNew[i,j] = pixelMap[i,j]

    # #deploy
    img.save(os.getcwd()+"\\Faze_2\\crops\\new"+str(number)+".jpg")

    img = cv2.imread(os.getcwd()+"\\Faze_2\\crops\\new"+str(number)+".jpg")

    #test
    # img.save(os.getcwd()+"\\crops\\new"+str(number)+".jpg")

    # img = cv2.imread(os.getcwd()+"\\crops\\new"+str(number)+".jpg")

    custom_config = r'--oem 3 --psm 6'
    output=pytesseract.image_to_string(img, config=custom_config)
    return output.encode('utf-8').strip().decode('utf-8')
def main(path):
    w=1700
    h=1100
    name=get_text(path,0,93,0,w)
    print(name)
    orar=[[],[],[],[],[],[],[],[],[],[]]
    coords=[]
    with open(os.getcwd()+"\\Faze_2\\coord.txt", "r") as fp:
        lines=fp.readlines() 
        for line in lines:
            coords.append(line.strip().split(','))
        for i in range(len(coords)):
            for j in range(len(coords[i])):
                coords[i][j]=int(coords[i][j])
    text=[]
    for i in range(0,len(coords),2):
        t=get_text(path,coords[i][1],coords[i+1][1],coords[i][0],coords[i+1][0])
        t=t.replace('|','')
        t=t.replace('—','')
        t=t.replace('/','')
        text.append(t)

    orar={'groupName':name,'orar':[]}
    for i in range(0,len(text),7):
        print("Day: "+text[i])
        orar['orar'].append({'day':text[i],'lessons':[]})
        modules=['08:00-09:50','10:00-11:50','12:00-13:50','14:00-15:50','16:00-17:50','18:00-19:50']
        for j in range(i+1,i+7):
            splitted=text[j].split('\n')
            if(len(splitted)==1):
                orar['orar'][-1]['lessons'].append({'lesson':'free','prof':'','room':'','time':modules[j-i-1]})
            else:
                lesson=splitted[0]
                splitted1=splitted[1].split(' ')
                if(len(splitted1)==1):
                    orar['orar'][-1]['lessons'].append({'lesson':lesson,'prof':splitted1[0].strip(),'room':'','time':modules[j-i-1]})
                else:   
                    #eliminate from splitted1 the '' elements
                    splitted1=[x for x in splitted1 if x!='']
                    room=''
                    prof=''
                    if(len(splitted1)>2):
                        if(len(splitted1[1])==2):
                            room=splitted1[0].strip()+'-'+splitted1[1].strip()
                            prof=splitted1[2].strip()
                        else:
                            room=splitted1[0].strip()
                            prof=splitted1[1].strip()+'-'+splitted1[2].strip()
                    else:
                        room=splitted1[0].strip()
                        prof=splitted1[1].strip()
                    orar['orar'][-1]['lessons'].append({'lesson':lesson,'prof':prof,'room':room,'time':modules[j-i-1]})

    #print(orar)
    with open(os.getcwd()+"\\Faze_2\\orar.json", 'r+') as json_file:
        file_data = json.load(json_file)
        file_data.append(orar)
        json_file.seek(0)
        json.dump(file_data, json_file, 
                            indent=4,  
                            separators=(',',': '))
if __name__ == "__main__":
    main(sys.argv[1])