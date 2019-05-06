#!/usr/bin/env python3
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class MyRequestHandler(BaseHTTPRequestHandler):
 
  def do_GET(self):
        self.send_response(200)
 
        self.send_header('Content-type','text/plain')
        self.end_headers()
 
        message = "server: " + socket.gethostname() + "\n"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  httpd = HTTPServer(('0.0.0.0', 8080), MyRequestHandler)
  print('Started.')
  httpd.serve_forever()
 
run()