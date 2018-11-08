from PIL import Image, ImageDraw, ImageFont
import random

width = 160
height = 50


# 生成随机颜色
def getRandomColor():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)


def getRandomStr():
    random_num = str(random.randint(0, 9))
    random_lower = chr(random.randint(97, 122))  # 数字转ascii码
    random_upper = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_lower, random_upper])
    return random_char


def drawLine(draw):
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())


def drawPoint(draw):
    for i in range(50):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=getRandomColor())


def createImg(img_name):
    bg_color = getRandomColor()
    img = Image.new(mode="RGB", size=(width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    # /System/Library/Fonts/PingFang.ttc
    font = ImageFont.truetype(font="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=36)
    for i in range(5):
        random_item = getRandomStr()
        txt_color = getRandomColor()
        while txt_color == bg_color:
            txt_color = getRandomColor()
        draw.text((10 + 30 * i, 3), text=random_item, fill=txt_color, font=font)
    drawLine(draw)
    drawPoint(draw)
    with open(img_name, "wb") as f:
        img.save(f, format="png")

# createImg()
