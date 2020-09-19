#!/usr/bin/python3

import io
import picamera
from threading import Condition
import http.server
import socketserver
import base64

# Server config
PORT = 8000

# Camera config
width = 150
height = 120
fps = 20
rotation = 180 # degrees

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    allow_reuse_address = True
    def do_GET(self):
        if self.path == '/build/tex.jpg' or self.path == '/tex.jpg':
            with output.condition:
                output.condition.wait()
                frame = output.frame
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(base64.b64encode(frame))

            self.wfile.write(b'\r\n')
        else:
            super().do_GET()

class MyServer(socketserver.TCPServer):
    allow_reuse_address = True

with picamera.PiCamera(resolution=str(width) + "x" + str(height), framerate=fps) as camera:
    global cam
    cam = camera
    cam.rotation = rotation
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg', bitrate=3500000, quality=40)
    try:
        with MyServer(("", PORT), MyHandler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
    finally:
        camera.stop_recording()