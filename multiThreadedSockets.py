#!/usr/bin/python

import thread
import time
import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import robot

HOST = ''                 # Symbolic name meaning all available interfaces
VIDEOPORT = 9000              # Arbitrary non-privileged port
CONTROLLERPORT = 8000              # Arbitrary non-privileged port

def videoStreamSocket():
	cap = cv2.VideoCapture(0)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, VIDEOPORT))
	s.listen(1)
	conn, addr = s.accept()
	while True:
		ret,frame = cap.read()
		data = pickle.dumps(frame)
		print lens(data)
		try:
			s.sendall(struct.pack("L", len(data)) + data)
		except:
			break
	s.close()
	cap.release()

def controllerSocket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, CONTROLLERPORT))
	s.listen(1)
	conn, addr = s.accept()
	#robot = robot.Robot()
	while True:
		data = s.recv(12)
		print lens(data)
		print data
		
if __name__ == "__main__":
	try:
	 thread.start_new_thread(videoStreamSocket)
	 thread.start_new_thread(controllerSocket)
	except:
		print "unable to start threads"