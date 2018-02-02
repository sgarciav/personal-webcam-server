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
#
# WebSocket code obtained from:
# https://gist.github.com/punchagan/53600958c1799c2dcf26
#
# FlaskSockets:
# https://github.com/kennethreitz/flask-sockets
# ----------------------------------------------------------------------------

import cv2
from flask import Flask, render_template, Response
from flask_sockets import Sockets


app = Flask(__name__)
app.debug = False

sockets = Sockets(app)


@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('WebSockets_index.html')

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message[::-1])

@app.route('/')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(cv2.VideoCapture(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    """Video streaming generator function."""
    while camera.isOpened():

        # read next frame form webcam
        success_read, frame = camera.read()

        # encode frame to jpeg
        if success_read:
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 0.1] # 90 is good
            success_encode, jpeg = cv2.imencode('.jpg', frame, encode_param)
        else:
            print 'Unsuccessfull to read frame from webcam.'

        if success_encode:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            print 'Unsuccessfull econding frame.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
