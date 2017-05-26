
#ifndef CAMERASTREAM_HPP_
#define CAMERASTREAM_HPP_
#include <raspicam/raspicam_cv.h>
/**
 * Client can send live audio and video data to a specified server
 */
class CameraStream{
public:
	CameraStream();
	~CameraStream();
	void startStream();
	void stop();
private:
	bool running;
};

#endif /* CLIENT_HPP_ */
