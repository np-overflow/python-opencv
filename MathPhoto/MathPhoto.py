import cv2
import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     #https://github.com/UB-Mannheim/tesseract/wiki
signs = ["x","/","+","-","*"]
mistakes = ["x","l","|","z","s","%","o"]
correction = ["*","1","1","2","5","*","0"]

camera = cv2.VideoCapture(0)
n = 0
while True:
    n+=1
    _,img = camera.read()
    cv2.imshow('Text detection', img)     #ensure that you have a camera installed or else this wont work
    
    if n % 30 == 0:         #might want to increase this 30 number if ur computer is too slow
    
        new_image = cv2.resize(img, (400,400))      #Tesseract works best on images which have a DPI of at least 300 dpi, so it may be beneficial to resize images
        img = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)       #grayscale the entire image
        kernel = np.ones((1,1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.GaussianBlur(img, (5,5), 0)
        img = cv2.medianBlur(img,5)

        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        bordered_img= cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_CONSTANT,value=[255,255,255])       #Add white border for better accuracy

        cv2.imwrite('eqn.jpg',bordered_img)     #can write the image out to see what it looks like

        equation = pytesseract.image_to_string(bordered_img).lower()       #lower X -> x
        print("pre processed:", equation)

        for c in equation:
            if not c.isnumeric() and c not in signs:
                equation = equation.replace(c,"")       #getting rid of all the useless stuff

        if any(c in equation for c in signs) != True:
            print("No equations found gg")
            continue

        else:
            for i in range(len(mistakes)):
                equation = equation.replace(mistakes[i],correction[i])      #commonly misread numbers by tesseract
            print(equation)
            try:
                print(f"{equation}={eval(equation)}")
            except Exception as e:
                print(e)

            
            #for c in equation:         #check if symbol is surrounded by numbers, remove all other symbols that are not, then do the eqn
            #    pass

    if cv2.waitKey(1) & 0xFF==ord(' '):
        break




