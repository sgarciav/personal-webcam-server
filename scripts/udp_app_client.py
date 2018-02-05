import socket   #for sockets
import sys  #for exit
import cv2
from flask import Flask, render_template, Response

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = 'localhost';
port = 8888;


def gen(camera):
    """Video streaming generator function."""
    while camera.isOpened():

        # read next frame form webcam
        success_read, frame = camera.read()

        # encode frame to jpeg
        if success_read:
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 0.1] # 90 is good
            # success_encode, jpeg = cv2.imencode('.jpg', frame, encode_param)
            success_encode, jpeg_str = cv2.imencode('.jpg', frame, encode_param)[1].tostring()
        else:
            print 'Unsuccessfull to read frame from webcam.'

        if success_encode:
            # yield (b'--frame\r\n'
            #        b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
            yield jpeg_str
        else:
            print 'Unsuccessfull econding frame.'


while(1) :
    msg = raw_input('Enter message to send : ')
    # msg = Response(gen(cv2.VideoCapture(0)),
    #                mimetype='multipart/x-mixed-replace; boundary=frame')

    try :
        #Set the whole string
        s.sendto(msg, (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print 'Server reply : ' + reply

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
