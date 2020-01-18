import cv2
import numpy as np
from PIL import ImageGrab
#using python imaging library

# screen _size = (1440,900)
img = ImageGrab.grab()
img_np = np.array(img)
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
cv2.imshow("frame",frame)
cv2.waitKey(0)w
# cv2.destroyAllWindows()
