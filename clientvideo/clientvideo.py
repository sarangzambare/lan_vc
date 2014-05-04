import cv
import socket
#10.4.192.63
s = socket.socket()

cv.NamedWindow('Client',cv.CV_WINDOW_AUTOSIZE)
imgframe = cv.CreateImage((640,480),cv.IPL_DEPTH_8U,3)

s.connect(('localhost',12345))
while True:
	imgstr = ''
	while True:

		imgstr = "".join((imgstr,s.recv(1048576)))
		if(len(imgstr) ==921600):
			break
	cv.SetData(imgframe,imgstr)

	cv.ShowImage('Client',imgframe)
	c = cv.WaitKey(1)
	if(c == 'q'):
		break
	





s.close()




