# -------------------------------------------------------------------------------------------
# 	USAGE: python server.py
# -------------------------------------------------------------------------------------------

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from utils import getFrame
from StringIO import StringIO
from io import BytesIO
from PIL import Image
import numpy as np
import scipy.misc
import threading
import urlparse
import base64
import time
import cv2

capture=None

class CamHandler(BaseHTTPRequestHandler):

	def finish_headers(self,filetype="text/html"):
		self.send_header('Content-type',filetype)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()	

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		if parsed_path.path.endswith(".html") or parsed_path.path.endswith(".css") or parsed_path.path.endswith(".png"):
			try:
				path = parsed_path.path[1:]
				html_file = open(path)
				filetype = path[path.index(".")+1:]
				if filetype in ['.png','.jpg','.gif']:
					filetype = "image/"+filetype				
				else:
					filetype = "text/"+filetype
				text = html_file.read()
				self.send_response(200)
				self.finish_headers(filetype=filetype)
				self.wfile.write(text)
			except Exception as e:
				print e
				self.send_response(400)	
				self.finish_headers()		
		else:
			html_file = open("home.html")
			text = html_file.read()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()
			self.wfile.write(text)
				
		return

	def do_POST(self):
		content_length = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_length)
		text = str(post_body)
		text = text[text.index(",")+1:]
                im = Image.open(BytesIO(base64.b64decode(text)))
		data = np.array(im.getdata())
		im = np.array(im.getdata()).reshape(im.size[1], im.size[0], 4)[:,:,:-1]
		im = im.astype(np.uint8)
		frm = getFrame(im)
		_,buf = cv2.imencode('.png',frm)
		frm = base64.b64encode(buf)
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
		self.wfile.write(frm)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def main():
	global capture
	time.sleep(2.0)
	global img
	try:
		server = ThreadedHTTPServer(('localhost',6969), CamHandler)
		print "server started"
		server.serve_forever()
	except KeyboardInterrupt:
		capture.stop()
		server.socket.close()

if __name__ == '__main__':
	main()