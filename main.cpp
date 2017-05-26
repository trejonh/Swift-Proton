#include "CameraStream.hpp"
#include <thread>
#include <pthread.h>
#include <python2.7/Python.h>
#include <stdio.h>
using namespace std;
int main(void){
	CameraStream cam;
	thread t(&CameraStream::startStream,cam);
	Py_Initialize();
    FILE *fd = fopen("opencvSocket.py", "r");
	PyRun_SimpleFileEx(fd, "opencvSocket.py", 1);
    Py_Finalize();
	return 0;
}