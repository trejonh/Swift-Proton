import socket
import threading
import os
import sys
import time
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy

running = True

def videoShell():
	# initialize the video stream and allow the cammera sensor to warmup
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)
		# loop over the frames from the video stream
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 9000              # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print "video streaming"
	while running:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=320)

		# draw the timestamp on the frame
		#timestamp = datetime.datetime.now()
		#ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
		#cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		#	0.35, (0, 0, 255), 1)

		# show the frame
		#cv2.imshow("Frame", frame)
		encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)  
        data = numpy.array(imgencode)  
        stringData = data.tostring() + "\r\n"
        #conn.sendall( str(len(stringData)).ljust(16));  
        conn.sendall( stringData );  

	# do a bit of cleanup
	cv2.destroyAllWindows()
	s.close()
	vs.stop()
	
def controllerSocket():
	HOST = ''                 # Symbolic name meaning all available interfaces
	CONTROLLER_PORT = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, CONTROLLER_PORT))
	s.listen(1)
	conn, addr = s.accept()
	while running:
		data = conn.recv(12)
		print data
	s.close()

if __name__ == "__main__":
	#try:
	t = threading.Thread(target=videoShell)
	t.start()
	t1 = threading.Thread(target=controllerSocket)
	t1.start()
	while running:
		q = raw_input("enter q to quit")
		if q=="q":
			running = False
	#except:
	#	print "unable to start threads"
