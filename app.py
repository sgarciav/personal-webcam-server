#!/usr/bin/env python

# ----------------------------------------------------------------------------
# The MIT License (MIT)

# Copyright (c) 2014 Miguel Grinberg

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------
# Original file can be found in:
# https://github.com/miguelgrinberg/flask-video-streaming
# ----------------------------------------------------------------------------

import cv2
import argparse
from flask import Flask, render_template, Response

app = Flask(__name__)


# user-defined functions
# ---------------------------------------
# ---------------------------------------


# -----------------------
def parse_arguments():
    ''' parse through command line arguments '''
    global args_

    parser = argparse.ArgumentParser(description='Run personal webcam server.')

    # # required values
    # parser.add_argument(
    #     "quality",
    #     type=int,
    #     help="Quality of compression."
    # )

    # optional values
    parser.add_argument(
        "--quality",
        type=float, default=90.0,
        help="Quality of image compression."
    )

    args_ = parser.parse_args()


# main functions
# =======================================

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while camera.isOpened():

        # read next frame form webcam
        success_read, frame = camera.read()

        # encode frame to jpeg
        if success_read:
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), args_.quality] # 90 is good
            success_encode, jpeg = cv2.imencode('.jpg', frame, encode_param)
        else:
            print 'Unsuccessfull to read frame from webcam.'

        if success_encode:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            print 'Unsuccessfull econding frame.'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(cv2.VideoCapture(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ---------------

if __name__ == '__main__':
    parse_arguments()
    app.run(host='0.0.0.0', threaded=True)
