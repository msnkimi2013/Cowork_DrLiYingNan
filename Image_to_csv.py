import cv2
import numpy as np
import csv



image = cv2.imread('your_image.jpg')
# Reshape to a 2D array for each RGB value
pixel_data = image.reshape(-1, 3)  


with open('image_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(pixel_data)
