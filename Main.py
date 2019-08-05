from flask import Flask, request, redirect, render_template, send_file
# import cgi
import os
import jinja2
from binConv import *
from rgbConv import *

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

    try: 
        if request.method == "POST":
            msg = (request.form['msg'])
            wid = (request.form['wid'])
            ht = (request.form['ht'])

            txt_color = request.form['txt_color']
            txt_color = conv(txt_color)

            back_color = request.form['back_color']
            back_color = conv(back_color)

            dire = (request.form['dire'])
            tType = (request.form['tType'])
            font = (request.form['form'])
            rot = (request.form['rot'])
            ext = (request.form['ext'])
            text_size = (request.form['text_size'])

            wid = int(wid)
            ht = int(wid)
            text_size = int(text_size)

            img_size = (wid, ht)
            font = ImageFont.truetype(font + ".ttf", text_size)

            if tType == "bin":
                msg = getBinMsg(msg)

            img = Image.new("RGB", img_size, back_color)
            draw = ImageDraw.Draw(img)

            if tType == "rtl":
                rtl(draw, msg, img_size, txt_color, font, text_size)
            
            if tType == "ltr":
                ltr(draw, msg, img_size, txt_color, font, text_size)
            
            if tType == "btt":
                btt(draw, msg, img_size, txt_color, font, text_size)
            
            if tType == "ttb":
                ttb(draw, msg, img_size, txt_color, font, text_size)
            
            if rot > 0:
                img.rotate(rot)
            imageName = msg + ".jpg"
            img.save(imageName)
            img.close()

            # return redirect("/downloads")
            try:
                return send_file("imageName", as_attachment=True, attachment_filename='imageName')
            except Exception as e:
                error = str(e)
                return render_template("error.html", error=error)

            
    except Exception as e:
        error = str(e)
        return render_template("error.html", error=error)

# @app.route("/downloads")
# def download():
#     try:
#         return send_file("imageName", as_attachment=True, attachment_filename='imageName')
#     except Exception as e:
#         error = str(e)
#         return render_template("error.html", error=error)

app.run()
