# msg = (request.form['msg'])
#             wid = int(request.form['wid'])
#             ht = int(request.form['ht'])

#             txt_color = request.form['txt_color']
#             txt_color = conv(txt_color)

#             back_color = request.form['back_color']
#             back_color = conv(back_color)

#             # dire = (request.form['dire'])
#             tType = (request.form['tType'])
#             font = (request.form['font'])
#             rot = (request.form['rot'])
#             # ext = (request.form['ext'])
#             text_size = (request.form['text_size'])

#             wid = int(wid)
#             ht = int(wid)
#             text_size = int(text_size)

#             img_size = (wid, ht)
#             font = ImageFont.truetype(font + ".ttf", text_size)

#             if tType == "bin":
#                 msg = getBinMsg(msg)

#             img = Image.new("RGB", img_size, "black")
#             draw = ImageDraw.Draw(img)

#             if tType == "rtl":
#                 rtl(draw, msg, img_size, txt_color, font, text_size)

#             if tType == "ltr":
#                 ltr(draw, msg, img_size, txt_color, font, text_size)

#             if tType == "btt":
#                 btt(draw, msg, img_size, txt_color, font, text_size)

#             if tType == "ttb":
#                 ttb(draw, msg, img_size, txt_color, font, text_size)

#             if rot > 0:
#                 img.rotate(rot)