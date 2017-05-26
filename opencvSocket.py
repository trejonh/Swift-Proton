import socket
import threading

running = True

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
	t1 = threading.Thread(target=controllerSocket)
	t1.start()
	while running:
		q = raw_input("enter q to quit")
		if q=="q":
			running = False
	#except:
	#	print "unable to start threads"
