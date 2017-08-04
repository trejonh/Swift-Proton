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
#include <boost/array.hpp>
#include <boost/asio.hpp>
#include <vector>
using boost::asio::ip::udp;
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
	try
	{
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
			boost::asio::io_service io_service;
			udp::socket socket(io_service, udp::endpoint(udp::v4(), 13));
			vector<uchar> buff;
			vector<int> params;
			params.push_back(cv::IMWRITE_JPEG_QUALITY);
			params.push_back(80);
			cv::imencode(".jpg", image, buff, params);
			udp::endpoint remote_endpoint;
			boost::system::error_code error;
			socket.receive_from(boost::asio::buffer(recv_buf),
			  remote_endpoint, 0, error);

			if (error && error != boost::asio::error::message_size)
				throw boost::system::system_error(error);

			boost::system::error_code ignored_error;
			socket.send_to(boost::asio::buffer(buff), remote_endpoint, 0, ignored_error);			
		}
		Camera.release();
	}
	catch (std::exception& e)
	{
		std::cerr << e.what() << std::endl;
	}
}