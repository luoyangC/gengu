"""
  Created by Amor on 2018-09-30
  图片处理的脚本
"""
import os
from PIL import Image

__author__ = '骆杨'


def compress_image(file_name):
    image = Image.open('./certificate/{}'.format(file_name))
    width = image.width
    height = image.height
    rate = 1.0  # 压缩率

    # 根据图像大小设置压缩率
    if width >= 2000 or height >= 2000:
        rate = 0.3
    elif width >= 1000 or height >= 1000:
        rate = 0.5
    elif width >= 500 or height >= 500:
        rate = 0.6

    width = int(width * rate)    # 新的宽
    height = int(height * rate)  # 新的高

    image.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
    # if width < height:
    #     cp_im = image.crop((0, 0, width, width))
    # else:
    #     cp_im = image.crop((0, 0, height, height))
    cp_im = image.crop((0, 0, width, height))
    cp_im.save('./certificate/{}'.format(file_name))

def get_file():
    pwd = os.walk('./certificate')
    for item in pwd:
        return item[2]


if __name__ == '__main__':
    file_list = get_file()
    for item in file_list:
        compress_image(item)
