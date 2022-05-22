# About

Welcome! Herein lies the code you need to stream your webcam over the internet.
Work in progress ...

# First Time Instructions

## Install Dependencies

1. Setup directories and create a python virtual environment:

        $ mkdir -p ~/python_ws/webcam-server
        $ cd ~/python_ws/webcam-server
        $ python3 -m venv env
        $ source ./env/bin/activate

2. Install Python requirements:

        $ cd /path/to/personal-webcam-server
		$ pip install -r requirements.txt

# Usage

## Local Development

1. Open a new terminal, and execute:

        $ cd /path/to/personal-webcam-server
		$ ./app.py

2. Open a browser and navigate to `localhost:5000`.

## Remote Access

1. Open a new terminal, and execute:

        $ cd /path/to/personal-webcam-server
		$ gunicorn --threads 4 --workers 1 --bind 192.168.1.70:5000 app:app

2. Open a browser on any device and navigate to `garcia.webhop.me:5000`. The
   explanation for setting up the remote access is not covered in this README.

# Credits

Most of the code credits to Miguel Grinberg, except for the small changes I
made. Thanks!

Website links:
* [Miguel Grinberg Blog](http://blog.miguelgrinberg.com/post/video-streaming-with-flask)
* [GitHub Source Code](https://github.com/miguelgrinberg/flask-video-streaming)
