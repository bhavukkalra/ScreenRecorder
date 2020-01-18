import cv2
import numpy as np

import pyautogui

output = "video1.avi"
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 8.0, (width, height))

while(True):
 try:

  img = pyautogui.screenshot()
  image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  out.write(image)
  StopIteration(0.5)
 except KeyboardInterrupt:
   print("interrupted")
   break



  

out.release()
cv2.destroyAllWindows()