import cv2
import numpy as np
import pyautogui


#take a screenshot of a small region
while True:
    
    image = pyautogui.screenshot(region=(600,885,255,250))
    #convert screenshot into numpy array
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    #count pixel
    black_pixel_count = np.sum(image < 100) #if any pixel value less than 100 will be taken as black
    white_pixel_count = np.sum(image > 100) #if any pixel value more than 100 will be taken as black

    #print pixel value for reference
    
    #print('Number of black pixels : ', black_pixel_count)
    print('Number of white pixels : ', white_pixel_count)
    #check pixel value
    #for light mode -> black pixel count should be 4000 to 30000
    if black_pixel_count > 4700 and black_pixel_count < 30000:
        pyautogui.press('up')
    
    #for dark mode -> white pixel count should be 4000 to 30000
    if white_pixel_count > 4700 and white_pixel_count < 30000:
        pyautogui.press('up')

    #display image
    cv2.imshow('image',image)
    if cv2.waitKey(25) &0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
