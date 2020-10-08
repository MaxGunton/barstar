import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../images/cocktails.jpg', cv2.IMREAD_UNCHANGED)

reds = image[:,:,0]  # reds
red_hist = np.histogram(reds, 255)

blues = image[:,:,1]  # blues
blue_hist = np.histogram(blues, 255)

greens = image[:,:,2]  # greens
green_hist = np.histogram(greens, 255)


# plt.plot(green_hist[0])
# plt.show()

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()