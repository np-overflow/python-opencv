## Referenced From Chua Jie Yi, Addison
## For Overflow OpenCV Session

#OpenCV
import cv2 as cv
import numpy as np
from time import time,sleep

#Screencap (Can use win32 to capture screenfaster ; more complex (bitmap & stuff))
from PIL import ImageGrab

#Keyboard Emulation
import pyautogui as pag

looptime = time() # Time Bookmark
while True:
    # ScreenGrabbing
    img = ImageGrab.grab(bbox=(120,400,350,800)) #bbox default = whole screen | (left_x, top_y, right_x, bottom_y)
    
    img_arry = np.array(img) # Convert Image to an array ; so open CV can understand
    img_grey = cv.cvtColor(img_arry, cv.COLOR_BGR2GRAY) # Convert to greyscale
    

    # Compare Images (Screencap vs cactus template)
    template = cv.imread(r'.\template\catc1.png',0) #0 parameter = read image in greyscale mode

    result = cv.matchTemplate(img_grey,template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    threshold = 0.3
    cactusFound = False
    if max_val >= threshold:
        print("Found Cactus")
        pag.press('space') # Keyboard Input (if cactus is found; emulate key press)


    # FPS (How many time segments can fit within 1 second)
    print('FPS {}'.format(1/(time() - looptime))) # Compare current time to initial starting time of the first bookmark 
    looptime = time()

    
    cv.imshow("",result) # Show screencaptured images (videos = buch of photos (frames)) [result,img_arry]


    # Exit ;
    if cv.waitKey(1) == 27: 
        break #Keybaord key ID ; 27 = esc

cv.destroyAllWindows()
