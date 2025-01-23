from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

offset = 5
target_size = 30
max_offset = 10

def get_font_size(size, text, max_length):
    if size < target_size:
        check_font = ImageFont.truetype('image-template/impact.ttf', size)
        if check_font.getlength(text) >= max_length:
            return size-1
        else:
            return get_font_size(size+1, text, max_length)
    else:
        return target_size

def draw(text, file_path=""):
    template = Image.open("image-template/template.jpeg")
    image = ImageDraw.Draw(template)
    img_w, img_h = template.size
    font_size = get_font_size(1, text, img_w-max_offset)
    myFont = ImageFont.truetype('image-template/impact.ttf', font_size)
    txt_r, txt_b = image.textbbox((0,0), text, font=myFont)[2], image.textbbox((0,0), text, font=myFont)[3]
    image.text(((img_w-txt_r)/2,img_h-txt_b-offset), text, font=myFont, fill=(255, 255, 255))
    file = file_path + "output-" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".jpeg"
    template.save(file)
    return file