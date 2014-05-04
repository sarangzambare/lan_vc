import cv
import socket


s = socket.socket()

capture = cv.CaptureFromCAM(0)


s.bind(('localhost',12345))
s.listen(5)
print 'Waiting for the client to Connect...'

conn,addr = s.accept()

print 'Got Conection from ' + str(addr)


while True:
	frame = cv.QueryFrame(capture)
	conn.send(frame.tostring())
	c = cv.WaitKey(1)
	if(c == 'q'):
		break
	
	

print 'Image Sent with size= ' + str(len(frame.tostring()))

s.close()





