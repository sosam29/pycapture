import cv2
import time,threading
#print(cv2.__version__)

cap= cv2.VideoCapture(0)
w= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


writer = cv2.VideoWriter('/home/pi/Videos/basicvideo.mp4', cv2.VideoWriter_fourcc(*'H264'),20, (w,h))
ret, fra= cap.read()

def cameracapture():
    print("starting new capture {}".format(time.ctime()))
    
    
    if fra is None:
        print("no stream available")
        exit
    writer.write(fra)
    #gray= cv2.cvtColor(fra, cv2.COLOR_RGB2GRAY)
    #cv2.imshow("img",fra)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit
    #print('releasecamera')
    #cap.release()
        
        
def startrecording():
    print(time.ctime())
    threading.Timer(10, cameracapture).start()

startrecording()

cap.release()
cv2.destroyAllWindows()
