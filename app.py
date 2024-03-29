from flask import Flask, render_template, request, send_file
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import tempfile
import io

app = Flask(__name__)

def getBinMsg(msg):
    lst = []
    for char in msg:
        lst.append(ord(char))

    msg = ""
    for each in lst:
        msg += "{0:b}".format(each)

    return msg 

def rtl(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for x in range(0, img_size[1], text_size):
        for y in range(0, img_size[0], text_size):
            draw.text((y,x),msg[idx], txt_color, font=font)
            idx += 1
            if idx > leng - 1:
                idx = 0

def ltr(draw, msg, img_size, txt_color, font, text_size):
    idx = len(msg)
    for x in range(0, img_size[1], text_size):
        for y in range(0, img_size[0], text_size):
            draw.text((y,x),msg[idx -1], txt_color, font=font)
            idx -= 1
            if idx == 0:
                idx = len(msg)

def ttb(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for y in range(0, img_size[0], text_size):
        for x in range(0, img_size[1], text_size):
            draw.text((y,x),msg[idx], txt_color, font=font)
            idx += 1
            if idx > leng - 1:
                idx = 0

def btt(draw, msg, img_size, txt_color, font, text_size):
    idx = len(msg)
    for x in range(0, img_size[0], text_size):
        for y in range(0, img_size[1],text_size):
            draw.text((x,y),msg[idx], txt_color, font=font)
            idx -= 1
            if idx == 0:
                idx = len(msg)

@app.route("/", methods=['GET'])
def indexGet():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def indexPost():
    try:
        # filename will be generated from msg
        msg = request.form['msg'] + " "
        fileName = msg + ""
        fontSz = int(request.form['fontSz'])
        txtColor = request.form['txtColor']
        font = "arial"

        res = request.form["res"]
        arr = res.split(", ")
        wid = int(arr[0])
        ht = int(arr[1])
        imageSz = (wid, ht)

        # font = ImageFont.truetype(font, fontSz)
        font = ImageFont.load_default()
        bckColor = request.form['bckColor']

        # TODO check to see if text color and background color are the same

        # additional options
        textDirection = request.form['dir']
        binary = bool(request.form.getlist('bin'))

        # TODO add capability to rotate image
        # rot = request.form['rot']

        # technical options
        # wid = int(request.form['wid'])
        # ht = int(request.form['ht'])

        extension = request.form['ext']
        extDict = {
            ".bmp" : "bmp", ".gif" : "gif", ".jpg": "jpeg", ".tiff": "tiff"
        }
        fileFormat = extDict[extension]
        
        # create image object to use in functions
        img = Image.new("RGB", imageSz, bckColor)
        draw = ImageDraw.Draw(img)

        if binary == True:
            msg = getBinMsg(msg)

        # mutates img
        if textDirection == "rtl":
            rtl(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "ltr":
            ltr(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "ttb":
            ttb(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "btt":
            btt(draw, msg, imageSz, txtColor, font, fontSz)

        # converts image to binary, writes bytes to array which is sent to a temporary file, puts array at the begining of
        # file before it is returned to user so stream works properly
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=fileFormat)
        img_byte_arr = img_byte_arr.getvalue()
        fp = tempfile.TemporaryFile()
        fp.write(img_byte_arr)
        fp.seek(0,0)

        return send_file(fp, as_attachment=True, attachment_filename=fileName + extension)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()