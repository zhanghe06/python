# encoding: utf-8
__author__ = 'zhanghe'

import os
from PIL import Image

SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'


def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'jpeg' in f)


def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)


if __name__ == '__main__':
    img_folder = os.path.abspath(
        '11_18_2013_R000_IQM_Big_Sur_Mon__e10d1958e7b766c3e840')
    os.mkdir(os.path.join(img_folder, SAVE_DIRECTORY))

    images = get_image_paths(img_folder)

    for image in images:
        create_thumbnail(Image)