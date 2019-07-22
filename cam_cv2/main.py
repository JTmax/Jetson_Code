#from cam import Camera 
import cv2

cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3820, height=2464, format=NV12, framerate=21/1 ! nvvidconv ! video/x-raw, width=960, height=616, format=BGRx ! videoconvert ! appsink' , cv2.CAP_GSTREAMER)

while(True):
	ret, frame = cap.read()
	
	flip = cv2.flip(frame, -1)

	cv2.imshow('frame', flip)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
