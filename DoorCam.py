import config
import os
import cv2
from time import sleep, localtime, strftime

# Get settings from config
USER = config.getConfigSetting('IPCam', 'username')
PSWD = config.getConfigSetting('IPCam', 'password')
ADDR = config.getConfigSetting('IPCam', 'address')
PORT = config.getConfigSetting('IPCam', 'port')

address = 'rtsp://'+ADDR+':'+PORT+'/user='+USER+'&password='+PSWD+'&channel=1&stream=0'
dirname = '/home/pi/Code/img/static'

def capture_cam_image():
    cap = cv2.VideoCapture(address)
    imgPath = ""
    if(cap.isOpened()):
        _, frame = cap.read()
        cv2.imshow('frame', frame)
        #The recieved " frame"  will be saved. Or you can manipulate " frame" as per your needs.
        name = "door_cam_" +strftime('%Y%m%d%H%M%S')+".jpg"
        imgPath = os.path.join(dirname,name)
        cv2.imwrite(imgPath, frame)
        
    cap.release()
    cv2.destroyAllWindows()

    return imgPath
