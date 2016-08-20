#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


int main () {
	cv::VideoCapture cap(0);
	if (!cap.isOpened()) { return 1; }

	cv::namedWindow("Test");
	cv::namedWindow("Test2");

	while (1) {
		cv::Mat frame, grayFrame, blurFrame;
		int success = cap.read(frame);
		cv::cvtColor(frame, grayFrame, cv::COLOR_BGR2GRAY);
		cv::GaussianBlur(grayFrame, blurFrame, cv::Size(9, 9), 0, 0);
		cv::imshow("Test", frame);
		cv::imshow("Test2", blurFrame);

		if (cv::waitKey(30) == 27) { break; }
	}

	return 0;
}
