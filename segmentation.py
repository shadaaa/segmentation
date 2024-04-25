#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
image = cv2.imread("C:/Users/ASUS/OneDrive/Desktop/segm.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)



# In[2]:


contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
segmented_image = image.copy()
cv2.drawContours(segmented_image, contours, -1,(0,0,255),2)


# In[3]:


cv2.imshow('Image',segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




