from flask import Flask, render_template, request, send_file
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import tempfile
import io
from ImageCreator import ImageCreator

app = Flask(__name__)

@app.route("/", methods=['GET'])
def indexGet():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def indexPost():
    ic = ImageCreator()
    try:
        # filename will be generated from msg
        msg = request.form['msg'] + " "
        fileName = msg + ""
        fontSz = int(request.form['fontSz'])
        txtColor = request.form['txtColor']
        font = "arial"

        # resolution is pulled from form in array/list form
        res = request.form["res"]
        arr = res.split(", ")
        wid = int(arr[0])
        ht = int(arr[1])
        imageSz = (wid, ht)

        # TODO add custom font capabilities
        # font = ImageFont.truetype(font, fontSz)
        font = ImageFont.load_default()
        bckColor = request.form['bckColor']

        # TODO check to see if text color and background color are the same

        # additional options
        textDirection = request.form['dir']
        binary = bool(request.form.getlist('bin'))

        # TODO add capability to rotate image
        # rot = request.form['rot']

        # TODO add ability to create custom sized image
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
            msg = ic.getBinMsg(msg)

        # mutates img
        if textDirection == "rtl":
            ic.rtl(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "ltr":
            ic.ltr(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "ttb":
            ic.ttb(draw, msg, imageSz, txtColor, font, fontSz)
        
        if textDirection == "btt":
            ic.btt(draw, msg, imageSz, txtColor, font, fontSz)

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