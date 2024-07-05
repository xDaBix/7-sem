#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:32:09 2024

@author: bmiit202106100110091
"""

import cv2
import mahotas
import numpy as np 
img=mahotas.imread('images.jpeg')
img=img[:,:,0]
print("image with filter")
cv2.imshow("winname", img)
mean=img.mean()
print("Mean Value  : " + str(mean))
cv2.waitKey(0)
cv2.destroyAllWindows()