import cv2
import time
from datetime import  datetime, timedelta
import os

import shutil

x=1
starttime= datetime.now()
print("start time {}".format(starttime))
terminateby = starttime + timedelta(hours=8)
print("terminateby time {}".format(terminateby))

while(True):
    # Capture frame-by-frame
    cap = cv2.VideoCapture(0)
    framerate = cap.get(30)
    ret, frame = cap.read()
    cap.release()
    # Our operations on the frame come here
    fmtdate=datetime.now()
    fmtprint=fmtdate.strftime('%m%d%Y%H%M%S')

    print(fmtprint)
    path='/mnt/mydisk/Pictures'
 #   os.makedirs(path, exist_ok=True)
  #  if os.path.isdir(path):
   #     print("directory exists")
   # else:
    #    print("Directory does not exists, Existing ...")
    #    exit -1
    finame=str(fmtprint)+".png"
    
    filename = '/mnt/mydisk/Pictures/'+finame
    #x=x+1
    print(filename)
    #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #inverted = cv2.bitwise_not(gray)
    half= cv2.resize(frame, (0,0), fx=0.2, fy=0.2)
    try:
        cv2.imwrite(finame, half)
        shutil.copy(finame,filename)
#        print("file copied")
        os.remove(finame)
    except Exception as e:
        print(e)
 #   if os.path.isfile(filename):
 #      print("file exists")
  #  else:
  #      print("file does not exist")
    endtime= datetime.now()
   # print("end time {}".format(endtime))
    
    if endtime > terminateby:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(30)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("all cleaned. Closing...")
