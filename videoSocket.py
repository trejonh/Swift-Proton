import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap = cv2.VideoCapture(0)
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9000              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
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