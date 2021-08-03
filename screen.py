import cv2
import numpy as np
import pyautogui
import datetime
from win32api import GetSystemMetrics
import time

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
dimension = (w,h)
dateTime = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
# resolution = (1920,1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = dateTime+ ".avi"
fps= 30.0
out = cv2.VideoWriter(filename,codec,fps,dimension)
now = time.time()

# If time specified before
# duration= 10
# duration = int(input("Please tell us in sec: "))
# duration += duration
# end_time= now+duration

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    # If time specified before
    # current_time = time.time()
    
    cv2.imshow("Live", frame)
    
    # If time specified before
    # if end_time > current_time :
    if cv2.waitKey(10) == ord('q'):
        break

out.release()
cv2.destroyAllWindows

