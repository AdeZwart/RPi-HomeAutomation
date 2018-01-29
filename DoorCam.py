import ProjectConfigParser
import cv2

class DoorCam:
    """Class to retrieve a frame from an IP Cam RTSP stream"""
    
    def __init__(self)
        self.config = ProjectConfigParser.parser()
        
        # Get settings from config
        self._user = config.getConfigSetting('IPCam', 'username')
        self._pswd= config.getConfigSetting('IPCam', 'password')
        self._addr = config.getConfigSetting('IPCam', 'address')
        self._port = config.getConfigSetting('IPCam', 'port')        
        
        # Compile the complete address
        self.address = 'rtsp://'+_addr+':'+_port+'/user='+_user+'&password='+_pswd+'&channel=1&stream=0'        
        # Retrieve the image destination path
        self.imgpath = config.getconfigSetting('IPCam', 'imagepath')

    def captureFrame(self):
        cap = cv2.VideoCapture(self.address)
        imgFileName = "door_cam.jpg"
        
        if(cap.isOpened()):
            _, frame = cap.read()
            cv2.imshow('frame', frame)            
            imgFileFullPath = os.path.join(self.imgpath,name)
            cv2.imwrite(imgFileFullPath, frame)
            
        cap.release()
        cv2.destroyAllWindows()

        return imgFileFullPath
