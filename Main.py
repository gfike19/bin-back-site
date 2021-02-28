from flask import Flask, request, redirect, render_template, send_file
import os
import jinja2
import imageCreator
import rgbConv
import io
import tempfile
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        try:
            # filename will be generated from msg
            msg = request.form['msg']
            fileName = msg + ""
            fontSz = int(request.form['fontSz'])
            txtColor = request.form['txtColor']
            font = request.form["font"]
            font = ImageFont.truetype(font, fontSz)
            bckColor = request.form['bckColor']

            # TODO check to see if text color and background color are the same

            # additional options
            textDirection = request.form['dir']
            binary = bool(request.form['bin'])

            # TODO add capability to rotate image
            # rot = request.form['rot']

            # technical options
            wid = int(request.form['wid'])
            ht = int(request.form['ht'])

            # TODO need to create dictionary or something to generate format dynamically so image can be downloaded
            extension = request.form['ext']
            imageSz = (wid, ht)
            
            # create image object to use in functions
            img = Image.new("RGB", imageSz, bckColor)
            draw = ImageDraw.Draw(img)

            if binary == True:
                msg = imageCreator.getBinMsg(msg)

            # mutates img
            if textDirection == "rtl":
                imageCreator.rtl(draw, msg, imageSz, txtColor, font, fontSz)

            # converts image to binary, writes byte array to temporary file, puts array at the begining 
            # file is returned to user
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="jpeg")
            img_byte_arr = img_byte_arr.getvalue()
            fp = tempfile.TemporaryFile()
            fp.write(img_byte_arr)
            fp.seek(0,0)

            return send_file(fp, as_attachment=True, attachment_filename=fileName + extension)
        except Exception as e:
            return str(e)

app.run()
