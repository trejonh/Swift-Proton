#include "CameraStream.hpp"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <iostream>
#include <ctime>
#include <raspicam/raspicam_cv.h>
using namespace std;
CameraStream::CameraStream(){
	running = true;
}

CameraStream::~CameraStream(){
	running = false;
}

void CameraStream::stop(){
	running = false;
}

void CameraStream::startStream(){
	/*************Socket Setup***********/
		int sockfd, newsockfd, clilen;
	struct sockaddr_in serv_addr, cli_addr;
	int n;

	//Create a socket
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	//If the return is less than 0, then the socket failed to create
	if (sockfd < 0)
	{
		cout << "ERROR opening socket" << endl;
	}
	//Initialize the buffer to all zeros
	memset((void*) &serv_addr, 0, sizeof(serv_addr));
	//Setup the server address structure
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(9000);
	//Bind the socket appropriately
	if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
	{
		cout << "ERROR on binding" << endl;
	}
	//Listen on the socket for an incoming connection
	listen(sockfd,5);
	clilen = sizeof(cli_addr);
	//Block until a client has connected to the server
	newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, (socklen_t*) &clilen);
	//If the return is less than 0l, there is an error
	if (newsockfd < 0)
	{
		cout << "ERROR on accept" << endl;
		running = false;
	}
		/************************************/
	raspicam::RaspiCam_Cv Camera;
	cv::Mat image;
	Camera.set(CV_CAP_PROP_FRAME_WIDTH,640);   // width pixels
	Camera.set(CV_CAP_PROP_FRAME_HEIGHT,480);   // height pixels
	Camera.set(CV_CAP_PROP_GAIN, 0);            // Enable auto gain etc.
	Camera.set( CV_CAP_PROP_FORMAT, CV_8UC1 );
	if (!Camera.open()) {
		cout<<"Error opening the camera"<<endl;
		running = false;
	}
	cv::vector<unsigned char>buff;
	while(running){
		Camera.grab();
		Camera.retrieve(image);
		int imgSize =  image.total()*image.elemSize();
		//makes it continous
		image = (image.reshape(0,1));
		//capture->retrieve(frame,0);
		//Send_All(sockfd,frame.data,imgSize);
		n = write(newsockfd,image.data,imgSize);
		cout << "bytes sents: "<<n<<endl;
		cout << "image size :"<< imgSize<<endl;
		cout << "buffer size: "<< sizeof(buff) <<endl;
		if(n<0){
			cout<<"error writing to socket\n";
			running = false;
		}
		running = false;
	}
	close(sockfd);
	Camera.release();
}