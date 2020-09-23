"""
用pillow操作图像
"""
from PIL import Image, ImageFilter


def main():
    image = Image.open('./res/img/conpon1.png')
    image2 = image.copy()
    print((image.format, image.size, image.mode))
    image.show()
    # 剪裁图像
    rect = 0, 0, 20, 60
    image.crop(rect).show()

    # 生成缩略图
    size = 40, 40
    image.thumbnail(size)
    image.show()

    # 缩放和粘贴
    image2.paste(image.resize((x * 2 for x in image.size)), (0, 0))
    image2.show()

    # 旋转
    image2.rotate(90).show()
    # 翻转
    image2.transpose(Image.FLIP_LEFT_RIGHT).show()

    # 操作像素
    for x in range(30, 131):
        for y in range(10, 111):
            image2.putpixel((x, y), (255, 255 - x, 255 - y))
    image2.show()

    # 滤镜效果
    image2.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    main()
