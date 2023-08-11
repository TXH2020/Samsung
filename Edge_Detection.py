import cv2 as cv
import numpy as np
from cv2 import VideoCapture
from cv2 import waitKey

camera = VideoCapture(0)

while True:
    _, frame = camera.read()
    #Output of Normal Camera
    
    cv.imshow('Camera',frame)

    #Output from Laplacian Filter
    
    laplacian = cv.Laplacian(frame , cv.CV_64F)
    #laplacian = np.unit8(laplacian)
    cv.imshow('Laplacian',laplacian)
    
    #Output from Canny Filter
    
    edges = cv.Canny(frame , 200 , 200)
    cv.imshow('Canny', edges)
    
    #Output from Sobel Filter

    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY).astype(float)
    edge_x = cv.Sobel(frame , cv.CV_64F,1,0,ksize=3)
    edge_y = cv.Sobel(frame , cv.CV_64F,0,1,ksize=3)    
    edge = np.sqrt(edge_x**2 + edge_y**2) 
    cv.imshow('Sobel' , edge)

    if cv.waitKey(5) == ord('x'):
        break


camera.release()
cv.destroyAllWindows() 
