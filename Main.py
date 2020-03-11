from flask import Flask, request, redirect, render_template, send_file
# import cgi
import os
import jinja2
from binConv import *
from rgbConv import *
import io

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():

    # if request.method == "GET":
    msg = "Hello world!"
    wid = 1024
    ht = 768
    return render_template("index.html", msg=msg, wid=wid, ht=ht)

    # try: 
    # if request.method == "POST":
       
    #     return send_file(img_io, mimetype='image/jpeg')

            # return redirect("/downloads")
            # try:
                #return send_file("imageName", as_attachment=True, mimetype="image/jpeg", attachment_filename='imageName')
                #return send_file(imageName, mimetype=None, as_attachment=False, attachment_filename=None, add_etags=True, cache_timeout=None, conditional=False, last_modified=None)
                #send_from_directory(file_dir, filename, as_attachment=True, mimetype='application/pdf', attachment_filename=(str(filename) + '.pdf'))
            # except Exception as e:
            #     error = str(e)
            #     return render_template("error.html", error=error)

            
    # except Exception as e:
    #     error = str(e)
    #     return render_template("error.html", error=error)

@app.route('/return-files/')
def return_files_tut():
    try:
        msg = (request.form['msg'])
        wid = int(request.form['wid'])
        ht = int(request.form['ht'])

        txt_color = request.form['txt_color']
        txt_color = conv(txt_color)

        back_color = request.form['back_color']
        back_color = conv(back_color)

        # dire = (request.form['dire'])
        tType = (request.form['tType'])
        font = (request.form['font'])
        rot = (request.form['rot'])
        # ext = (request.form['ext'])
        text_size = (request.form['text_size'])

        wid = int(wid)
        ht = int(wid)
        text_size = int(text_size)

        img_size = (wid, ht)
        font = ImageFont.truetype(font + ".ttf", text_size)

        if tType == "bin":
            msg = getBinMsg(msg)

        img = Image.new("RGB", img_size, "black")
        draw = ImageDraw.Draw(img)

        if tType == "rtl":
            rtl(draw, msg, img_size, txt_color, "Arial", text_size)

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
        # img_io = io.StringIO()
        # img.save(img_io, 'JPEG', quality=70)
        # img_io.seek(0)
        return send_static_file(img, attachment_filename='python.jpg')
    except Exception as e:
        return str(e)


# @app.route("/downloads")
# def download():
#     try:
#         return send_file("imageName", as_attachment=True, attachment_filename='imageName')
#     except Exception as e:
#         error = str(e)
#         return render_template("error.html", error=error)

app.run()
