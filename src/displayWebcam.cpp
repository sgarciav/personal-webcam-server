#include<stdio.h>
#include<opencv2/opencv.hpp>

// to avoid having to use cv:: for each variable
using namespace cv;

int main(int argc, char *argv[])
{
	// variable declarations
	VideoCapture cap;
	Mat frame;

	// open the default camera, use something different from 0 otherwise;
	if(!cap.open(0))
	{
		printf("No camera recognized.\n");
		return 1;
	}

	// display continuously
	while(true)
	{
		// create image frames from capture
		cap >> frame;
		
		// show frame as long as frame is not empty
		if (!frame.empty())
			imshow("smile! :)", frame);
		
		// stop capturing by pressing ESC
		if (waitKey(1) == 27)
			break;
	}

	// the camera will be closed automatically upon exit
	return 0;
}
