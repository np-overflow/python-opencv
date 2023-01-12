from __future__ import print_function
import cv2
import numpy as np
 
def main():
    """
    Main method of the program.
    """
 
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
 
    # Create the background subtractor object
    # Use the last 700 video frames to build the background
    back_sub = cv2.❓❓❓
 
    # Create kernel for morphological operation
    # You can tweak the dimensions of the kernel
    # e.g. instead of 20,20 you can try 30,30.
    kernel = np.ones((20,20),np.uint8)
 
    while(True):
 
        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.
        ret, frame = cap.read()
 
        # Use every frame to calculate the foreground mask and update
        # the background
        fg_mask = ❓❓❓
 
        # Close dark gaps in foreground object using closing
        fg_mask = ❓❓❓
 
        # Remove salt and pepper noise with a median filter
        fg_mask = ❓❓❓ 
         
        # Threshold the image to make it either black or white
        _, fg_mask = ❓❓❓
 
        # Find the index of the largest contour and draw bounding box
        fg_mask_bb = fg_mask
        contours, hierarchy = ❓❓❓
        areas = [cv2.contourArea(c) for c in contours]
 
        # If there are no countours
        if len(areas) < 1:
 
            # Display the resulting frame
            cv2.imshow('frame',frame)
 
            # If "q" is pressed on the keyboard, 
            # exit this loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
 
            # Go to the top of the while loop
            continue
 
        else:
            # Find the largest moving object in the image
            max_index = np.argmax(areas)
 
        # Draw the bounding box
        cnt = contours[max_index]
        x,y,w,h = ❓❓❓
        cv2.rectangle(❓❓❓)
 
        # Draw circle in the center of the bounding box
        x2 = x + int(w/2)
        y2 = y + int(h/2)
        cv2.circle(❓❓❓)
 
        # Print the centroid coordinates (we'll use the center of the
        # bounding box) on the image
        text = "x: " + str(x2) + ", y: " + str(y2)
        cv2.putText(❓❓❓)
         
        # Display the resulting frame
        cv2.imshow('frame',frame)
 
        # If "q" is pressed on the keyboard, 
        # exit this loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    # Close down the video stream
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    print(__doc__)
    main()
