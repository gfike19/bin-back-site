from flask import Flask, request, redirect, render_template, send_file
import os
import jinja2
from binConv import *
from rgbConv import *
import io
import tempfile
from shutil import copyfileobj

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        msg = "Hello world!"
        wid = 1024
        ht = 768
        return render_template("index.html", msg=msg, wid=wid, ht=ht)
    
    if request.method == "POST":
        try:
            name = "test"
            img_size = (1024, 768)
            txt_color = "white"
            back = "black"
            msg = "test"
            text_size = 24
            img = Image.new("RGB", img_size, back)
            draw = ImageDraw.Draw(img)
            leng = len(msg)
            idx = 0
            font = ImageFont.truetype("arial.ttf", text_size)
            imageName = msg + ".jpg"
            for x in range(0, img_size[1], text_size + text_size // 2):
                for y in range(0, img_size[0], text_size):
                    draw.text((y,x),msg[idx], txt_color, font=font)
                    idx += 1
                    if idx > leng - 1:
                        idx = 0

            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="jpeg")
            img_byte_arr = img_byte_arr.getvalue()
            fp = tempfile.TemporaryFile()
            fp.write(img_byte_arr)
            fp.seek(0,0)
            return send_file(fp, as_attachment=True, attachment_filename='myfile.jpg')
        except Exception as e:
            return str(e)

app.run()
