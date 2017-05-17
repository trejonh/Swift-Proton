import socket
from threading import Thread
import os
import sys

def videoShell(vars):
	print "launching shell"
	os.system("./video.sh")
	
def controllerSocket():
	HOST = ''                 # Symbolic name meaning all available interfaces
	PORT = 9000              # Arbitrary non-privileged port
	CONTROLLER_PORT = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, CONTROLLER_PORT))
	s.listen(1)
	conn, addr = s.accept()
	while True:
		data = s.recv(12)
		print data
	s.close()
	sys.exit()

if __name__ == "__main__":
	try:
		thread =Thread(target=videoShell,args=1234)
		thread.start()
		controllerSocket
	except:
	print "unable to start threads"
