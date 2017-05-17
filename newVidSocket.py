import socket
import threading
import os
import sys
import time

def videoShell():
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
		data = conn.recv(12)
		print data
	s.close()
	sys.exit()

if __name__ == "__main__":
	#try:
	t = threading.Thread(target=videoShell)
	t.start()
	controllerSocket()
	time.sleep(0.1)
	#except:
	#	print "unable to start threads"
