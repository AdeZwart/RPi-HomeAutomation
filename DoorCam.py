import config
import os
import cv2

# Get settings from config
USER = config.getConfigSetting('IPCam', 'username')
PSWD = config.getConfigSetting('IPCam', 'password')
ADDR = config.getConfigSetting('IPCam', 'address')
PORT = config.getConfigSetting('IPCam', 'port')

address = 'rtsp://'+ADDR+':'+PORT+'/user='+USER+'&password='+PSWD+'&channel=1&stream=0'
print(address)

dirname = '/home/pi/Code/img/static'
cap = cv2.VideoCapture(address)
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    else:
        cv2.imshow('frame', frame)
        #The recieved " frame"  will be saved. Or you can manipulate " frame" as per your needs.
        name = " rec_frame" +str(count)+".jpg"
        cv2.imwrite(os.path.join(dirname,name), frame)
        count +=1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

        
