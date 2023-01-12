import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     #https://github.com/UB-Mannheim/tesseract/wiki
signs = ["x","/","+","-","*"]
mistakes = ["x","l","|","z","s","%","o"]
correction = ["*","1","1","2","5","*","0"]

camera = cv2.VideoCapture(0)
n = 0
while True:
    n += 1
    #❓❓❓<INSERT CAMERA CAPTURE 🔥>
    #❓❓❓<INSERT CAMERA CAPTURE 🔥>     #Ensure that you have a camera installed or errors will be faced
    
    if n % 45 == 0:         #Every 45 frames, process the captured image
        
        """ <-- Remove this 👍 (After you are done)

        new_image = cv2.❓❓❓                  #Tesseract works best on images which have a DPI of at least 300 dpi, so resizing can increase accuracy
        img = cv2.❓❓❓                        #Converting to Grayscale
        kernel = np.ones((2,2), np.uint8)
        img = cv2.❓❓❓                        #iterations --> how many times applied
        img = cv2.❓❓❓
        img = cv2.❓❓❓
        img = cv2.❓❓❓

        Remove this 👍 -->""" 

        img = cv2.threshold(img, 0, 255, ❓❓❓ + ❓❓❓)[1]

        bordered_img= cv2.❓❓❓(img,30,30,30,30,❓❓❓,value=[255,255,255])       #Add white border for better accuracy

        cv2.imwrite(r"python-opencv\MathPhoto\eqn.jpg",bordered_img)     #Writing the image out to see what it looks like

        equation = pytesseract.❓❓❓(bordered_img).lower()               #lower X -> x
        print("Original Text:", equation)
        for c in equation:
            if not c.❓❓❓ and c not in ❓❓❓:
                equation = equation.replace(c,"")       #Removing noise from equation

        if any(c in equation for c in signs) != True:
            print("No equations found!")
            continue

        else:
            for i in range(len(mistakes)):
                equation = equation.replace(mistakes[i],correction[i])      #Correcting frequently misread text
            try:
                print(f"{equation} = {eval(equation)}\n")
            except Exception as e:                      #In case of any errors E.g. Division by 0
                print(e, "\n")

    if cv2.waitKey(1) == ord(❓❓❓):     #Toggle set on Spacebar to end video capture
        break

camera.release()
cv2.destroyAllWindows()