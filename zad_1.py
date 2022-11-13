# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:29:48 2022

@author: Jakub
"""

import cv2
import pytesseract
import matplotlib.pyplot as plt


#pytesseract.pytesseract.tesseract_cmd = "C:/Users/Jakub/AppData/Local/Tesseract-OCR/tesseract"
pytesseract.pytesseract.tesseract_cmd = "C:/Users/student/AppData/Local/Tesseract-OCR/tesseract"

images = {}
for i in range(1, 6):
    filename = "original{}.jpg".format(i)
    images[i] = cv2.imread(filename)

def im_extracttext(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    return data


for key in images.keys():
    print("Tekst z obrazka nr {}: ".format(key))
    print(im_extracttext(images[key]))
