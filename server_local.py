from flask import Flask, request, send_from_directory, render_template
from utils_local import getFrame
from OpenSSL import SSL
from io import BytesIO
from PIL import Image
import numpy as np
import base64
import json
import cv2

app = Flask(__name__,static_url_path='/static')
@app.route("/")
def landing_page():
    return render_template('home.html')

@app.route("/about.html")
def about_page():
    return render_template('about.html')

@app.route("/home.html")
def home_page_direct():
    return landing_page()


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/hatpls', methods=['POST'])
def hatpls():
    text = request.data
    if not text:
        return "fuh"
    text = text[text.index(",")+1:]
    im = Image.open(BytesIO(base64.b64decode(text)))
    data = np.array(im.getdata())
    im = np.array(im.getdata()).reshape(im.size[1], im.size[0], 4)[:,:,:-1]
    im = im.astype(np.uint8)
    frm = getFrame(im)
    _,buf = cv2.imencode('.png',frm)
    frm = base64.b64encode(buf)
    return frm

# visit localhost:6000 to view the contents of this.
if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(host="0.0.0.0", port=6000, ssl_context=context)
