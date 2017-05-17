import socket
import thread
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
	 thread.start_new_thread(videoShell,1234)
	except:
		print "unable to start threads"
	controllerSocket()