# About

Welcome! Herein lies the code you need to stream your webcam over the internet.
Work in progress ...

# Install Dependencies

1. Install Python requirements:

		$ pip install -r requirements.txt

2. Install
   [OpenCV3](https://github.com/kratzert/Ubuntu_from_scratch/blob/master/Ubuntu_16_04LTS.md#installing-opencv3)
   from source.

# Usage

Open a new terminal, and execute:

	$ ./app.py

# Troubleshooting

## Problem: camera won't capture video frame

Taken from [GitHub](https://github.com/opencv/opencv/issues/8471):

After compiling OpenCV from source, replace the cv2.so library file:

	$ sudo cp opencv-3.2.0/build/lib/cv2.so /usr/local/lib/python2.7/dist-packages/cv2/

# Credits

Most of the code credits to Miguel Grinberg, except for the small changes I
made. Thanks!

Website links:
* [Miguel Grinberg Blog](http://blog.miguelgrinberg.com/post/video-streaming-with-flask)
* [GitHub Source Code](https://github.com/miguelgrinberg/flask-video-streaming)

# Authors

Sergio Garcia-Vergara <sergiodotgarcia@gmail.com>
