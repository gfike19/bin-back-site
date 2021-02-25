from flask import Flask, request, redirect, render_template, send_file
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import os
import jinja2
import io
from PIL import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/test", methods=['GET', 'POST'])
def test():

    if request.method == "GET":
        return render_template("test.html")
    
    if request.method == "POST":
        img_size = (1024, 768)
        img = Image.new("RGB", img_size, "black")
        draw = ImageDraw.Draw(img)
        leng = len("Hello world! ")
        idx = 0
        for x in range(0, img_size[1], 12):
            for y in range(0, img_size[0], 12):
                draw.text((y,x),msg[idx], "green", font="arial.ttf")
                idx += 1
                if idx > leng - 1:
                    idx = 0
        img.save("test.jpg")
        img.close()

        return img
    
app.run()