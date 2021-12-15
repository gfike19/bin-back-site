# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw

class ImageCreator:

    #TODO create function that doesn't convert spaces to binary?
    def getBinMsg(self, msg):
        lst = []
        for char in msg:
            lst.append(ord(char))

        msg = ""
        for each in lst:
            msg += "{0:b}".format(each)

        return msg 

    def rtl(self, draw, msg, img_size, txt_color, font, text_size):
        leng = len(msg)
        idx = 0
        for x in range(0, img_size[1], text_size):
            for y in range(0, img_size[0], text_size):
                draw.text((y,x),msg[idx], txt_color, font=font)
                idx += 1
                if idx > leng - 1:
                    idx = 0

    def ltr(self, draw, msg, img_size, txt_color, font, text_size):
        idx = len(msg)
        for x in range(0, img_size[1], text_size):
            for y in range(0, img_size[0], text_size):
                draw.text((y,x),msg[idx -1], txt_color, font=font)
                idx -= 1
                if idx == 0:
                    idx = len(msg)

    def ttb(self, draw, msg, img_size, txt_color, font, text_size):
        leng = len(msg)
        idx = 0
        for y in range(0, img_size[0], text_size):
            for x in range(0, img_size[1], text_size):
                draw.text((y,x),msg[idx], txt_color, font=font)
                idx += 1
                if idx > leng - 1:
                    idx = 0

    def btt(self, draw, msg, img_size, txt_color, font, text_size):
        idx = len(msg)
        for x in range(0, img_size[0], text_size):
            for y in range(0, img_size[1],text_size):
                draw.text((x,y),msg[idx], txt_color, font=font)
                idx -= 1
                if idx == 0:
                    idx = len(msg)